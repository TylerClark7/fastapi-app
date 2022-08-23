
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .database import engine
from .routers import post, user, auth, votes
from . config import settings
#uvicorn app.main:app --reload
##models.Base.metadata.create_all(bind=engine)  #Not Needed if you have alembic

app = FastAPI()  # app is conventional
 
origins = ["https://www.google.com"] #Use "https://www." the www is important

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(votes.router)

@app.get("/")
def root():
    return {"message": "welcome to my frikn api!!!"}

    # Hey ur aight, breakday. Play safe
