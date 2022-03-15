import pygame
from pygame import Color
import random
import math

# DISPLAY

# Pygame
pygame.init()
pygame.mixer.init()

# Set-up
empty = Color(0, 0, 0, 0)
screen = pygame.display.set_mode((548, 248))
sky = pygame.image.load('sky.png').convert()
grass = pygame.Surface((550, 50))
grass.fill('darkgreen')
icon = pygame.image.load('icon.png').convert()
pygame.display.set_icon(icon)

# Animations


# Colours
transparent = (0, 0, 0, 0)

# Settings
font = pygame.font.Font(None, 35)
rasengan_text = font.render('Rasengan!', False, 'Cyan')
kage_text = font.render('Kage-bunshin no jutsu!', False, 'Darkblue')

# Window
pygame.display.set_caption('Naruto World')
clock = pygame.time.Clock()

# Naruto
naruto = pygame.image.load('naruto.png').convert_alpha()
go = 1
go_2 = 2
jump = 0
walk = 0
clone = False
clone_freq = []


# Attacks
ninja_enemy = pygame.image.load('ninja-star.png').convert_alpha()
ninja_enemy_x = 250
advance = [1, 2, 3, 4, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 1, 1, 1, 0, 2]
advance_rand = random.choice(advance)
chakra = 100

# Naruto_jutsu
rasengan = pygame.image.load('rasengan.png').convert_alpha()
rasengan_1 = False
star = pygame.image.load('ninja-star.png').convert_alpha()
star_1 = False
star_freq = 2
clone = False



# Functions

def check_near(object1_x, object1_y, object2_x, object2_y):
    x_diff = object1_x - object2_x
    if x_diff <= 10:
        y_diff = object1_y - object2_y
        if y_diff <= 5:
            return True
        else:
            return False
    else:
        return False


# GAME

while True:
    # Display
    screen.blit(sky, (0, 0))
    screen.blit(grass, (0, 200))

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit('You left the game')
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit('You left the game')
            if event.key == pygame.K_SPACE:
                jump += 5
            if event.key == pygame.K_UP:
                jump += 5
            if event.key == pygame.K_DOWN:
                jump -= 5
            if event.key == pygame.K_1:
                if rasengan_1 == False:
                    rasengan_1 = True
                elif rasengan_1 == True:
                    rasengan_1 = 23
                elif rasengan_1 == 22:
                    rasengan_1 = False
                    go_2 = 1
            if event.key == pygame.K_2:
                if star_1 == False:
                    star_1 = True
                elif star_1 == True:
                    go -= 40
                    star_1 = 23
                elif star_1 == 22:
                    star_1 = False
                    go = 1
            if event.key == pygame.K_LEFT:
                walk += 5
            if event.key == pygame.K_RIGHT:
                walk -= 5
            if event.key == pygame.K_EQUALS:
                if clone == False:
                    clone = True
                elif clone == True:
                    clone = False
                    chakra -= 5

    chakra_text = font.render(f'Chakra: {int(chakra)}', False, 'Black')
    star_text = font.render(f'{star_freq}/9', False, 'Black')

    screen.blit(chakra_text, (0, 0))
    # screen.blit(star_text,(460,0))
    # screen.blit(star,(280,-205))

    chakra += 0.002

    if chakra <= 0:
        jump = 0
        walk = 0
        print("Naruto: Oh no! I ran out of chakra!")
        rasengan_1 = False
        star_1 = False
        clone = False
        chakra = 99

    if chakra >= 99:
        chakra = 99

    # if star_freq == 1:
    # print("Naruto: Oh no! I have only 1 ninja-star left! I can't use it!")

    # if star_freq > 9:
    # star_freq = 9
    # print("Naruto: There's no space for more ninja-stars.")

    # Attacks

    ninja_enemy_x -= advance_rand
    if ninja_enemy_x < -220:
        ninja_enemy = None
        ninja_enemy = pygame.image.load('ninja-star.png')
        ninja_enemy_x *= -1
    screen.blit(ninja_enemy, (ninja_enemy_x, -55))

    # Naruto
    y_1 = [17, 16]
    x_1 = [-1, 2, 1]
    rand_y = random.choice(y_1)
    rand_x = random.choice(x_1)

    if -jump >= 10:
        jump = 0

    if -jump <= -100:
        jump = 0
    screen.blit(naruto, (-walk, -jump))

    if clone == True:
            screen.blit(naruto, (-walk - 50, -jump))
            screen.blit(kage_text, (20, 20))

    if rasengan_1 == True:
        if clone == True:
            screen.blit(rasengan, (-walk - 70, -jump + rand_y))
            screen.blit(kage_text, (20, 20))
        else:
            print("Naruto: I need a shadow clone to make the rasengan!")
            clone = True

    if rasengan_1 == 23:
        screen.blit(rasengan_text, (20, 20))
        screen.blit(rasengan, (go_2 + rand_x, -jump + rand_y))
        go_2 += 3
        if go_2 >= 400:
            rasengan_1 = 22
            chakra -= 20

    if star_1 == True:
        screen.blit(star, (-walk - 125, -jump - 65))

    if star_1 == 23:
        screen.blit(star, (go, -jump - 65))
        go += 2
        if go >= 400:
            star_1 = 22
            # star_freq -= 1

    # Collisions

    # Running
    pygame.display.update()
    clock.tick(80)
