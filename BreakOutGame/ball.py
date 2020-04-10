#!/usr/bin/env python3

from random import randint
import pygame

black = (0, 0, 0)

# This Class Represents A Ball. It Derives From The Sprite Class In Pygame


class Ball(pygame.sprite.Sprite):

    def __init__(self, colour, width, height):
        # Calls The Parent Class (Sprite) Constructor
        super().__init__()

        # Pass In The Colour Of The Ball, Its Width & Its Height
        # Set Background Colour And Set It To Be Transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(black)
        self.image.set_colorkey(black)

        # Draw The Ball (A Rectangle)
        pygame.draw.rect(self.image, colour, [0, 0, width, height])

        self.velocity = [randint(4, 8), randint(-8, 8)]

        # Fetch The Rectange Object That Has Dimensions Of The Image
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8, 8)
