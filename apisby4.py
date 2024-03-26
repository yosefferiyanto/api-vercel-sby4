from fastapi import FastAPI, HTTPException
import uvicorn

app = FastAPI()

students = {
    "fadilla": {
        "hobi": "membaca",
        "favFood": "bakso"
    },
    "kumala": {
        "hobi": "menyanyi",
        "favFood": "mie"
    },
    "putra": {
        "hobi": "play Valorant",
        "favFood": "nasi"
    }
}

#Base url (homepage)
@app.get('/')       #'/' setara dengan base url
def home():
    return{"message" : "Hello World! & mamah juga"}

#Show other message
@app.get('/sby4message')
def msg():
    return{"message" : "Hactiv8 SBY-4 adalah murid-murid teladan dan cakep-cakep"}

#Show all data
@app.get('/sby4')   #'/sby4' berarti dengan end-point baru
def studentsList():
    return students #memanggil variable data

#Show one data with key
@app.get('/{name}')
def getName(name:str):
    if name in students.keys():
        return students[name]
    else:
        raise HTTPException(status_code=404, detail="Students not found! Try one of this (fadilla, kumala, putra)")
    
#Add students data
@app.post('/add_data')
def addData(studentsData:dict):
    print('Students Data: ', studentsData)
    studentsName = studentsData['name']
    studentsHobi = studentsData['hobi']
    studentsFavFood = studentsData['favFood']
    #Add it to our data variable
    students[studentsName] = {
        "hobi": studentsHobi,
        "favFood": studentsFavFood
    }
    #Add a message
    return{"message":"Students data have been successfully added"}