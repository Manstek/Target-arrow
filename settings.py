class Settings:
    """Класс для хранения всех настроек игры."""
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        self.moving_up = False
        self.moving_down = False
        self.ship_speed = 1

        self.bullet_speed = 2
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        
