from fastapi import FastAPI
from pydantic import BaseModel
from fatsecret import create_food_entry

app = FastAPI()

class FoodEntryData(BaseModel):
    food_id: int
    food_entry_name: str
    serving_id: int
    number_of_units: float
    meal: str

@app.post('/create_food_entry')
def create_food_entry_route(food_entry_data: FoodEntryData):
    food_entry_id = create_food_entry(food_entry_data.dict())
    return {'food_entry_id': food_entry_id}
