from fastapi import APIRouter
from .tests import test as tests_router

router = APIRouter()

router.include_router(tests_router, prefix="/tests")


@router.get("/")
async def root():
    return {"message": "Welcome to YianCloud API"}
