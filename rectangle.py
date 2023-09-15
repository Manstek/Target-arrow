import pygame


class Rectangle:
    """Класс для управления прямоугольником."""
    def __init__(self, ta_game):
        self.screen = ta_game.screen
        self.settings = ta_game.settings
        self.screen_rect = self.screen.get_rect()
        self.color = self.settings.rectangle_color
        self.width = self.settings.rectangle_width
        self.height = self.settings.rectangle_height

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.right = self.screen_rect.right

        self.y = float(self.rect.y)
    

    def update(self):
        """Непрерывное движение корабля вниз/вверх."""
        self.y += (self.settings.rectangle_speed * self.settings.fleet_direction)
        self.rect.y = self.y


    def check_edges(self):
        """Смена направления прямоугольника, если он находится максималь сверху или снизу."""
        if self.rect.bottom == self.screen_rect.bottom:
            self.settings.fleet_direction = -1
        elif self.rect.y == self.screen_rect.top:
            self.settings.fleet_direction = 1


    def draw_rectangle(self):
        """Функция для вывода прямоугольника на экран."""
        pygame.draw.rect(self.screen, self.color, self.rect)
    

    def right_up_rectangle(self):
        """Расcпологает прямоугольник в правом верхнем углу."""
        self.rect.topright = self.screen_rect.topright

