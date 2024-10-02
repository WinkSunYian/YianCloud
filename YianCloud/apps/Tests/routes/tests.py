from fastapi import APIRouter


test = APIRouter()


@test.get(
    "/",
    summary="这是test的summary",
    description="这是test的description",
    deprecated=False,
)
async def test_api():
    return {"message": "Hello World"}


@test.get(
    "/a",
    summary="这是test的summary",
    description="这是test的description",
    deprecated=False,
)
async def test_api():
    return {"message": "Hello World"}


@test.get(
    "/user/{user_id}",
    summary="这是test的summary",
    description="这是test的description",
    deprecated=False,
)
async def test_api_b(user_id):
    return {"message": f"{user_id}"}
