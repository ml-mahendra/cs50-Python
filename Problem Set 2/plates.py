def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    if len(s) >=2 and len(s) <= 6:
        return True
    elif s.isalnum():
            return True
    elif s[:2].isalpha():
                return True
    elif s[-1].isalpha() or s[-2].isalpha():
                    return False
    else:
          dec(s)


def dec(s):
    for c in s:
        x = ""
        if c.isdigit():
            index = index + c
            if x[0] == "0":
                return False
            else:
                return True
main()

