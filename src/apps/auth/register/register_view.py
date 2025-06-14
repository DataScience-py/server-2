from fastapi import APIRouter

router = APIRouter(tags=["register"])

@router.post("/register/")
async def register():
    return {"message": "register"}