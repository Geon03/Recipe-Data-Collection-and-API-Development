import sqlite3
import json

conn = sqlite3.connect('DISHES.db')
cursor = conn.cursor()

# Drop table if exists to recreate without AUTOINCREMENT
cursor.execute('DROP TABLE IF EXISTS MENU')

cursor.execute('''
    CREATE TABLE MENU(
        id INTEGER PRIMARY KEY,
        continent VARCHAR(255),
        country_state VARCHAR(255),
        cuisine VARCHAR(255),
        title VARCHAR(255),
        url TEXT,
        rating FLOAT,
        prep_time INTEGER,
        cook_time INTEGER,
        total_time INTEGER,
        description TEXT,
        nutrients TEXT,
        serves VARCHAR(255)
    )
''')

# Insert data with specific ids
cursor.execute('''
    INSERT INTO MENU (id, continent, country_state, cuisine, title, url, rating, prep_time, cook_time, total_time, description, nutrients, serves)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
''', (1, "North America", "US", "Southern Recipes", "Sweet Potato Pie", "https://www.allrecipes.com/recipe/12142/sweet-potato-pie-i/",
      4.8, 15, 100, 115, "Shared from a Southern recipe, this homemade sweet potato pie is easy to make with boiled sweet potato. Try it, it may just be the best you've ever tasted!",
      json.dumps({"calories": "389 kcal", "carbohydrateContent": "48 g", "cholesterolContent": "78 mg", "fiberContent": "3 g", "proteinContent": "5 g", "saturatedFatContent": "10 g", "sodiumContent": "254 mg", "sugarContent": "28 g", "fatContent": "21 g", "unsaturatedFatContent": "0 g"}), "8"))

cursor.execute('''
    INSERT INTO MENU (id, continent, country_state, cuisine, title, url, rating, prep_time, cook_time, total_time, description, nutrients, serves)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
''', (2, "North America", "US", "Southern Recipes", "Fresh Southern Peach Cobbler", "https://www.allrecipes.com/recipe/51535/fresh-southern-peach-cobbler/",
      4.7, 20, 40, 60, "This peach cobbler recipe makes the perfect dessert. Sweet Georgia peaches are topped with homemade biscuits creating a bubbling Southern-style peach cobbler perfect for summer nights.",
      json.dumps({"calories": "562 kcal", "carbohydrateContent": "99 g", "cholesterolContent": "46 mg", "fiberContent": "1 g", "proteinContent": "4 g", "saturatedFatContent": "11 g", "sodiumContent": "400 mg", "sugarContent": "73 g", "fatContent": "18 g", "unsaturatedFatContent": "0 g"}), "4"))

cursor.execute('''
    INSERT INTO MENU (id, continent, country_state, cuisine, title, url, rating, prep_time, cook_time, total_time, description, nutrients, serves)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
''', (3, "North America", "US", "Southern Recipes", "Best Fried Green Tomatoes", "https://www.allrecipes.com/recipe/16760/best-fried-green-tomatoes/",
      4.7, 5, 15, 20, "Fried green tomatoes are a quick and easy way to use up green tomatoes and make a wonderful late summer treat.",
      json.dumps({"calories": "510 kcal", "carbohydrateContent": "56 g", "cholesterolContent": "95 mg", "fiberContent": "5 g", "proteinContent": "13 g", "saturatedFatContent": "4 g", "sodiumContent": "1136 mg", "sugarContent": "10 g", "fatContent": "27 g", "unsaturatedFatContent": "0 g"}), "4"))

cursor.execute('SELECT * FROM MENU')
rows = cursor.fetchall()
for row in rows:
    print(row)

conn.commit()
conn.close()
