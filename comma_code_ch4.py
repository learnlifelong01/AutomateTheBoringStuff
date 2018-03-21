def comma_code(list_arg):
    for i in list_arg:
        if i == list_arg[len(list_arg)-1]:
            print("and ", end='')
        print(i, end='')

print("please enter a list with elements separated with commas and space")
user_list = input()
output = comma_code(user_list)
    
