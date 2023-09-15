import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from rectangle import Rectangle
from game_stats import GameStats
from button import Button


class Target_arrow():
    """Класс для управления ресурсами и поведением игры."""
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Target Arrow')

        self.ship = Ship(self)

        self.bullets = pygame.sprite.Group()

        self.rectangle = Rectangle(self)

        self.stats = GameStats()

        self.play_button = Button(self, 'Play')


    def run_game(self):
        """Запуск основного цикла игры."""
        while True:
            self._check_events()

            if self.stats.game_active:
                
                self.ship.update()
                self._update_bullets()
                self._update_rectangle()

            self._update_screen()


    def _check_events(self):
        """Обрабатывает нажатия клавиш и события мыши."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
    

    def _check_keydown_events(self, event):
        """Реагирует на нажатия клавиш."""
        if event.key == pygame.K_q:
            sys.exit()
        if self.stats.game_active:
            if event.key == pygame.K_UP:
                self.settings.moving_up = True
            elif event.key == pygame.K_DOWN:
                self.settings.moving_down = True
            elif event.key == pygame.K_SPACE:
                self._fire_bullet()
    

    def _check_keyup_events(self, event):
        """Реагирует на отпускания клавиш."""
        if event.key == pygame.K_UP:
            self.settings.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.settings.moving_down = False


    def _check_play_button(self, mouse_pos):
        """Проверяет нажимает ли игрок на кнопку мышкой."""
        button_cliced = self.play_button.rect.collidepoint(mouse_pos)
        if button_cliced and not self.stats.game_active:
            self.settings.initialize_dynamic_settings()

            self.stats.reset_stats()
            self.stats.game_active = True

            self.bullets.empty()
            self.ship.center_ship()
            self.rectangle.right_up_rectangle()


    def _fire_bullet(self):
        """Создание нового снаряда и включение его в группу bullets."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
        
    
    def _update_bullets(self):
        """Обновляет позиции снярядов и удаляет вышедшие за пределы экрана."""
        self.bullets.update()
        if self.stats.bullets_left > 0:
            for bullet in self.bullets.copy():
                if bullet.rect.x > self.settings.screen_width:
                    self.bullets.remove(bullet)
                    self.stats.bullets_left -= 1
            
            self._check_bullet_rectangle_collisions()
        else:
            self.stats.game_active = False


    def _check_bullet_rectangle_collisions(self):
        """Проверяет коллизию снаряда и прямоугольника."""
        collisions = pygame.sprite.spritecollide(self.rectangle, self.bullets, True)
        if collisions:
            self.settings.increase_speed()

    def _update_rectangle(self):
        """Смена направления движения и отображение на экране прямоугольника."""
        self.rectangle.check_edges()
        self.rectangle.update()


    def _update_screen(self):
        """Обновляет изображения на экране и отображает новый экран."""
        self.screen.fill(self.settings.bg_color)

        self.ship.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        
        self.rectangle.draw_rectangle()

        if not self.stats.game_active:
            self.play_button.draw_button()

        pygame.display.flip()


if __name__ == '__main__':
    ta = Target_arrow()
    ta.run_game()