import sys
import pygame

from settings import Settings
from ship import Ship


class Target_arrow():
    """Класс для управления ресурсами и поведением игры."""
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Target Arrow')

        self.ship = Ship(self)


    def run_game(self):
        """Запуск основного цикла игры."""
        while True:
            self._check_events()

            self.ship.update()

            self._update_screen()
    

    def _check_events(self):
        """Обрабатывает нажатия клавиш и события мыши."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
    

    def _check_keydown_events(self, event):
        """Реагирует на нажатия клавиш."""
        if event.key == pygame.P_q:
            sys.exit()


    def _update_screen(self):
        """Обновляет изображения на экране и отображает новый экран."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        pygame.display.flip()


if __name__ == '__main__':
    ta = Target_arrow()
    ta.run_game()