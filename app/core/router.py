from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from os.path import dirname, join as path_join

from app.core.schemas import Task, Solution, Help, User
from app.core.services import calc


templates_directory = path_join(
    dirname(dirname(__file__)),
    "templates",
)


templates = Jinja2Templates(directory=templates_directory)

router = APIRouter()


@router.get("/calculator")
async def get_calculator_page(request: Request):
    return templates.TemplateResponse("calculator.html", {"request": request})


@router.post("/calc")
async def get_solution(task: Task) -> Solution:
    return Solution(
        task=task.task,
        solution=await calc(task.task),
    )


@router.get("/help")
async def get_help_text() -> Help:
    return Help(
        text="Push the buttons to get the result",
    )


@router.get("/me")
async def get_session_id(request: Request) -> User:
    return User(
        session=request.cookies.get('session'),
    )
