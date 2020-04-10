#!/usr/bin/env python3

import pygame

black = (0, 0, 0)

# This Class Represents A Paddle, It Derives From The "Sprite" Class In Pygame


class Paddle(pygame.sprite.Sprite):

    def __init__(self, colour, width, height):

        # Call The Parent Class (Sprite) Constructor
        super().__init__()

        # Pass In The Color Of The Car, Its (x,y) Position, Width & Height
        # Set The Background Colour To Transparent
        self.image = pygame.Surface((width, height))
        self.image.fill(black)
        self.image.set_colorkey(black)

        # Draw The Paddle (A Rectangle)
        pygame.draw.rect(self.image, colour, [0, 0, width, height])

        # Fetch The Rectangle Object That Has The Dimensions Of The Image
        self.rect = self.image.get_rect()

    def moveLeft(self, pixels):
        self.rect.x -= pixels
        # Check You Aren't Going Off The Screen
        if self.rect.x < 0:
            self.rect.x = 0

    def moveRight(self, pixels):
        self.rect.x += pixels
        # Check You Aren't Going Off The Screen
        if self.rect.x > 700:
            self.rect.x = 700
