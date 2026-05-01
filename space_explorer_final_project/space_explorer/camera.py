import pygame
from .settings import SCREEN_WIDTH, SCREEN_HEIGHT, WORLD_WIDTH, WORLD_HEIGHT


class Camera:
    def __init__(self):
        self.offset = pygame.Vector2(0, 0)

    def update(self, target_rect):
        self.offset.x = target_rect.centerx - SCREEN_WIDTH // 2
        self.offset.y = target_rect.centery - SCREEN_HEIGHT // 2

        self.offset.x = max(0, min(self.offset.x, WORLD_WIDTH - SCREEN_WIDTH))
        self.offset.y = max(0, min(self.offset.y, WORLD_HEIGHT - SCREEN_HEIGHT))

    def apply(self, rect):
        return rect.move(-self.offset.x, -self.offset.y)
