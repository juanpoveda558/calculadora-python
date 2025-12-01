from fastapi import FastAPI
from datetime import datetime
import pytz

app = FastAPI()

def get_local_time():
    # Definir zonas horarias
    bogota_tz = pytz.timezone('America/Bogota')
    
    return {
        "bogota": datetime.now(bogota_tz).isoformat()
    }

@app.get("/local-time")
def read_local_time():
    return get_local_time()