import datetime


# when a user wants to add a new birthday
def add_birthday():
    # getting name
    first_name = input("What is the person's first name: ").capitalize()
    last_name = input("What is their last name: ").capitalize()
    name = first_name + " " + last_name

    # date of birth
    year = int(input(f'What year was {first_name} born? (YYYY): '))
    month = int(input(f'What month was {first_name} born? (MM): '))
    day = int(input(f'What day was {first_name} born? (DD): '))
    birthday1 = datetime.date(year, month, day)
    birthday = birthday1.strftime("%d %B %Y")  # for birthday in string format

    # adding name & birthday to text file
    with open("birthdays.txt", "a") as f:
        f.write("\n" + name + "," + " " + birthday)

    print(f"{name}'s birthday has successfully been added! :)")
    print()


# goes through birthdays file and returns a dictionary with names & date of births
def birthday_info():
    with open("birthdays.txt", 'r') as users:
        my_dict = {}
        for lines in users.readlines():
            lines2 = lines.strip()  # to remove the white spaces on the passwords
            lines2 = lines.split(',')  # to remove the comma next to the username
            my_dict[lines2[0]] = lines2[1]  # creating a dictionary with usernames and passwords
    return my_dict


# searches for a person & returns their date of birth
def search_name():
    info = birthday_info()  # calling dictionary of birthdays

    # getting name
    name_first = input("Enter the person's first name: ").capitalize()
    name_last = input("Enter the person's last name: ").capitalize()
    name = name_first + " " + name_last

    if name in info.keys():
        print(f"Showing info for {name_first}: ")
        print(f"{name} ---> {info[name]}")

    # name is not in dictionary
    else:
        print(f"Hmm... Awkward, we can't  seem to find information on {name} :( ")
        print("Please check the spelling or go ahead & add them to the database!")

    print()


# viewing all birthdays
def view_bdays():
    info = birthday_info()  # calling dictionary of birthdays

    print("Showing all birthdays: ")
    for names, date in info.items():
        print(f"{names} ---> {date}")

    print()


while True:
    option = int(input("""Hello, welcome to the birthday app. What would you like to do:
          (1). Add a new birthday
          (2). View all birthdays
          (3). Search for a birthday
          (4). Exit"""))

    # adding a new birthday
    if option == 1:
        add_birthday()

    # viewing all the birthdays in database
    elif option == 2:
        view_bdays()

    # searching for someone's birthday
    elif option == 3:
        search_name()

    # exit app
    elif option == 4:
        exit()
