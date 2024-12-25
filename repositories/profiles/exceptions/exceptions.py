from ...base.exceptions.exceptions import BaseException

PROFILE_NOT_FOUNT_DETAIL: str = "Профиль не найден"

class ProfileNotFoundException(BaseException):
    status: int = 400
    detail: str = PROFILE_NOT_FOUNT_DETAIL

    def __init__(self):
        super().__init__(status=self.status, detail=self.detail)