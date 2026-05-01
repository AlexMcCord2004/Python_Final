import pygame
from .settings import PLAYER_SPEED, PLAYER_MAX_HEALTH, PLAYER_SIZE, WORLD_WIDTH, WORLD_HEIGHT
from .assets import load_image


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = load_image("player.png", (PLAYER_SIZE, PLAYER_SIZE))
        self.rect = self.image.get_rect(center=(x, y))
        self.health = PLAYER_MAX_HEALTH
        self.invincible_timer = 0

    def update(self, keys):
        dx = 0
        dy = 0

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            dx -= PLAYER_SPEED
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            dx += PLAYER_SPEED
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            dy -= PLAYER_SPEED
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            dy += PLAYER_SPEED

        self.rect.x += dx
        self.rect.y += dy

        self.rect.left = max(0, self.rect.left)
        self.rect.right = min(WORLD_WIDTH, self.rect.right)
        self.rect.top = max(0, self.rect.top)
        self.rect.bottom = min(WORLD_HEIGHT, self.rect.bottom)

        if self.invincible_timer > 0:
            self.invincible_timer -= 1

    def hit(self):
        if self.invincible_timer == 0:
            self.health -= 1
            self.invincible_timer = 90

    def draw(self, screen, camera):
        draw_rect = camera.apply(self.rect)

        if self.invincible_timer > 0 and self.invincible_timer % 12 < 6:
            return

        screen.blit(self.image, draw_rect)
