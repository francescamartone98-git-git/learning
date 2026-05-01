
def calculate_age(birth_year, current_year):
    return current_year - birth_year

birth = int(input("what is your year of birth?"))
age = calculate_age (birth, 2026)


print(f"You are {age} years old!")
