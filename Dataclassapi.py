from pydantic import BaseModel


class Attempts(BaseModel):
    is_negative: bool
    lesson_title: str
    lesson_url: str
    submitted_at: str

    class Config:
        populate_by_name = True


class Response(BaseModel):
    new_attempts: list[Attempts] | None = None
    status: str
    timestamp_to_request: float | None = None

    class Config:
        populate_by_name = True
