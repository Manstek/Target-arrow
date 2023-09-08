import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Класс для управления снарядами выпущенными кораблём."""
    def __init__(self, ta_game):
        super().__init__()
        self.screen = ta_game.screen
        self.settings = ta_game.settings
        self.color = self.settings.bullet_color

        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.center = ta_game.ship.rect.center

        self.x = float(self.rect.x)
    

    def update(self):
        """Перемещает снаряд влево по экрану."""
        self.x += self.settings.bullet_speed
        self.rect.x = self.x
    

    def draw_bullet(self):
        """Вывод снаряда на экран."""
        pygame.draw.rect(self.screen, self.color, self.rect)
