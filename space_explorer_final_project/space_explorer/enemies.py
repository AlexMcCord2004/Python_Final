import math
import pygame
from .settings import ENEMY_SIZE, WORLD_WIDTH, WORLD_HEIGHT
from .assets import load_image


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, image_name):
        super().__init__()
        self.image = load_image(image_name, (ENEMY_SIZE, ENEMY_SIZE))
        self.rect = self.image.get_rect(center=(x, y))

    def draw(self, screen, camera):
        screen.blit(self.image, camera.apply(self.rect))


class PatrolEnemy(Enemy):
    def __init__(self, x, y, distance=180, speed=2):
        super().__init__(x, y, "enemy_patrol.png")
        self.start_x = x
        self.distance = distance
        self.speed = speed
        self.direction = 1

    def update(self, player=None):
        self.rect.x += self.speed * self.direction

        if abs(self.rect.centerx - self.start_x) > self.distance:
            self.direction *= -1


class ChaserEnemy(Enemy):
    def __init__(self, x, y, speed=2):
        super().__init__(x, y, "enemy_chaser.png")
        self.speed = speed

    def update(self, player=None):
        if player is None:
            return

        dx = player.rect.centerx - self.rect.centerx
        dy = player.rect.centery - self.rect.centery
        distance = math.hypot(dx, dy)

        if distance > 0:
            self.rect.x += int(self.speed * dx / distance)
            self.rect.y += int(self.speed * dy / distance)


class BouncerEnemy(Enemy):
    def __init__(self, x, y, velocity_x=3, velocity_y=2):
        super().__init__(x, y, "enemy_bouncer.png")
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y

    def update(self, player=None):
        self.rect.x += self.velocity_x
        self.rect.y += self.velocity_y

        if self.rect.left <= 0 or self.rect.right >= WORLD_WIDTH:
            self.velocity_x *= -1
        if self.rect.top <= 0 or self.rect.bottom >= WORLD_HEIGHT:
            self.velocity_y *= -1
