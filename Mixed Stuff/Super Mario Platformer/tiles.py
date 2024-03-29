import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, position, size):
        super().__init__()
        self.image = pygame.Surface((size,size)) # x and y
        self.image.fill('grey')
        self.rect = self.image.get_rect(topleft = position)

    def update(self, x_shift):
        self.rect.x += x_shift