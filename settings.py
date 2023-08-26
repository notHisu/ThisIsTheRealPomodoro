# settings.py


class Settings:
    def __init__(self):
        self.session_length = 25 * 60
        self.break_length = 5 * 60

    def set_custom_lengths(self, session_length, break_length):
        self.session_length = session_length
        self.break_length = break_length


settings_instance = Settings()
