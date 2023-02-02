class Foods:

    def __init__(self, food, measure, grams, calories, protein, fat, fiber, carbs):
        self._name = food
        self._quantity = measure
        self._weight = grams
        self._calories = self.convert_to_float(calories)
        self._protein = self.convert_to_float(protein)
        self._fat = self.convert_to_float(fat)
        self._fiber = self.convert_to_float(fiber)
        self._carbs = self.convert_to_float(carbs)

    def convert_to_float(self, value):
        # Extra process to deal with unusual values in the data
        if value.replace(".", "").isdigit() is not True:
            return 0
        return float(value)

    def __str__(self):
        return f"name = {self._name}, quantity = {self._quantity}, weight = {self._weight} grams, calories = {self._calories}, protein = {self._protein}, fat = {self._fat}, fiber = {self._fiber}, carbs = {self._carbs})"

    def __lt__(self, other):
        if self._calories < other.calories():
            return True
        return False

    def __gt__(self, other):
        if self._calories > other.calories():
            return True
        return False

    def __eq__(self, other):
        if self._calories == other.calories():
            return True
        return False

    def __add__(self, other):
        return self._calories + other.calories()

    def __sub__(self, other):
        return self._calories - other.calories()

    def name(self):
        return self._name

    def calories(self):
        return self._calories

    def protein(self):
        return self._protein

    def fat(self):
        return self._fat

    def fiber(self):
        return self._fiber

    def carbs(self):
        return self._carbs


class Meat(Foods):

    def __repr__(self):
        return f"Meat(name = {self._name}, quantity = {self._quantity}, weight = {self._weight}, calories = {self._calories}, protein = {self._protein}, fat = {self._fat}, fiber = {self._fiber}, carbs = {self._carbs})"

    def specialized_nutrient_amount(self):
        return f"{self._protein} gram(s) of protein"

    def specialized_nutrient_ratio(self):
        value_and_unit = self._quantity.split()
        value = value_and_unit[0]
        unit = value_and_unit[1]

        if value.isdigit() is True:
            ratio = self._protein / int(value)
            if unit == "oz.":
                return f"{self._name} has {ratio} gram(s) of protein per ounce"
            if unit == "cup" or unit == "cups":
                return f"{self._name} has {ratio} gram(s) of protein per cup"
        return f"Not calculable"


class Dairy(Foods):
    def __repr__(self):
        return f"Dairy(name = {self._name}, quantity = {self._quantity}, weight = {self._weight}, calories = {self._calories}, protein = {self._protein}, fat = {self._fat}, fiber = {self._fiber}, carbs = {self._carbs})"

    def specialized_nutrient_amount(self):
        return f"{self._fat} gram(s) of fat"

    def specialized_nutrient_ratio(self):
        value_and_unit = self._quantity.split()
        value = value_and_unit[0]
        unit = value_and_unit[1]

        if value.isdigit() is True:
            ratio = self._fat / int(value)
            if unit == "oz.":
                return f"{self._name} has {ratio} gram(s) of fat per ounce"
            if unit == "cup" or unit == "cups":
                return f"{self._name} has {ratio} gram(s) of fat per cup"
            if unit == "qt":
                return f"{self._name} has {ratio} gram(s) of fat per quart"
            if unit == "T.":
                return f"{self._name} has {ratio} gram(s) of fat per tablespoon"
        return f"Not calculable"


class Grain(Foods):
    def __repr__(self):
        return f"Grain(name = {self._name}, quantity = {self._quantity}, weight = {self._weight}, calories = {self._calories}, protein = {self._protein}, fat = {self._fat}, fiber = {self._fiber}, carbs = {self._carbs})"

    def specialized_nutrient_amount(self):
        return f"{self._carbs} gram(s) of carbohydrates"

    def specialized_nutrient_ratio(self):
        value_and_unit = self._quantity.split()
        value = value_and_unit[0]
        unit = value_and_unit[1]

        if value.isdigit() is True:
            ratio = self._carbs / int(value)
            if unit == "slice":
                return f"{self._name} has {ratio} gram(s) of carbohydrates per slice"
            if unit == "cup" or unit == "cups":
                return f"{self._name} has {ratio} gram(s) of carbohydrates per cup"
        return f"Not calculable"


class Fruit(Foods):
    def __repr__(self):
        return f"Fruit(name = {self._name}, quantity = {self._quantity}, weight = {self._weight}, calories = {self._calories}, protein = {self._protein}, fat = {self._fat}, fiber = {self._fiber}, carbs = {self._carbs})"

    def specialized_nutrient_amount(self):
        return f"{self._fiber} gram(s) of fiber"

    def specialized_nutrient_ratio(self):
        value_and_unit = self._quantity.split()
        value = value_and_unit[0]
        unit = value_and_unit[1]

        if value.isdigit() is True:
            ratio = self._fiber / int(value)
            if unit == "med." or unit == "med":
                return f"Each medium {self._name} has {ratio} gram(s) of fiber"
            if unit == "cup" or unit == "cups":
                return f"{self._name} has {ratio} gram(s) of fiber per cup"
        return f"Not calculable"


class Vegetable(Foods):
    def __repr__(self):
        return f"Vegetable(name = {self._name}, quantity = {self._quantity}, weight = {self._weight}, calories = {self._calories}, protein = {self._protein}, fat = {self._fat}, fiber = {self._fiber}, carbs = {self._carbs})"

    def specialized_nutrient_amount(self):
        return f"{self._fiber} gram(s) of fiber"

    def specialized_nutrient_ratio(self):
        value_and_unit = self._quantity.split()
        value = value_and_unit[0]
        unit = value_and_unit[1]

        if value.isdigit() is True:
            ratio = self._fiber / int(value)
            if unit == "med.":
                return f"Each medium {self._name} has {ratio} grams of fiber"
            if unit == "cup" or unit == "cups":
                return f"{self._name} has {ratio} grams of fiber per cup"
        return f"Not calculable"


class Beverage(Foods):
    def __repr__(self):
        return f"Beverage(name = {self._name}, quantity = {self._quantity}, weight = {self._weight}, calories = {self._calories}, protein = {self._protein}, fat = {self._fat}, fiber = {self._fiber}, carbs = {self._carbs})"

    def specialized_nutrient_amount(self):
        return f"{self._carbs} gram(s) of carbohydrates"

    def specialized_nutrient_ratio(self):
        value_and_unit = self._quantity.split()
        value = value_and_unit[0]
        unit = value_and_unit[1]

        if value.isdigit() is True:
            ratio = self._carbs / int(value)
            if unit == "oz.":
                return f"{self._name} has {ratio} gram(s) of carbohydrates per ounce"
            if unit == "cup" or unit == "cups":
                return f"{self._name} has {ratio} gram(s) of carbohydrates per cup"
        return f"Not calculable"


class Other(Foods):
    def __repr__(self):
        return f"Other(name = {self._name}, quantity = {self._quantity}, weight = {self._weight}, calories = {self._calories}, protein = {self._protein}, fat = {self._fat}, fiber = {self._fiber}, carbs = {self._carbs})"

    def specialized_nutrient_amount(self):
        return f"{self._calories} calories"

    def specialized_nutrient_ratio(self):
        value_and_unit = self._quantity.split()
        value = value_and_unit[0]
        unit = value_and_unit[1]

        if value.isdigit() is True:
            ratio = self._calories / int(value)
            if unit == "slice":
                return f"{self._name} has {ratio} calories per slice"
            if unit == "cup" or unit == "cups":
                return f"{self._name} has {ratio} calories per cup"
        return f"Not calculable"
