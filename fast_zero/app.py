from fastapi import FastAPI

app = FastAPI()

@app.get('/coelho')
def read_root():
    return 'Coelhinho peludo!'