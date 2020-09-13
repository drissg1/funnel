from pydantic import BaseModel
from typing import List


class EmailPost(BaseModel):
    """The expected schema for a Post request"""
    email: str


class EmailPostResponse(BaseModel):
    """The response schema for the predict method"""
    top_topic: int
    topic_distribution: List[float] = []
    email_topics: List[str] = []
