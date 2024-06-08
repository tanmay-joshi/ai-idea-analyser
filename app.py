from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from main import research_and_analyse_idea

app = FastAPI()

class Idea(BaseModel):
    idea: str

items=[
    {"name": "item1", "id": 0},
    {"name": "item2", "id": 1},
    {"name": "item3", "id": 2},
]

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/idea")
async def analyse_idea(idea: Idea):
    result = research_and_analyse_idea(idea.idea)
    return {"analysis": result,
            "idea": idea.idea
            }
