from repositories.base.exceptions.exceptions import BaseException


UNAUTH_USER_EXCEPTION_DETAIL: str = "Вы не авторизованы"

class UnAuthUserException(BaseException):
    status: int = 401
    detail: str = UNAUTH_USER_EXCEPTION_DETAIL

    def __init__(self):
        super().__init__(status=self.status, detail=self.detail)