# Guess the id letter
# Adrián Navarro Gabino

letter = ['T','R','W','A','G','M','Y','F','P','D','X','B','N','J','Z','S','Q',
    'V','H','L','C','K','E']

dni = int(input("DNI: "))

a = dni % 23

print(letter[a])
