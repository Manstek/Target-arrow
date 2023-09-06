import pygame


class Ship:
    """Класс для управления кораблём."""
    def __init__(self, ta_game):
        self.screen = ta_game.screen
        self.settings = ta_game.settings
        self.screen_rect = ta_game.screen.get_rect()
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.rect.left = self.screen_rect.left

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
    

    def update(self):
        """Обновляет позицию корабля с учётом флага."""
        pass


    def blitme(self):
        """Рисует корабль в текущей позиции."""
        self.screen.blit(self.image, self.rect)
