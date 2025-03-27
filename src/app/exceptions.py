from fastapi import HTTPException


class InvalidAddress(HTTPException):
    def __init__(self, detail: str = None):
        super().__init__(status_code=422, detail=detail)


class WalletNotFound(InvalidAddress):
    pass


class TronNetworkError(HTTPException):
    def __init__(self, detail: str = None):
        super().__init__(status_code=503, detail=detail)
