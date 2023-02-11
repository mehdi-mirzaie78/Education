from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from core.config import settings
from apis.general_pages.route_homepage import general_pages_router
# import uvicorn


def include_router(app):
    app.include_router(general_pages_router)


def configure_static(app):
    app.mount("/static", StaticFiles(directory="static"), name="static")

def start_application():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    include_router(app)
    configure_static(app)
    return app


app = start_application()

# if __name__ == "__main__":
    # uvicorn.run(app, host="127.0.0.1", port=8000, reload=False)


# You can run this in the terminal if you want to:
# uvicorn main:app --reload











