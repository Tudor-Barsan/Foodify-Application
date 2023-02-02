from Food_Groups import *
from Food import *
import csv


def create_instance(row):
    if row["Category"] == "Meat, Poultry" or row["Category"] == "Fish, Seafood":
        food_item = Meat(row["Food"], row["Measure"], row["Grams"], row["Calories"], row["Protein"], row["Fat"], row["Fiber"], row["Carbs"])

    elif row["Category"] == "Dairy products":
        food_item = Dairy(row["Food"], row["Measure"], row["Grams"], row["Calories"], row["Protein"], row["Fat"],row["Fiber"], row["Carbs"])

    elif row["Category"][:6] == "Breads":
        food_item = Grain(row["Food"], row["Measure"], row["Grams"], row["Calories"], row["Protein"], row["Fat"],row["Fiber"], row["Carbs"])

    elif row["Category"][:6] == "Fruits":
        food_item = Fruit(row["Food"], row["Measure"], row["Grams"], row["Calories"], row["Protein"], row["Fat"],row["Fiber"], row["Carbs"])

    elif row["Category"][:10] == "Vegetables":
        food_item = Vegetable(row["Food"], row["Measure"], row["Grams"], row["Calories"], row["Protein"], row["Fat"],row["Fiber"], row["Carbs"])

    elif row["Category"][:6] == "Drinks":
        food_item = Beverage(row["Food"], row["Measure"], row["Grams"], row["Calories"], row["Protein"], row["Fat"],row["Fiber"], row["Carbs"])

    else:
        food_item = Other(row["Food"], row["Measure"], row["Grams"], row["Calories"], row["Protein"], row["Fat"],row["Fiber"], row["Carbs"])

    return food_item


def read_and_store_foods():
    with open("Nutrition_Facts.csv", "r") as file_in:
        reader = csv.DictReader(file_in)
        foods = Food()
        for row in reader:
            item = create_instance(row)
            foods.add_food(item)

    return foods


# Main
foods_collection = read_and_store_foods()

