from fastapi import FastAPI
import uvicorn
from app.core.config import settings
from app.api.routes.health import router

app = FastAPI(title=settings.app_title, description=settings.description)
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run('app.main:app', reload=True)
