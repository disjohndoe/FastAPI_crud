# Importing the FastApi class
from fastapi import FastAPI

app = FastAPI()

# Creating request enpoint


@app.get("/", tags=['root'])
async def root():
    return {"root": "Hello cruel world"}


# GET Method to Read Car List
@app.get("/cars", tags=["Cars"])
async def get_cars():
    return {"Data": cars}


# Post Method to Create Cars
@app.post("/cars/{id}", tags=["Cars"])
async def add_car(car: dict):
    cars.append(car)
    return {
        "data": f"A brand new {car['Brand']} has been added under the id: {car['id']}"
    }


# PUT  -- > Update Cars
@app.put("/cars/{id}", tags=["Cars"])
async def update_car(id: int, body: dict):
    for car in cars:
        if (int(car["id"])) == id:
            car["Brand"] = body["Brand"]
            return {
                "data": f"Car with the id {id} has been updated"
            }
    return {
        "data": f"The Car with the id {id} is not found!"
    }


# DELETE
@app.delete("/cars/{id}", tags=["Cars"])
async def delete_car(id: int):
    for car in cars:
        if int(car["id"]) == id:
            cars.remove(car)
            return{
                "data": f"Car with the id {id} has been deleted!"
            }
    return {
        "data": f"Car with the id {id} was not found!"
    }

# Cars List

cars = [
    {
        "id": "1",
        "Brand": "Mercedes"
    },
    {
        "id": "2",
        "Brand": "VW"
    }
]
