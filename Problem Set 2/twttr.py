inp_str = input("Input: ")
v = ['a','e','i','o','u']
for letter in inp_str:
    if letter.lower() in v:
        inp_str= inp_str.replace(letter, "")
print(inp_str)
