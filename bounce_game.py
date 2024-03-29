# Christmas Lights Bouncing Game
# MUST DO
# Add Lights
# Add Sound Effects
# MAYBE DO
# Add strike zone


import sys
import pygame
import random
import time
import board
import neopixel

pygame.init()
pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 150

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(pixel_pin, num_pixels,
                           brightness=0.8, auto_write=False, pixel_order=ORDER)
size = width, height = 600, 10
speed = 2
black = 0, 0, 0
white = (255, 255, 255)
screen = pygame.display.set_mode(size)
score = [0, 0]
position = 50
strikezone = 50
speed_multiplier = 1.5


def testBounce():
    pixels.fill((0, 255, 0))
    for i in range(num_pixels):
        time.sleep(.1)
        pixels[i] = (255, 0, 0)
        if(i > 0):
            pixels[i-1] = (0, 255, 0)


testBounce()


def changePos():
    return random.randint(0+width/4, 3*width/4)


# Main Game Loop
while 1:
    # Scoring
    if(score[0] > 10):
        pygame.mixer.music.load('Score.ogg')
        pygame.mixer.music.play(0)
        print('Player 0 wins')
        score = [0, 0]
    if(score[1] > 10):
        pygame.mixer.music.load('Score.ogg')
        pygame.mixer.music.play(0)
        print('Player 1 wins')
        score = [0, 0]

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.unicode == 'a':
                if position < strikezone:
                    pygame.mixer.music.load('Pop.ogg')
                    pygame.mixer.music.play(0)
                    if position < strikezone/2:
                        print('Strike zone hit!')
                        speed *= speed_multiplier
                    else:
                        speed *= speed_multiplier
                    speed = -speed
            if event.unicode == 's':
                if position > width-strikezone:
                    pygame.mixer.music.load('Pop.ogg')
                    pygame.mixer.music.play(0)

                    if position > width-strikezone/2:
                        print('Strike zone hit!')
                        speed *= speed_multiplier
                    else:
                        speed *= speed_multiplier
                    speed = -speed

            if event.unicode == 'q':
                sys.exit()
    # Movement
    position = position + speed
    # CHeck for Position
    if position < 0 or position > width:
        pygame.mixer.music.load('Score.ogg')
        pygame.mixer.music.play(0)
        # They Lose
        if position < 0:
            score[0] += 1

        if position > width:
            score[1] += 1
        print(score)
        position = changePos()
        speed = speed_multiplier * random.choice([-1, 1])

    # Draw Screen
    screen.fill(black)
    pygame.draw.rect(screen, white, [position, 0, 10, 10])
    pygame.display.flip()
