

# Базовый родительский класс ошибки, которые отслеживается в main.py
# от него наследуются все ошибки
class BaseException(Exception):
    def __init__(self, status: int, detail: str):
        self.status = status
        self.detail = detail