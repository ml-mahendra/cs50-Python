while True:
    try:
        x,y = input("Fraction:").split("/")
        if int(x) > int(y):
            continue
        fuel = int(x) / int(y) * 100
        break
    except (ValueError, ZeroDivisionError):
        print("Divide by zero") # if use pass, ot prompts the user input without printing any

fuel = round((int(x) / int(y)) * 100)
if fuel >= 99:
    print("F")
elif fuel <= 1:
    print("E")
else:
    print(round(fuel),'%', sep='')
