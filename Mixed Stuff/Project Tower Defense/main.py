# import libraries
import pygame
import math
import ctypes
import sys
from enemy import Enemy
import random
import button
import os



# initialise pygame
pygame.init()

# game window
SCREEN_WIDTH = 1650
SCREEN_HEIGHT = 900

# create game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(f"Frank's Castle Defender")

clock = pygame.time.Clock()
FPS = 60

#define game variables
level = 1
level_difficulty = 0
high_score = 0
target_difficulty = 2100
DIFFICULTY_MULTIPLIER = 1.2 #increase each level bei 10%
game_over = False
next_level = False
ENEMY_TIMER = 900
last_enemy = pygame.time.get_ticks()
enemies_alive = 0
TOWER_COST = 1250
max_towers = 6
tower_positions = [
[SCREEN_WIDTH - 900, SCREEN_HEIGHT - 800],
[SCREEN_WIDTH - 1200, SCREEN_HEIGHT - 800],
[SCREEN_WIDTH - 800, SCREEN_HEIGHT - 300],
[SCREEN_WIDTH - 1100, SCREEN_HEIGHT - 300],
[SCREEN_WIDTH - 1500, SCREEN_HEIGHT - 800],
[SCREEN_WIDTH - 1400, SCREEN_HEIGHT - 300]
]

#load high score
if os.path.exists('score.txt'):
    with open('score.txt', "r") as fhandle:
        high_score = int(fhandle.read())


# define colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
PINK = (235, 65, 54)
GREY = (100,100,100)

#define font
font = pygame.font.SysFont('Futura', 30)
font_60 = pygame.font.SysFont('Futura', 60)
font_90 = pygame.font.SysFont('Futura', 90)
# load images
bg = pygame.image.load('img/bg.png').convert_alpha()
width = bg.get_width()
height = bg.get_height()
scale = 0.45
bg = pygame.transform.scale(bg, (int(width * scale), int(height * scale)))




# castle image
castle_img_100 = pygame.image.load('img/castle/castle_100.png').convert_alpha()
castle_img_50 = pygame.image.load('img/castle/castle_50.png').convert_alpha()
castle_img_25 = pygame.image.load('img/castle/castle_25.png').convert_alpha()

#tower image

tower_img_100 = pygame.image.load('img/tower/tower_100.png').convert_alpha()
tower_img_50 = pygame.image.load('img/tower/tower_50.png').convert_alpha()
tower_img_25 = pygame.image.load('img/tower/tower_25.png').convert_alpha()

# bulletbullet image
bullet_img = pygame.image.load('img/bullet.png').convert_alpha()
b_width = bullet_img.get_width()
b_height = bullet_img.get_height()
b_scale = 0.3
bullet_img = pygame.transform.scale(bullet_img, (int(b_width * b_scale), int(b_height * b_scale)))

# enemy image
enemy_animations = []
enemy_types = ['knight', 'goblin', 'purple_goblin', 'red_goblin']
enemy_health = [225, 300, 375, 700]

# button images
repair_img = pygame.image.load('img/repair.png').convert_alpha()
armor_img = pygame.image.load('img/armour.png').convert_alpha()

#music

shot_fx = pygame.mixer.Sound('audio/cannonball-89596 (online-audio-converter.com).wav')
shot_fx.set_volume(0.02)
castle_shot_fx = pygame.mixer.Sound('audio/cannonball-89596 (online-audio-converter.com).wav')
castle_shot_fx.set_volume(0.03)
main_music = pygame.mixer.Sound('audio/kingdom-of-fantasy-version-60s-10817.wav')
main_music.set_volume(0.03)
main_music.play(-1)
attack_music = pygame.mixer.Sound('audio/mixkit-sword-strikes-armor-2765.wav')
attack_music.set_volume(0.04)
repair_music = pygame.mixer.Sound('audio/Hammer-hitting-single-tap-on-metal-1-www.FesliyanStudios.com (online-audio-converter.com).wav')
repair_music.set_volume(0.06)
build_music = pygame.mixer.Sound('audio/mixkit-sci-fi-construction-complete-811.wav')
build_music.set_volume(0.04)
health_music = pygame.mixer.Sound('audio/mario-1-up (online-audio-converter.com).wav')
health_music.set_volume(0.04)
next_music = pygame.mixer.Sound('audio/Project-Name.wav')
next_music.set_volume(0.04)
game_over_music = pygame.mixer.Sound('audio/mario-meme (online-audio-converter.com).wav')
game_over_music.set_volume(0.04)

animation_types = ['walk', 'attack', 'death']

for enemy in enemy_types:
    # load animation
    animation_list = []
    for animation in animation_types:
        # reset temp list of images
        temp_list = []
        # define number of frames
        num_of_frames = 20
        for i in range(num_of_frames):
            img = pygame.image.load(f'img/enemies/{enemy}/{animation}/{i}.png').convert_alpha()
            e_w = img.get_width()
            e_h = img.get_height()
            e_scale = 0.5
            t_scale = 2
            img = pygame.transform.scale(img, (int(e_w * e_scale), int(e_h * e_scale)))
            temp_list.append(img)
        animation_list.append(temp_list)
    enemy_animations.append(animation_list)

#function to put text on screen

def draw_text(text,font,text_col,x,y):
    img = font.render(text,True,text_col)
    screen.blit(img,(x,y))

#function for displaying status
def show_info():
    draw_text('Money: ' + str(castle.money), font, GREY, 10, 10)
    draw_text('Score: ' + str(castle.score), font, GREY, 10, 35)
    draw_text('High Score: ' + str(high_score), font, GREY, 450, 10)
    draw_text('Level: ' + str(level), font, GREY, 450, 35)
    draw_text('Health: ' + str(castle.health) + " / " + str(castle.max_health), font, RED, 1100, 800)
    draw_text('750', font, RED, 1120, 75)
    draw_text('1250', font, RED, 1200, 75)
    draw_text('500', font, RED, 1275, 75)
# castle class
class Castle():
    def __init__(self, image100, image50, image25, x, y, scale):
        self.health = 1200
        self.max_health = self.health
        self.fired = False
        self.money = 0
        self.score = 0
        self.x = x
        self.y = y

        width = image100.get_width()
        height = image100.get_height()

        self.image100 = pygame.transform.scale(image100, (int(width * scale), int(height * scale)))
        self.image50 = pygame.transform.scale(image50, (int(width * scale), int(height * scale)))
        self.image25 = pygame.transform.scale(image25, (int(width * scale), int(height * scale)))
        self.rect = self.image100.get_rect()
        self.rect.x = x
        self.rect.y = y

    def shoot(self):
        pos = pygame.mouse.get_pos()
        x_dist = pos[0] - self.rect.midleft[0]
        y_dist = -(pos[1] - self.rect.midleft[1])
        self.angle = math.degrees(math.atan2(y_dist, x_dist))
        # get mouseclick
        if pygame.mouse.get_pressed()[0] and self.fired == False and pos[1] > 200:  # leftclick middle = 1, right = 2
            self.fired = True
            castle_shot_fx.play(0,800,400)
            bullet = Bullet(bullet_img, self.rect.midleft[0], self.rect.midleft[1], self.angle)
            bullet_group.add(bullet)
        # rest mouseclick
        if pygame.mouse.get_pressed()[0] == False:  # leftclick middle = 1, right = 2
            self.fired = False

    def repair(self):
        if self.money >= 750 and self.health < self.max_health:
            self.health += 500
            self.money -= 500
            repair_music.play(0,900,300)
            if self.health > self.max_health:
                self.health = self.max_health

    def armor(self):
        if self.money >= 500:
            self.max_health += 250
            self.money -= 500
            health_music.play()

    def draw(self):
        # check which image to use based on health
        if self.health <= 250:
            self.image = self.image25
        elif self.health <= 500:
            self.image = self.image50
        else:
            self.image = self.image100

        screen.blit(self.image, self.rect)


class Tower(pygame.sprite.Sprite):
    def __init__(self, image100, image50, image25, x, y, scale):
        pygame.sprite.Sprite.__init__(self)

        self.target_acquired = False
        self.angle = 0
        self.last_shot = pygame.time.get_ticks() #timestamp when tower was created

        width = image100.get_width()
        height = image100.get_height()

        self.image100 = pygame.transform.scale(image100, (int(width * scale), int(height * scale)))
        self.image50 = pygame.transform.scale(image50, (int(width * scale), int(height * scale)))
        self.image25 = pygame.transform.scale(image25, (int(width * scale), int(height * scale)))
        self.image = self.image100
        self.rect = self.image100.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, enemy_group):
        self.target_acquired = False
        target_x = 0
        target_y = 0
        for e in enemy_group:
            if e.alive:
                target_x, target_y = e.rect.midbottom
                self.target_acquired = True
                break
        if self.target_acquired:
            #pygame.draw.line(screen, WHITE, (self.rect.midleft[0], self.rect.midleft[1]), (target_x, target_y))
            pos = pygame.mouse.get_pos()
            x_dist = target_x - self.rect.midleft[0]
            y_dist = -(target_y - self.rect.midleft[1])
            self.angle = math.degrees(math.atan2(y_dist, x_dist))


            shot_cooldown = 1000 #ms
            #fire bullet
            if pygame.time.get_ticks() - self.last_shot > shot_cooldown:
                self.last_shot = pygame.time.get_ticks()
                bullet = Bullet(bullet_img, self.rect.midleft[0], self.rect.midleft[1], self.angle)
                bullet_group.add(bullet)
                castle_shot_fx.play()

            # check which image to use based on health

            if castle.health <= 250:
                self.image = self.image25
            elif castle.health <= 500:
                self.image = self.image50
            else:
                self.image = self.image100

            screen.blit(self.image, self.rect)



class Bullet(pygame.sprite.Sprite):
    def __init__(self, image, x, y, angle):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.angle = math.radians(angle)
        self.speed = 10
        # calculate horizontal and vertical speeds based on the angle
        self.dx = math.cos(self.angle) * self.speed
        self.dy = -(math.sin(self.angle) * self.speed)

    def update(self):
        # check if bullet has gone off the screen
        if self.rect.right < 0 or self.rect.left > SCREEN_WIDTH or self.rect.bottom < 0 or self.rect.top > SCREEN_HEIGHT:
            self.kill()

        # move bullet
        self.rect.x += self.dx * 1.5
        self.rect.y += self.dy * 1.5

class Crosshair():
    def __init__(self, scale):
        image = pygame.image.load('img/crosshair.png').convert_alpha()
        width = image.get_width()
        height = image.get_height()

        self.image = pygame.transform.scale(image, (int(width * scale), int(height*scale)))
        self.rect = self.image.get_rect()

        #hide mouse
        pygame.mouse.set_visible(False)

    def draw(self):
        mx, my = pygame.mouse.get_pos()
        self.rect.center = mx, my
        screen.blit(self.image, self.rect)


# create castle
castle = Castle(castle_img_100, castle_img_50, castle_img_25, SCREEN_WIDTH - 580, SCREEN_HEIGHT - 840, 0.6)
crosshair = Crosshair(0.10)

#create buttons
repair_button = button.Button(SCREEN_WIDTH - 550, 0.1, repair_img, 0.8)
tower_button = button.Button(SCREEN_WIDTH - 450, 0.1, tower_img_100, 0.1)
armour_button = button.Button(SCREEN_WIDTH - 380, 12, armor_img, 1.5)

# create groups
tower_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()

# game loop
run = True
idle = False
while run:

    clock.tick(FPS)

    if game_over == False:
        screen.blit(bg, (0, 0))

        #draw castle
        castle.draw()
        castle.shoot()
        #draw towers
        tower_group.draw(screen)
        tower_group.update(enemy_group)

        #draw crosshair
        crosshair.draw()

        #draw bullets
        bullet_group.update()
        bullet_group.draw(screen)

        #draw enemies
        enemy_group.update(screen, castle, bullet_group)

        #show details
        show_info()

        #draw buttons
        if repair_button.draw(screen):
            castle.repair()
        if tower_button.draw(screen):
            if castle.money >= TOWER_COST and len(tower_group) < max_towers:
                tower = Tower(
                    tower_img_100,
                    tower_img_50,
                    tower_img_25,
                    tower_positions[len(tower_group)][0],
                    tower_positions[len(tower_group)][1],
                    0.6)
                tower_group.add(tower)
                castle.money -= TOWER_COST
                build_music.play(0, 900, 300)
        if armour_button.draw(screen):
            castle.armor()

        #create enemies
        #check if max number of enemies has been reached
        if level_difficulty < target_difficulty:
            if pygame.time.get_ticks() - last_enemy > ENEMY_TIMER:
                e = random.randint(0, len(enemy_types) -1)
                enemy = Enemy(enemy_health[e], enemy_animations[e], -200, SCREEN_HEIGHT - random.randrange(220, 530), 1)
                #reset enemy timer
                last_enemy = pygame.time.get_ticks()
                enemy_group.add(enemy)
                #increas level difficulty by enemy_health[0]
                level_difficulty += enemy_health[e]


        #check if all the enemies have been spawned
        if level_difficulty >= target_difficulty:
            #check how many are still alive
            enemies_alive = 0
            for e in enemy_group:
                if e.alive == True:
                    enemies_alive += 1
            #if there are none alive the level is complete
            if enemies_alive == 0 and next_level == False:
                next_level = True
                level_reset_time = pygame.time.get_ticks()

        #move onto the next level
        if next_level == True:
            draw_text('LEVEL COMPLETE!', font_60, WHITE, 600, 500)
            next = True
            if next:
                next_music.play()
                next = False
            #update high score
            if castle.score > high_score:
                high_score = castle.score
                with open('score.txt', 'w') as file:
                    file.write(str(high_score))
            if pygame.time.get_ticks() - level_reset_time > 5000:
                next_level = False
                level += 1
                last_enemy = pygame.time.get_ticks()
                target_difficulty *= DIFFICULTY_MULTIPLIER
                level_difficulty = 0
                enemy_group.empty()

        #check game over
        if castle.health <= 0:
            game_over = True
            idle = True


    if game_over == True:
        screen.fill(WHITE)
        draw_text('YOU SUCK!', font_90, BLACK, 580, 410)
        draw_text('PRESS "A" TO PLAY AGAIN!', font_60, BLACK, 480, 480)
        main_music.stop()
        if idle == True:
            game_over_music.play(0)
            idle = False
        pygame.mouse.set_visible(True)
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            #reset variables
            game_over = False
            level = 1
            target_difficulty = 2400
            level_difficulty = 0
            last_enemy = pygame.time.get_ticks()
            enemy_group.empty()
            main_music.play()
            tower_group.empty()
            castle.score = 0
            castle.health = 1000
            castle.max_health = castle.health
            castle.money = 0
            pygame.mouse.set_visible(False)

    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ctypes.windll.user32.MessageBoxW(0, "Ich geb dir Headshot in CS ;)", "Das wirst du bereuen!",
                                             1)  # message box
            run = False
        if event.type == pygame.KEYDOWN:  # on downpress
            if event.key == pygame.K_ESCAPE:
                ctypes.windll.user32.MessageBoxW(0, "Ich geb dir Headshot in CS ;)", "Das wirst du bereuen!",
                                                 1)  # message box
                pygame.quit()  # stop pygame
                sys.exit()  # stop script
    # update display window
    pygame.display.update()

pygame.quit()