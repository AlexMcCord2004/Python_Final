from pathlib import Path
import pygame


ASSET_DIR = Path(__file__).parent / "assets"


def create_surface(size, color, shape="rect"):
    surface = pygame.Surface((size, size), pygame.SRCALPHA)

    if shape == "ship":
        points = [(size // 2, 4), (size - 6, size - 8), (size // 2, size - 18), (6, size - 8)]
        pygame.draw.polygon(surface, color, points)
        pygame.draw.circle(surface, (220, 240, 255), (size // 2, size // 2), size // 7)
    elif shape == "star":
        center = size // 2
        points = [
            (center, 3), (center + 7, center - 7), (size - 3, center - 6),
            (center + 10, center + 3), (center + 14, size - 3),
            (center, center + 9), (center - 14, size - 3),
            (center - 10, center + 3), (3, center - 6),
            (center - 7, center - 7)
        ]
        pygame.draw.polygon(surface, color, points)
    elif shape == "enemy":
        pygame.draw.circle(surface, color, (size // 2, size // 2), size // 2 - 4)
        pygame.draw.circle(surface, (30, 30, 30), (size // 3, size // 3), 5)
        pygame.draw.circle(surface, (30, 30, 30), (2 * size // 3, size // 3), 5)
    elif shape == "background":
        surface = pygame.Surface((size, size))
        surface.fill((8, 12, 30))
        for x in range(8, size, 45):
            for y in range(10, size, 50):
                pygame.draw.circle(surface, (230, 230, 255), (x, y), 1)
    else:
        pygame.draw.rect(surface, color, surface.get_rect(), border_radius=8)

    return surface


def ensure_assets():
    ASSET_DIR.mkdir(exist_ok=True)

    assets = {
        "player.png": create_surface(64, (80, 180, 255), "ship"),
        "star.png": create_surface(40, (255, 220, 60), "star"),
        "enemy_patrol.png": create_surface(54, (255, 90, 90), "enemy"),
        "enemy_chaser.png": create_surface(54, (180, 90, 255), "enemy"),
        "enemy_bouncer.png": create_surface(54, (255, 150, 40), "enemy"),
        "background.png": create_surface(256, (8, 12, 30), "background"),
    }

    for filename, surface in assets.items():
        path = ASSET_DIR / filename
        if not path.exists():
            pygame.image.save(surface, path)


def load_image(filename, size=None):
    path = ASSET_DIR / filename
    image = pygame.image.load(path).convert_alpha()
    if size is not None:
        image = pygame.transform.smoothscale(image, size)
    return image
