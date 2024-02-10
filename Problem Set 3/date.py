months = [ "January", "February", "March", "April", "May", "June","July", "August", "September", "October", "November", "December"]
while True:
    date = input("Date: ")
    try:
        month, day, year = date.split("/")
        month = int(month.replace(" ", ""))
        day = int(day)
        year = int(year.replace(" ", ""))
        if (int(month) >= 1 and int(month) <= 12) and (int(day) >= 1 and int(day) <= 31):
            if year >= 1000 and year <= 9999:
                print(year, f"{month:02}", f"{day:02}", sep="-")
                break
    except:
            try:
                if ","  in date:
                    month, day, year = date.split(" ")
                    day = int(day.replace(",", ""))
                    year = int(year)
                    if month in months and (day >= 1 and day <= 31):
                        if year >= 1000 and year <= 9999:
                            month = (months.index(month)+1)
                            print(year, f"{month:02}", f"{day:02}", sep="-")
                            break
                else:
                    raise SyntaxError
            except:
                pass


