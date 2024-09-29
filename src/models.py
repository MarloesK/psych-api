from pydantic import BaseModel


class Pineapple(BaseModel):
    episode: str
    description: str