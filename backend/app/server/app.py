from fastapi import FastAPI
from routes.movie_routes import rotas 

app = FastAPI()

app.include_router(rotas, tags=["Movie"], prefix="/movie")


