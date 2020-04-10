#!/usr/bin/env python3

# Import The Pygame Library And Initialise The Game Engine
import pygame

# Import Paddle Class
from paddle import Paddle

# Import Ball Class
from ball import Ball

# Import Brick Class
from brick import Brick

pygame.init()

# Defining Colours
white = (255, 255, 255)
darkblue = (36, 90, 190)
lightblue = (0, 176, 240)
red = (255, 0, 0)
orange = (255, 100, 0)
yellow = (255, 255, 0)

# Defining Global Variables (Score & Lives)
score = 0
lives = 3

# Opening A Game Window
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("BreakOut")

# This Will Be A List Containing All Sprites We Intend To Use In The Game
all_sprites_list = pygame.sprite.Group()

# Create The Paddle
paddle = Paddle(lightblue, 100, 10)
paddle.rect.x = 350
paddle.rect.y = 560

# Create The Ball
ball = Ball(white, 10, 10)
ball.rect.x = 345
ball.rect.y = 195

# Create Bricks

all_bricks = pygame.sprite.Group()
for i in range(7):
    brick = Brick(red, 80, 30)
    brick.rect.x = 60 + i*100
    brick.rect.y = 60
    all_sprites_list.add(brick)
    all_bricks.add(brick)
for i in range(7):
    brick = Brick(orange, 80, 30)
    brick.rect.x = 60 + i*100
    brick.rect.y = 100
    all_sprites_list.add(brick)
    all_bricks.add(brick)
for i in range(7):
    brick = Brick(yellow, 80, 30)
    brick.rect.x = 60 + i*100
    brick.rect.y = 140
    all_sprites_list.add(brick)
    all_bricks.add(brick)

# Add Paddle & Ball To List Of Sprites
all_sprites_list.add(paddle)
all_sprites_list.add(ball)

# Game Loop

# The Loop Will Carry On Until The User Exits The Game
carryOn = True

# The Clock Will Be Used To Control How Fast The Screen Updates
clock = pygame.time.Clock()

# Main Program Loop
while carryOn:

    # Main Event Loop
    for event in pygame.event.get():  # User Did Something
        if event.type == pygame.QUIT:  # If The User Clicked Close
            carryOn = False  # Exit Loop

    # Moving Paddle When The User Uses Arrow Keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle.moveLeft(5)
    if keys[pygame.K_RIGHT]:
        paddle.moveRight(5)

    # Game Logic
    all_sprites_list.update()

    # Check If Ball Is Bouncing Against Any 4 Walls
    if ball.rect.x >= 790:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x <= 0:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y > 590:
        ball.velocity[1] = -ball.velocity[1]
        lives -= 1
        if lives == 0:
            # Display Game Over Message For 3 Seconds
            font = pygame.font.Font(None, 74)
            text = font.render("GAME OVER", 1, white)
            screen.blit(text, (250, 300))
            pygame.display.flip()
            pygame.time.wait(3000)

            # Stop The Game
            carryOn = False

    if ball.rect.y < 40:
        ball.velocity[1] = -ball.velocity[1]

    # Detect Collisions Between The Balls And The Paddles
    if pygame.sprite.collide_mask(ball, paddle):
        ball.rect.x -= ball.velocity[0]
        ball.rect.y -= ball.velocity[1]
        ball.bounce()

    # Check If There Is A Car Collision
    brick_collision_list = pygame.sprite.spritecollide(ball, all_bricks, False)
    for brick in brick_collision_list:
        ball.bounce()
        score += 1
        brick.kill()
        if len(all_bricks) == 0:
            # Display Level Complete Message For 3 Seconds
            font = pygame.font.Font(None, 74)
            text.font.render("LEVEL COMPLETE", 1, white)
            screen.blit(text, (200, 300))
            pygame.display.flip()
            pygame.time.wait(3000)

    # Drawing Code
    screen.fill(darkblue)  # Clears The Screen To Dark Blue
    # Game Window , Colour , Start Point , End Point , Width Of Line
    pygame.draw.line(screen, white, [0, 38], [800, 38], 2)

    # Display The Score And The Number Of Lives At The Top Of The Screen
    font = pygame.font.Font(None, 24)
    text = font.render("Score: " + str(score), 1, white)
    screen.blit(text, (20, 10))
    text = font.render("Lives: " + str(lives), 1, white)
    screen.blit(text, (650, 10))

    # Draws All Sprites In One Go
    all_sprites_list.draw(screen)

    # Updates Screen With What We've Drawn
    pygame.display.flip()

    # Limit To 60 Frames Per Second
    clock.tick(60)

# Once We Have Exited The Main Program Loop We Can Stop The Game Engine
pygame.quit()
