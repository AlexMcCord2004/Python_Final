from .player import Player
from .enemies import PatrolEnemy, ChaserEnemy, BouncerEnemy
from .items import Star


class Level:
    def __init__(self, number):
        self.number = number
        self.player = Player(100, 100)
        self.enemies = []
        self.stars = []
        self.build_level()

    def build_level(self):
        if self.number == 1:
            self.stars = [
                Star(300, 250),
                Star(700, 300),
                Star(1200, 450),
                Star(1500, 850),
                Star(400, 950),
            ]

            self.enemies = [
                PatrolEnemy(500, 450, distance=160, speed=2),
                ChaserEnemy(950, 500, speed=2),
                BouncerEnemy(1300, 850, velocity_x=3, velocity_y=2),
            ]

        elif self.number == 2:
            self.stars = [
                Star(250, 250),
                Star(550, 500),
                Star(900, 300),
                Star(1250, 750),
                Star(1600, 1000),
                Star(300, 1050),
                Star(1450, 250),
            ]

            self.enemies = [
                PatrolEnemy(450, 350, distance=220, speed=3),
                PatrolEnemy(1200, 900, distance=250, speed=3),
                ChaserEnemy(850, 650, speed=3),
                ChaserEnemy(1500, 350, speed=2),
                BouncerEnemy(1000, 1000, velocity_x=4, velocity_y=3),
                BouncerEnemy(350, 750, velocity_x=3, velocity_y=4),
            ]
