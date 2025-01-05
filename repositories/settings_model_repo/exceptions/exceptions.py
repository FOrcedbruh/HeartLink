from ...base.exceptions.exceptions import BaseException

SETTINGS_NOT_FOUND_DETAIL: str = "Данные о настройках не найдены"

class SettingsNotFoundException(BaseException):
    detail: str = SETTINGS_NOT_FOUND_DETAIL
    status: int = 404

    def __init__(self):
        super().__init__(detail=self.detail, status=self.status)