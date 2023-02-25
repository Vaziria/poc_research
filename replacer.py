import asyncio
from fastapi import FastAPI
from uvicorn import Config, Server
from pydantic import BaseModel



app = FastAPI()


class Pos(BaseModel):
    line_pos: int
    char_pos: int

class ReplacerData(BaseModel):
    pos: Pos
    first: int
    key: str
    hasil: str

fname = "assets_feb/545cf83630827e3e35f033cc866a33afd64eac39.backup.js"

with open(fname, "rb") as out:
    hasil = out.read()
    
    
lines = hasil.split(b"\n")



@app.get("/save")
def save_data():
    with open(fname, "wb") as out:
        out.write(hasil)
        
    return {}
    


@app.get("/replace")
def read_root(data: ReplacerData):
    line = lines[data.pos.line_pos]
    
    
    lines[data.pos.line_pos] = line
    return {}



if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    async def main():
        # check_login()
        
        config = Config(
            app=app,
            loop=loop,
            host="localhost",
            port=5003, 
            log_level="info"
        )
        server = Server(config)
        
        await server.serve()
        
    loop.run_until_complete(main())