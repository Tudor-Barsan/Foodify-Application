class Food:
    def __init__(self):
        self._foods = {}

    def __str__(self):
        return f"foods = {self._foods}"

    def __repr__(self):
        return f"Food(foods = {self._foods})"

    def __len__(self):
        length = 0
        for category in self._foods:
            for food_item in self._foods[category]:
                length += 1
        return length

    def add_food(self, food):
        food_type = type(food).__name__

        if food_type not in self._foods:
            self._foods[f"{food_type}"] = []

        self._foods[f"{food_type}"].append(food)

    def remove_food(self, food_name):
        for category in self._foods:
            for food_item in self._foods[category]:
                if food_item.name() == food_name:
                    self._foods[category].remove(food_item)
        return self._foods

    def sort_foods(self):
        for category in self._foods:
            self._foods[category].sort()
        return self._foods

    def highest_rating(self):
        max_rating = 0
        highest_rated = None
        for category in self._foods:
            for food_item in self._foods[category]:
                rating = food_item.calories() + food_item.protein() + food_item.fat() + food_item.fiber() + food_item.carbs()
                if rating > max_rating:
                    highest_rated = food_item
                    max_rating = rating
        return highest_rated

    def lowest_rating(self):
        min_rating = 10 ** 20
        lowest_rated = None
        for category in self._foods:
            for food_item in self._foods[category]:
                rating = food_item.calories() + food_item.protein() + food_item.fat() + food_item.fiber() + food_item.carbs()
                if rating < min_rating:
                    lowest_rated = food_item
                    min_rating = rating
        return lowest_rated






