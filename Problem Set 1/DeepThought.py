ans = input("What is the Answer to the Great Question of Life, the Universe, the Everything?")

if (ans.strip() == "42"): #strip() removes any leading or trailing whitespaces
    print("Yes")
elif (ans.lower() == "forty two" or ans.lower() == "forty-two"):
    print("Yes")
else:
    print("No")

