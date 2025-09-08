from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3
import json
from typing import List, Optional

app = FastAPI()

DATABASE = "DISHES.db"

class Recipe(BaseModel):
    id: int
    continent: Optional[str]
    country_state: Optional[str]
    cuisine: Optional[str]
    title: Optional[str]
    url: Optional[str]
    rating: Optional[float]
    prep_time: Optional[int]
    cook_time: Optional[int]
    total_time: Optional[int]
    description: Optional[str]
    nutrients: Optional[dict]
    serves: Optional[str]

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.get("/recipes", response_model=List[Recipe])
def read_recipes():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM MENU")
    rows = cursor.fetchall()
    conn.close()

    recipes = []
    for row in rows:
        nutrients = {}
        if row["nutrients"]:
            try:
                nutrients = json.loads(row["nutrients"])
            except json.JSONDecodeError:
                nutrients = {}
        recipe = Recipe(
            id=row["id"],
            continent=row["continent"],
            country_state=row["country_state"],
            cuisine=row["cuisine"],
            title=row["title"],
            url=row["url"],
            rating=row["rating"],
            prep_time=row["prep_time"],
            cook_time=row["cook_time"],
            total_time=row["total_time"],
            description=row["description"],
            nutrients=nutrients,
            serves=row["serves"]
        )
        recipes.append(recipe)
    return recipes

@app.get("/recipes/{recipe_id}", response_model=Recipe)
def read_recipe(recipe_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM MENU WHERE id = ?", (recipe_id,))
    row = cursor.fetchone()
    conn.close()
    if row is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    nutrients = {}
    if row["nutrients"]:
        try:
            nutrients = json.loads(row["nutrients"])
        except json.JSONDecodeError:
            nutrients = {}
    recipe = Recipe(
        id=row["id"],
        continent=row["continent"],
        country_state=row["country_state"],
        cuisine=row["cuisine"],
        title=row["title"],
        url=row["url"],
        rating=row["rating"],
        prep_time=row["prep_time"],
        cook_time=row["cook_time"],
        total_time=row["total_time"],
        description=row["description"],
        nutrients=nutrients,
        serves=row["serves"]
    )
    return recipe
