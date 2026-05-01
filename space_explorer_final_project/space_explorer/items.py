import pygame
from .settings import STAR_SIZE
from .assets import load_image


class Star(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = load_image("star.png", (STAR_SIZE, STAR_SIZE))
        self.rect = self.image.get_rect(center=(x, y))

    def draw(self, screen, camera):
        screen.blit(self.image, camera.apply(self.rect))
