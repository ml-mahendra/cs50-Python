def main():
    inp = input("What time is it? ")
    convert(inp)

def convert(time):

    h,m = time.split(":")
    h = float(h)
    m = float(m)
    float_time = m/60 + h
    if (7 <= float_time <= 8):
        print("breakfast time")
    elif (12 <= float_time <= 13):
        print("lunch time")
    elif (18 <= float_time <= 19):
        print("dinner time")
    return float_time



if __name__ == "__main__":
    main()

