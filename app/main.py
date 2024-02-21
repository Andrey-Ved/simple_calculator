import uvicorn

from datetime import datetime
from fastapi import FastAPI, Request, Response
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from os.path import dirname, join as path_join

from app.core.router import router
from app.core.cors_middleware import add_cors_middleware


app = FastAPI()


@app.middleware("http")
async def marking_middleware(request: Request, call_next):
    response = await call_next(request)

    if not request.cookies.get('session'):
        response.set_cookie(
            key='session',
            value=str(round(datetime.now().timestamp() * 10**5) % 10**15),
            httponly=True,
        )

    return response


static_files_app = StaticFiles(
    directory=path_join(
        dirname(__file__),
        "static",
    )
)

app.mount("/static", static_files_app, name="static")

app.include_router(router)
add_cors_middleware(app)


@app.get("/", tags=["Pages"])
async def root(request: Request) -> Response:  # noqa
    return RedirectResponse("/calculator", status_code=301)


def main():
    print(
        f'\n'
        f'INFO:     Documentation is available at '
        f'http://127.0.0.1:8000/docs'
        f'\n'
    )

    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000
    )


if __name__ == '__main__':
    main()
