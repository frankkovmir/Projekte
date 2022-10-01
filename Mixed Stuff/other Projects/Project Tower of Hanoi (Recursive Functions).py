"""
Solve Tower of Hanoi recusive

Tower of Hanoi is a math. game, which has three rules.
There are 3 rods with 3 discs, which are different sizes (smaller from low to high)
The Goal is to get all discs over to the rightmost rod

1. You can only move one disc at the time
2. You can only take the top disk and place on top of another rod
3. You cannot place a bigger disk on top of a smaller disk
"""

towers = [[3,2,1], [], []] #these are our rods

def move(towers, from_tower, dest_tower): #number of towers, from tower, to tower
    disk = towers[from_tower].pop()
    #take last disc (so the highest, smallest one) and append to the destionation rod (tower)
    towers[dest_tower].append(disk)
    return towers

def print_towers(towers): #helper function for visualization
    for i in range(len(towers), 0, -1):
        for tower in towers:
            if len(tower) >= i:
                print(tower[i-1], end = '  ')
            else:
                print('|', end = '  ')
        print()
    print('-------')

def solve_tower_of_hanoi(towers, n, start_tower, dest_tower, aux_tower):
    if n == 0:
        return
    #Move subproblem of n-1 disks from startower to auxtower
    solve_tower_of_hanoi(towers, n-1, start_tower, aux_tower, dest_tower)
    #Move disk n to dest_tower
    move(towers, start_tower, dest_tower)
    print_towers(towers)
    #move subproblem of n-1 from aux-tower to dest_tower
    solve_tower_of_hanoi(towers, n-1, aux_tower, dest_tower, start_tower)


print(solve_tower_of_hanoi(towers, 3, 0, 2, 1))