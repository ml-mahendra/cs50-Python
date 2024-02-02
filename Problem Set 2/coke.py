amt_due = 50
while amt_due > 0:
    print("Amount Due:", amt_due)
    amt = int(input("Insert Coin: "))
    if amt in [5,10,25]:
        amt_due -= amt

if amt_due < 0 or amt_due == 0:
    print("Change Owed:",abs(amt_due))
else:
    print("Amount Due:",abs(amt_due))


