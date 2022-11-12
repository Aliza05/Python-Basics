'''
def string_reverse(user_string):
    return user_string[::-1]

input_string = input("Enter a string: ")
print("Reversed String is: " + string_reverse(input_string))
'''

'''
def string_upper_lower_count(user_string):
    upper_case = 0
    lower_case = 0

    for characters in user_string:
        if characters.isupper():
            upper_case += 1
        elif characters.islower():
            lower_case += 1
        else:
            pass

    print("The user entered string is: " + user_string)
    print("The number of upper case letters in string are: " + str(upper_case))
    print("The number of lower case letters in string are: " + str(lower_case))

input_string = input("Enter the string: ")
string_upper_lower_count(input_string)
'''

def unique_list(user_list):
    new_unique_list = []

    for item in user_list:
        if item not in new_unique_list:
            new_unique_list.append(item)
    return new_unique_list

integer_list = [1, 2, 3, 3, 3, 3, 4, 5]
print(unique_list(integer_list))










