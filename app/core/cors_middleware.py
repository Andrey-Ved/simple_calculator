from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost:8000",
    "http://127.0.0.1:8000",
]

allow_methods = [
    "GET",
    "POST",
    "OPTIONS",
    "DELETE",
    "PATCH",
    "PUT",
]

allow_headers = [
    "Content-Type",
    "Set-Cookie",
    "Access-Control-Allow-Headers",
    "Access-Control-Allow-Origin",
    "Authorization",
]


def add_cors_middleware(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=allow_methods,
        allow_headers=allow_headers,
    )
