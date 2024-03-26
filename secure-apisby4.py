import pandas as pd
from fastapi import FastAPI, HTTPException, Header, Path

# Read data from csv file
df = pd.read_csv('players.csv')

# Make fastapi instance
app = FastAPI()

# Add API Key
API_KEY = "ini_password"

# Make homepage
@app.get('/')
def home():
    return{"message":"Wellcome to All Players API, it's a place to get players list"}

# Get all the data
@app.get('/players')
def getAllPlayers(api_key:str = Header(None)):
    print(api_key)
    if api_key is None or api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Bebas")
    else:
        return df.to_dict(orient='records')
    
# Get the player by the state
@app.get('/players/state/{state}')
def getPlayersByState(state:str, api_key:str = Header(None)):
    print(state)
    print(api_key)
    if api_key is None or api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Bebas")
    else:
        playerState = df[df['state'] == state]
        return playerState.to_dict(orient='records')
    
# Get the player by the year
@app.get('/players/year/{year}')
def getPlayersByYear(year:str, api_key:str = Header(None)):
    print(year)
    print(api_key)
    if api_key is None or api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Bebas")
    else:
        playerYear = df[df['year'] == year]
        return playerYear.to_dict(orient='records')
    
# Get the player by the position
@app.get('/players/position/{position}')
def getPlayersByPosition(position:str, api_key:str = Header(None)):
    print(position)
    print(api_key)
    if api_key is None or api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Bebas")
    else:
        playerPosition = df[df['position'] == position]
        return playerPosition.to_dict(orient='records')

# Get the player by the id
@app.get('/players/id/{id}')
def getPlayersById(id:int, api_key:str = Header(None)):
    print(id)
    print(api_key)
    if api_key is None or api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Bebas")
    else:
        playerId = df[df['id'] == id]
        return playerId.to_dict(orient='records')

# Delete players
@app.delete('/players/delete/{id}')
def delPlayer(id:int, api_key:str = Header(None)):
    """
    Delete player by id
    """
    print(id)
    print(api_key)
    if api_key is None or api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Bebas")
    else:
        if id not in df['id'].values:
            raise HTTPException(status_code=404, detail=f"Player with id {id} ga ada bang!")
        else:
            df.drop(df[df['id'] == id].index, inplace=True)
        return{"message":f"Player with id {id} has been deleted"}