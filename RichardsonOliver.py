# Name: Oliver Richardson
# Student Number: R00175244
# Class: Comp1A-X
import random


def load_data():  # This function reads the data.txt file and adds each item in there to the appropriate list
    connection = open("data.txt", "r")
    employee_id_list = []
    firstname_list = []
    surname_list = []
    salary_list = []
    email_list = []
    while True:
        # Since there is a certain order/pattern to how the data is written in the text file this while loop
        # can go through each line and add everything to the write list
        line = connection.readline().rstrip()
        if line == "":
            break
        employee_id_list.append(int(line))
        line = connection.readline().rstrip()
        firstname_list.append(line)
        line = connection.readline().rstrip()
        surname_list.append(line)
        line = connection.readline().rstrip()
        email_list.append(line)
        line = connection.readline().rstrip()
        salary_list.append(float(line))
    connection.close()
    return employee_id_list, firstname_list, surname_list, salary_list, email_list  # These lists are being returned to
    # the main()function


def show_all_employees(employee_id_list, firstname_list, surname_list, salary_list, email_list):
    i = 0
    while i < len(employee_id_list):
        # ^^^^^^^ this while loop prints out employee info the same way it is ordered in the text
        # file by using i as a position counter and then list[i] to pull a specific object from the list
        print(employee_id_list[i], firstname_list[i], surname_list[i],
              email_list[i], salary_list[i])
        i = i + 1


def employee_pos_in_list(employee_id_list):
    # this function is used when the employee needs to enter the id of an employee
    while True:
        usr_input = int(input("Enter the employee id"))
        id_validation = employee_id_list.count(usr_input)  # to check if the id is valid, .count is used
        if id_validation == 0:
            # if 0 instances are found of the id entered, ti i not valid and the user is asked for it again
            print("Enter a valid ID!")
            continue
        else:
            position = employee_id_list.index(usr_input)
            # if the id is found in the list its position is indexed
            # so it can be used to find the relevant info about the employee
            break
    return position


def show_employee(employee_id_list, firstname_list, surname_list, salary_list, email_list):
    list_position = employee_pos_in_list(employee_id_list)
    print("Employee ID:", employee_id_list[list_position], "\nFirst-Name:", firstname_list[list_position], "\nSurname:",
          surname_list[list_position], "\nEmail:", email_list[list_position], "\nSalary:", salary_list[list_position])


def change_salary(employee_id_list, salary_list):
    list_position = employee_pos_in_list(employee_id_list)
    # ^^^^^^ this a function that's further down in the program that
    # finds the position of an id entered by the user and uses that to find the other relevant
    # information of the employee
    while True:
        new_salary = float(input("Enter the new salary amount"))
        if new_salary < 0:
            print("Enter a valid salary")
            continue

        else:
            salary_list[list_position] = new_salary # This variable overwrites the old salary
            break
    print("The employees salary is now ", new_salary)


def id_generator(employee_id_list):
    new_id = '{}{}{}{}{}'.format(random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9),
                                 random.randint(0, 9))
    # This function uses random.randint for 5 single digit numbers between 1 and 9, this allows for the most amount of
    # variation possible in a 5 digit number
    while True:
        unique_id_checker = employee_id_list.count(new_id)
        # ^^^^^^ The unique id checker counts how many times the newly
        # generated id appears on the list
        if unique_id_checker > 0:  # If the id is found on the list already, it will generate a new id
            new_id = '{}{}{}{}{}'.format(random.randint(0, 9), random.randint(0, 9), random.randint(0, 9),
                                         random.randint(0, 9), random.randint(0, 9))
            continue  # This continue statement allows the id checker to run again and check if the new id is taken
        else:
            break  # if the id is found to be unique, the loop will break
# NOTE: while the new id is currently a string, it does get converted to an int when it is being added to the id list
    return new_id


def email_generator(firstname, surname, email_list):
    new_email = str(firstname).casefold() + "." + str(surname).casefold() + "@mycit.ie"
    i = 0
    while True:
        unique_email_checker = email_list.count(new_email)
        if unique_email_checker > 0:
            i = i + 1
            new_email = new_email = str(firstname).casefold() + "." + str(surname).casefold() + str(i) + "@mycit.ie"
            continue
        else:
            break
    # the email checker works mostly the same as the id checker except this time instead of generating an entirely new
    # email, it will add +1 on the end of the email until the new email is unique
    return new_email


def add_employee(employee_id_list, firstname_list, surname_list, salary_list, email_list):
    new_id = id_generator(employee_id_list)
    new_employee_firstname = input("Enter the new employee's first name:")
    new_employee_surname = input("Enter the new employee's surname:")
    new_employee_email = email_generator(new_employee_firstname, new_employee_surname, email_list)
    while True:
        new_employee_salary = float(input("Enter the employee's salary"))
        if new_employee_salary < 0:
            print("Enter a valid salary!")
            continue
        else:
            break
    employee_id_list.append(int(new_id))
    firstname_list.append(new_employee_firstname)
    surname_list.append(new_employee_surname)
    email_list.append(new_employee_email)
    salary_list.append(new_employee_salary)
    # ^^^^^^ the new information about the new employee added is added to the correct list
    print("Employee ID:", new_id, "\nFirst-Name:", new_employee_firstname, "\nSurname:",
          new_employee_surname, "\nEmail:", new_employee_email, "\nSalary:", new_employee_salary)


def remove_employee(employee_id_list, firstname_list, surname_list, salary_list, email_list):
    # ^^^^^ this function removes a user chosen employee from the data base
    list_position = employee_pos_in_list(employee_id_list)
    del firstname_list[list_position]
    del surname_list[list_position]
    del salary_list[list_position]
    del email_list[list_position]
    del employee_id_list[list_position]
    print("employee successfully removed from the data base")


def save_bonus_info(firstname, surname, salary):
    connection = open("bonus_info.txt", "w")  # This file will store all the bonus salary bonus info
    print("Enter the bonus info for the employees")
    i = 0
    n = 0
    bonus_list = []
    while i < len(salary):
        while True:
            bonus_input = float(input("Enter the percentage number for employee " + str(firstname[i]) + " " + str(surname[i])))
            if bonus_input < 0:
                print("Enter a valid percentage number!")
                continue

            else:
                break

        bonus_percent = bonus_input / 100  # the users input is divided by 100 to make it a decimal
        bonus_amount = salary[i] * bonus_percent  # then the salary specified by the counter i is multiplied by decimal
        f_bonus_amount = format(bonus_amount, ".2f")  # the end number is formatted to 2 decimal places
        bonus_list.append(f_bonus_amount)  # the bonus salary is added to a list
        i = i + 1
    print(bonus_list)
    while n < len(bonus_list):
        connection.write(str(bonus_list[n]) + "\n")
        n = n + 1
    connection.close()
    return bonus_list


def generate_report(employee_id_list, firstname_list, surname_list, salary_list):
    # ^^^^^^^ this function calculates the average salary of all employees and also the person who earns the most
    salary_total = sum(salary_list)  # first, the sum of all salaries is calculated
    no_items_salary_list = len(salary_list)  # then the number of salaries is got
    salary_avg = salary_total / no_items_salary_list  # next the sum of the salaries is divided by the no. of salaries
    f_salary_avg = format(salary_avg, ".2f")  # finally the result is formatted
    print("The average salary is:\n", f_salary_avg)
    max_salary = max(salary_list)
    no_of_ppl_with_max_salary = salary_list.count(max_salary)
    n = 0
    if no_of_ppl_with_max_salary == 1:
        while n < len(salary_list):
            if salary_list[n] == max_salary:
                print("The Highest Earner is:\nEmployee ID:", employee_id_list[n],
                      "\nFirst-Name:", firstname_list[n], "\nSurname:", surname_list[n], "\nSalary:", max_salary)

    elif no_of_ppl_with_max_salary > 1:
        print("There is ", no_of_ppl_with_max_salary, "with the highest salary, those people are:")
        while n < len(salary_list):
            if salary_list[n] == max_salary:
                print("One of the Highest Earners is:\nEmployee ID:", employee_id_list[n],
                      "\nFirst-Name:", firstname_list[n], "\nSurname:", surname_list[n], "\nSalary:", max_salary)
            n = n + 1


def save(employee_id_list, firstname_list, surname_list, salary_list, email_list,):
    # this function saves all the changes made to the lists that were created when initially reading data.txt
    # by writing to data.txt
    i = 0
    while True:
        print("Would you like to save your changes?")  # the user has to confirm they want their changes to be saved
        usr_input = input("Enter y for yes and n for no: ")
        if usr_input == "y":
            connection1 = open("data.txt", "w")
            while i < len(employee_id_list):
                connection1.write(str(employee_id_list[i]))
                connection1.write("\n" + str(firstname_list[i]))
                connection1.write("\n" + str(surname_list[i]))
                connection1.write("\n" + str(email_list[i]))
                connection1.write("\n" + str(salary_list[i]) + "\n")
                i = i + 1
            connection1.close()
            print("Changes saved successfully!")
            break
        elif usr_input == "n":
            print("Changes have been discarded!")
            break
        else:
            print("Please enter y or n to save or discard your changes!")
            continue


def show_menu(employee_id_list, firstname_list, surname_list, salary_list, email_list):
    # This function is where most of the functions are called based on the users input
    while True:
        print("========OPTIONS MENU========")
        print("1. show all employees\n2. show a specific employee\n3. change employee salary\n"
              "4. add an employee to the list\n5. remove an employee form the list\n6.Bonus info\n"
              "7.to generate a stat report\n8.exit")
        usr_input = int(input("Enter the corresponding number to select an option from the menu: "))
        if usr_input == 8:  # entering the number 8 will break the loop exiting the menu
            break
        elif usr_input == 1:
            show_all_employees(employee_id_list, firstname_list, surname_list, salary_list, email_list)
        elif usr_input == 2:
            show_employee(employee_id_list, firstname_list, surname_list, salary_list, email_list)
        elif usr_input == 3:
            change_salary(employee_id_list, salary_list)
        elif usr_input == 4:
            add_employee(employee_id_list, firstname_list, surname_list, salary_list, email_list)
        elif usr_input == 5:
            remove_employee(employee_id_list, firstname_list, surname_list, salary_list, email_list)
        elif usr_input == 6:
            save_bonus_info(firstname_list, surname_list, salary_list)
        elif usr_input == 7:
            generate_report(employee_id_list, firstname_list, surname_list, salary_list)
        else:
            print("Enter a valid option!")  # any number not used to select a number will cause the loop to continue
            continue


def main():  # all functions are housed within main
    employee_id_list, firstname_list, surname_list, salary_list, email_list = load_data()
    show_menu(employee_id_list, firstname_list, surname_list, salary_list, email_list)
    save(employee_id_list, firstname_list, surname_list, salary_list, email_list,)


main()
