from pydantic import BaseModel


class Attempts(BaseModel):
    is_negative: bool
    lesson_title: str
    lesson_url: str
    submitted_at: str

    class Config:
        allow_population_by_field_name = True


class Response(BaseModel):
    new_attempts: list[Attempts]

    class Config:
        allow_population_by_field_name = True