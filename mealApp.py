import random

print("Welcome to Austin's Meal App!")
mealList = []
done = False

# load data from mealData.txt to mealList
inFile = open('mealData.txt')
for line in inFile:
    mealList.append(line.strip())
inFile.close()

def suggestMeal(mealList):
    "This suggests a random meal in the meal list to the console."
    index = random.randint(0, len(mealList) - 1)
    print("This app suggests " + mealList[index] + "\n")
    return

def addMeal(mealList):
    "This adds a user-selected meal to the meal list."
    newMeal = input("Please enter the name of the new meal.\n")
    mealList.append(newMeal)
    print("Added " + mealList[len(mealList) - 1] + " to the meal list.\n")
    return

def viewMeals(mealList):
    "This prints the current meals in the meal list to the console."
    for meal in mealList:
        print(meal)
    print('')
    return

def editMeals(mealList):
    "This allows user to remove or rename meals in list."
    badMeal = input("Please enter the name of the meal you want to edit.\n")
    if not badMeal in mealList:
        print("Could not find " + badMeal)
        return
    else:
        choice = input("Please enter the number of your choice: 1. Rename 2. Remove\n")
        choice = int(choice)
        if choice == 1:
            goodMeal = input("Please enter the new name for " + badMeal + "\n")
            for meal in mealList:
                if badMeal == meal:
                    mealList[mealList.index(meal)] = goodMeal
                    print("Renamed " + badMeal + " to " + meal + '.\n')
                    return
        elif choice == 2:
            for meal in mealList:
                if badMeal == meal:
                    mealList.remove(meal)
                    print("Removed " + badMeal + '.\n')
                    return
        else:
            print("Something went wrong.\n")
            return

def save(mealList):
    file = open('mealData.txt', 'w')
    for meal in mealList:
        file.write(meal + '\n')
    file.close()

while not done:
    selection = input('Please enter the number of your selection: 1. Get a Suggestion 2. Add a Meal 3. View Meals 4. Edit Meals 5. Save and Exit\n')
    selection = int(selection)
    if selection == 1:
        suggestMeal(mealList)
    elif selection == 2:
        addMeal(mealList)
    elif selection == 3:
        viewMeals(mealList)
    elif selection == 4:
        editMeals(mealList)
    elif selection == 5:
        save(mealList)
        done = True
    else:
        print("something went wrong")