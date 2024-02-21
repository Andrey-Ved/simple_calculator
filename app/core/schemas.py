from pydantic import BaseModel, ConfigDict


class User(BaseModel):
    session: str

    model_config = ConfigDict(from_attributes=True)


class Task(BaseModel):
    task: str

    model_config = ConfigDict(from_attributes=True)


class Solution(Task):
    solution: str


class Help(BaseModel):
    text: str
