import pickle


def display_recipe(recipe):
    print('Name: ', recipe['Name'])
    print('Cooking time in minutes: ', recipe['Cooking_Time'])
    print('Ingredients: ', ', '.join(recipe['Ingredients']))
    print('Difficulty: ', recipe['Difficulty'])


def search_ingredient(data):
    ingredients_list = data['all_ingredients']
    indexed_ingredients_list = list(enumerate(ingredients_list, 1))

    for ingredient in indexed_ingredients_list:
        print('No.', ingredient[0], ' - ', ingredient[1])

    try:
        chosen_num = int(
            input('Enter the corresponding number of your chosen ingredient:   '))
        index = chosen_num - 1
        ingredient_searched = ingredients_list[index]
        ingredient_searched = ingredient_searched.lower()
    except IndexError:
        print('The number you entered is not on the list.')
    except:
        print('An error occurred while finding your ingredient.')
    else:
        for recipe in data['recipes_list']:
            for recipe_ing in recipe['Ingredients']:
                if (recipe_ing == ingredient_searched):
                    print('\nThe following recipe includes the searched ingredient: ')
                    print('------------------------------------------------------')
                    display_recipe(recipe)


# Enter the file name
filename = input('Enter the filename where you\'ve stored your recipes:  ')
try:
    recipes_file = open(filename, 'rb')
    data = pickle.load(recipes_file)

except FileNotFoundError:
    print('File doesn\'t exist in the current directory')
    data = {'recipes_list': [], 'all_ingredients': []}

except:
    print('An unexpected error occurred')
    data = {'recipes_list': [], 'all_ingredients': []}

else:
    search_ingredient(data)

finally:
    recipes_file.close()