txt = input("Camel case: ")
for i in txt:
    if i.islower():
        print(i, end="")
    else:
        print("_"+i.lower(),end="")
print("")
