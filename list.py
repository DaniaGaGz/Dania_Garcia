#Homogeneous list
integers = [1,2,3,4,5]

animals = ["dog","cat","goat"]

names = ["Sam","pelon", "DANIA"]

floats = [2.25, 34.54, 7.45]

#Heterogeneous list

numbers_animals = [1, "dog", 2, "giraffe", 3, "elephant"]

list_list = [[1,2,3],["catdog","rat","hamster"]]

#How to acces an element in a list 
print (numbers_animals [5])

print (numbers_animals[-1])

#ChatGPT list
words = [
    "apple", "banana", "cherry", "date", "elderberry",
    "fig", "grape", "honeydew", "kiwi", "lemon",
    "mango", "nectarine", "orange", "papaya", "quince",
    "raspberry", "strawberry", "tangerine", "ugli", "vanilla",
    "watermelon", "xigua", "yuzu", "zucchini", "avocado",
    "blueberry", "cantaloupe", "dragonfruit", "coconut", "jackfruit",
    "kumquat", "lime", "mulberry", "nectar", "passionfruit",
    "persimmon", "pomegranate", "starfruit", "tamarind", "cabbage",
    "carrot", "cauliflower", "celery", "corn", "cucumber",
    "eggplant", "garlic", "ginger", "lettuce", "mushroom",
    "onion", "pepper", "potato", "pumpkin", "spinach",
    "squash", "tomato", "zucchini", "basil", "chive",
    "cilantro", "dill", "oregano", "parsley", "rosemary",
    "sage", "thyme", "barley", "cornmeal", "flour",
    "millet", "oats", "quinoa", "rice", "sorghum",
    "wheat", "almond", "cashew", "hazelnut", "peanut",
    "pine", "pistachio", "walnut", "chocolate", "cinnamon",
    "clove", "cocoa", "vanilla", "sugar", "salt",
    "pepper", "paprika", "turmeric", "ginger", "mustard",
    "ketchup", "sauce", "oil", "vinegar", "soy",
    "fish", "chicken", "beef", "pork", "lamb",
    "turkey", "duck", "venison", "rabbit", "shellfish",
    "shrimp", "crab", "lobster", "clam", "mussel",
    "oyster", "scallop", "tofu", "tempeh", "seitan",
    "cheese", "yogurt", "milk", "cream", "butter",
    "egg", "bread", "bagel", "biscuit", "croissant",
    "muffin", "pancake", "waffle", "tortilla", "pizza",
    "pasta", "noodle", "risotto", "curry", "soup",
    "stew", "salad", "sandwich", "wrap", "burger",
    "taco", "quesadilla", "sushi", "dim_sum", "dumpling",
    "spring_roll", "kebab", "nugget", "fried", "grilled",
    "baked", "roasted", "steamed", "broiled", "barbecued",
    "smoked", "pickled", "fermented", "fresh", "dry",
    "sweet", "savory", "sour", "bitter", "umami",
    "tasty", "delicious", "spicy", "hot", "cold",
    "crunchy", "soft", "smooth", "creamy", "chewy",
    "sticky", "crispy", "flaky", "light", "dense",
    "thick", "thin", "juicy", "tender", "flavorful",
    "aromatic", "fragrant", "zesty", "refreshing", "nutty",
    "earthy", "rich", "bold", "subtle", "complex",
    "simple", "traditional", "modern", "fusion", "exotic"
]
print(words[-1])
print()

#list slicing
print(words[:])
print()

print(words [0:50])
print()

listy = [1,2,3,4,5,6]
print (listy [2:-1])
print()
#update a list
sciencelisty = ["art","chem","math"]
print(sciencelisty)
print()
sciencelisty[0]= "biology"
print(sciencelisty)
print()

sciencelisty[2] = "geology"
print(sciencelisty)
print()

integers1 = [1,2,3,4,5]
print(f"Original code: {integers1}")
print()

integers1[-1] = 6
print(f"Edited code: {integers1}")
print()

#remove
#quita el *valor* que quieras quitar, no el puesto
integers1.remove(6)
print(integers1)

#pop
#pop quita el ultimo valor de la lista (el indice donde está ese elemento)
integers1.pop(2)
print(integers1)

#Del
fruits = ["apple","pear","pineapple", "lemon", "tomato"]

del fruits[2]
print(fruits)

#Add to lists
nomen = ["Sam", "pelon","Dania"]

#append siempre añade al final
nomen.append("GILBERT")
print (nomen)