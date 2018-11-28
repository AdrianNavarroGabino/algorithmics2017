# Float numbers well formed
# Adrián Navarro Gabino

variable = input("Enter a float number: ")


if "." not in variable and "e" not in variable:
    print("It's NOT well formed")
else:
    try:
        variable2 = float(variable)
        print("{0} is well formed".format(variable))
    except:
        print("It's NOT well formed")
