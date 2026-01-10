from pydantic import BaseModel
from typing import List, Optional

#recursive self-referential model(eg: comment  then reply then the commnet on  reply and so on)

class Comment(BaseModel):
    id: int
    content: str
    reples: Optional[List["Comment"]] = None  # Self-referential field
    
Comment.model_rebuild()  # Required to resolve forward references
comment_data = Comment(
    id=1,
    content="This is the main comment",
    reples=[
        {
            "id": 2,
            "content": "This is a reply to the main comment",
            "reples": [
                {
                    "id": 3,
                    "content": "This is a reply to the first reply"
                }
            ]
        },
        {
            "id": 4,
            "content": "This is another reply to the main comment"
        }
    ]
)
    