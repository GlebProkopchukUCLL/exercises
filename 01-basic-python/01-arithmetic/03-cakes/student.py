# Write your code here
def cakes(eggs, butter, flour):
    eggs  = eggs // 5
    butter = butter // 250
    flour = flour // 250
    list_of_ingredients = [eggs, butter, flour]
    return min(list_of_ingredients)