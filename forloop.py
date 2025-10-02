apple = 10
totalprice = 0
totalpricewithdiscount = 0
pensionardiscount = 0.50
studentdiscount = 0.7
anvandare = input("ar du student eller pensionar?")
while anvandare != "student" or "pensionar":
    print("om du ar student eller pensionar skriv med alla sma bokstaver")
    anvandare = input("ar du student eller pensionar?")

hurmanga = int((input("hur manga apple vill du kopa")))

totalprice = hurmanga * apple


if anvandare == "student":
    totalpricewithdiscount = totalprice * studentdiscount
    print(f"du ska betala {totalpricewithdiscount} kr")
elif anvandare == "pensionar":
    totalpricewithdiscount = totalprice * pensionardiscount
    print(f"du ska betala {totalpricewithdiscount} kr")
else: print(totalprice)

