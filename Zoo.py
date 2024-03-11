txt1 = "Dog12, CAT3, LiOn7, DolphiN11, fish6"
txt2 = "PIG17, bear29, BiRd8" 
txt3 = "SNAKE39, donkey14"

temp_animal_list = (txt1 + ', ' + txt2 + ', ' + txt3).split(', ')
menu = None
animals_dict = {}
animals_str = ''
no_results = "We didn'nt find any animal matching your search\n---------------"

def adjust_data(animals_list):
    for animal in animals_list:
        for index in range(len(animal) - 1, 0, -1):
            if animal[index].isalpha():
                animal_index = animal[index + 1: len(animal)]
                animals_dict[animal_index] = animal[0: index + 1].capitalize()
                break

def print_animal(code:str):
    print('\nCode: ' + code + '\nName: ' + animals_dict[code])

def code_validation(code:str):
    while True:
            if code == '':
                print('No code provided, please enter a code:')
            elif not code.isnumeric():
                print('Only numbers allowed, please enter valid code:')
            else:
                break
            code = input('> ')
    return code

def name_validation(name:str):
    while True:
        if name == '':
            print('No name provided, please enter at least one letter')
        elif not name.isalpha():
            print('Only letters allowed, please enter valid name')
        else:
            break
        name = input('> ')
    return name

def yes_no_validatiob(message:str):
    choise = input(message + ' (Y/N)\n> ')
    while choise.lower() not in ['y', 'n']:
        choise = input('Only Y or N allowed, please try again\n> ')
    return choise.lower() == 'y'

def search_code():
    code = code_validation(input('Please enter an animal code:\n> '))
    if code not in animals_dict:
        print(no_results)
    else:
        print_animal(code)

def search_name():
    is_animal_found = False
    name  = name_validation(name = input('Please enter an animal name:\n> '))
    for animal_item in animals_dict.items():
        if name.lower() in animal_item[1].lower():
            print_animal(animal_item[0])
            is_animal_found = True
    if not is_animal_found:
        print(no_results)
            
def add_animal():
    code = code_validation(input('Please enter an animal code:\n> '))
    if code in animals_dict:
        print('Animal code already exist')
    else:
        name = name_validation(name = input('Please enter an animal name:\n> '))
        animals_dict[code] = name.capitalize()
        print('Animal successfuly added')

def remove_animal():
    code = code_validation(input('Please enter the animal code:\n> '))
    print()
    if code not in animals_dict:
        print("Animal code dose'nt exist")
    else:
        if(yes_no_validatiob("Are you sure you'de like remove " + code + " " + animals_dict[code] + " from Zoo Data?")):
            print_animal(code)
            del animals_dict[code]
            print('Animal successfuly deleted')
        else:
            print('Animal remove canceled')

def exit_program():
    if(yes_no_validatiob("Are you sure you want exit?")):
        print('Have a good day')
        exit()

adjust_data(temp_animal_list)
menu = {'1': search_code, '2': search_name, '3': add_animal, '4': remove_animal, '5': exit_program}

input_str = input('''Welcome to Zoo Data
Please enter the number of the action you'd like to do:
      
[1] Search for an animal by code
[2] Search for an animal by name
[3] Add new animal
[4] Delete an animal
[5] Exit

> ''')

while True:
    while input_str not in menu.keys():
        input_str = input("Unable searching, please enter valid option:\n> ")
    menu[input_str]()
    print()
    input_str = input('''Please choose your next action
> ''')