from settings import Settings


class GameStats:
    """Отслеживание статистики для игры Target Arrow."""
    def __init__(self):
        self.settings = Settings()

        self.reset_stats()
        self.game_active = False


    def reset_stats(self):
        """Сбрасывает статистику."""
        self.bullets_left = self.settings.bullets_limit