from fastapi import APIRouter

router = APIRouter(tags=["login"])

@router.post("/login/")
async def login():
    return {"message": "Login"}
