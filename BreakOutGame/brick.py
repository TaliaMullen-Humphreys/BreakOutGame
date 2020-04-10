import pygame

black = (0, 0, 0)

# This Class Represents A Brick. It Derives From The Sprite Class In Pygame


class Brick(pygame.sprite.Sprite):

    def __init__(self, colour, width, height):
        # Call The Parent Class (Sprite) Constructor
        super().__init__()

        # Pass In The Colour Of The Brick With Its X and Y Positions
        # Set Background Colour To Be Transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(black)
        self.image.set_colorkey(black)

        # Draw The Brick
        pygame.draw.rect(self.image, colour, [0, 0, width, height])

        # Fetch The Rectange Object That Has Dimensions Of The Image
        self.rect = self.image.get_rect()
