year = 0
birds = 80000

while birds > 8000: 
    print(f"currently this is year {year} and the number of birds is {birds}")
    birds = birds * 0.5
    print(f"at the end of year {year}, the number of birds decreses to {birds}")
    year += 1

    #break statement 

i = 0
while True:
        print(i)
        i += 1
        if i>5:
            break