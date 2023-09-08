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
        self.bullets_limit = 3

        self.rectangle_speed = 0.1
        self.rectangle_width = 50
        self.rectangle_height = 100
        self.rectangle_color = (0, 0, 255)
        self.fleet_direction = 1 # 1 move down, -1 move up 

    
        
