user_data = input('Ur name, last name, bYear separeted by space: ').split(' ')
curr_year = 2021
age = curr_year - int(user_data[2])
print(f"name: {user_data[0]}, last name: {user_data[1]}, age: {age}")