import pygame


class Ship:
    """Класс для управления кораблём."""
    def __init__(self, ta_game):
        self.screen = ta_game.screen
        self.settings = ta_game.settings
        self.screen_rect = ta_game.screen.get_rect()
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.rect.centery = self.screen_rect.centery

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
    

    def update(self):
        """Обновляет позицию корабля с учётом флага."""
        if self.settings.moving_up and self.rect.top >= 0:
            self.rect.y -= self.settings.ship_speed
        if self.settings.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += self.settings.ship_speed


    def blitme(self):
        """Рисует корабль в текущей позиции."""
        self.screen.blit(self.image, self.rect)
    

    def center_ship(self):
        """Распологает корабль по центру."""
        self.rect.centery = self.screen_rect.centery
        self.y = float(self.rect.y)
