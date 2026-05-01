import pygame

from .settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, WORLD_WIDTH, WORLD_HEIGHT
from .assets import ensure_assets, load_image
from .camera import Camera
from .levels import Level


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Space Explorer")
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 36)
        self.big_font = pygame.font.SysFont(None, 72)

        ensure_assets()
        self.background = load_image("background.png")

        self.camera = Camera()
        self.level_number = 1
        self.level = Level(self.level_number)
        self.score = 0
        self.state = "playing"

    def run(self):
        running = True

        while running:
            self.clock.tick(FPS)
            running = self.handle_events()

            if self.state == "playing":
                self.update()

            self.draw()

        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False

                if self.state == "level_complete" and event.key == pygame.K_SPACE:
                    self.next_level()

                if self.state in ("game_over", "victory") and event.key == pygame.K_r:
                    self.restart()

        return True

    def update(self):
        keys = pygame.key.get_pressed()

        self.level.player.update(keys)

        for enemy in self.level.enemies:
            enemy.update(self.level.player)

        self.camera.update(self.level.player.rect)

        collected_stars = []
        for star in self.level.stars:
            if self.level.player.rect.colliderect(star.rect):
                collected_stars.append(star)

        for star in collected_stars:
            self.level.stars.remove(star)
            self.score += 10

        for enemy in self.level.enemies:
            if self.level.player.rect.colliderect(enemy.rect):
                self.level.player.hit()

        if self.level.player.health <= 0:
            self.state = "game_over"

        if len(self.level.stars) == 0:
            if self.level_number == 1:
                self.state = "level_complete"
            else:
                self.state = "victory"

    def next_level(self):
        self.level_number += 1
        self.level = Level(self.level_number)
        self.camera = Camera()
        self.state = "playing"

    def restart(self):
        self.level_number = 1
        self.level = Level(self.level_number)
        self.camera = Camera()
        self.score = 0
        self.state = "playing"

    def draw_background(self):
        tile_width = self.background.get_width()
        tile_height = self.background.get_height()

        start_x = -int(self.camera.offset.x % tile_width)
        start_y = -int(self.camera.offset.y % tile_height)

        for x in range(start_x, SCREEN_WIDTH, tile_width):
            for y in range(start_y, SCREEN_HEIGHT, tile_height):
                self.screen.blit(self.background, (x, y))

    def draw_world_border(self):
        border_rect = pygame.Rect(0, 0, WORLD_WIDTH, WORLD_HEIGHT)
        visible_border = self.camera.apply(border_rect)
        pygame.draw.rect(self.screen, (80, 120, 170), visible_border, 4)

    def draw_hud(self):
        hud = f"Level: {self.level_number}   Score: {self.score}   Health: {self.level.player.health}"
        text = self.font.render(hud, True, (255, 255, 255))
        self.screen.blit(text, (20, 20))

    def draw_center_message(self, title, subtitle):
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 150))
        self.screen.blit(overlay, (0, 0))

        title_text = self.big_font.render(title, True, (255, 255, 255))
        subtitle_text = self.font.render(subtitle, True, (255, 255, 255))

        self.screen.blit(
            title_text,
            title_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 40))
        )
        self.screen.blit(
            subtitle_text,
            subtitle_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 35))
        )

    def draw(self):
        self.draw_background()
        self.draw_world_border()

        for star in self.level.stars:
            star.draw(self.screen, self.camera)

        for enemy in self.level.enemies:
            enemy.draw(self.screen, self.camera)

        self.level.player.draw(self.screen, self.camera)

        self.draw_hud()

        if self.state == "level_complete":
            self.draw_center_message("Level Complete!", "Press SPACE to begin Level 2")
        elif self.state == "game_over":
            self.draw_center_message("Game Over", "Press R to restart")
        elif self.state == "victory":
            self.draw_center_message("You Win!", "Press R to play again")

        pygame.display.flip()
