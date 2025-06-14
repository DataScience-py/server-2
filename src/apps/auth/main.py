from fastapi import FastAPI

from login.login_view import router as login_router
from register.register_view import router as register_router

from config import settings


app = FastAPI(
    title=settings.APP_NAME,
    root_path="/auth"
)


@app.get("/")
async def root():
    return {"Service": "Work"}


app.include_router(login_router)
app.include_router(register_router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
