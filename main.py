from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm


app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.get("/")
def index():
    return {"mensagem" : "Olá mundo"}

@app.post("/token")
async def logar(data: OAuth2PasswordRequestForm = Depends()):
    return 