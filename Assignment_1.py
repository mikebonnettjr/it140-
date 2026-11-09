name = input('What is your name? \n')
age = int(input('How old are you? \n'))
from datetime import date
current_yr = date.today().year
Birth_Year = current_yr - age
print(f'Hello {name}! You were born in {Birth_Year}.')