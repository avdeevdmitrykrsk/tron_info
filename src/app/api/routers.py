from fastapi import APIRouter

from src.app.api.endpoints.wallet_info import router as wallet_info_router

main_router = APIRouter(prefix='/api')

main_router.include_router(
    wallet_info_router, prefix='/wallet_info', tags=['Wallet Info']
)
