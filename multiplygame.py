import random

base = [1,2,3,4,5,6,7,8,9]


first_nr = base[random.randint(0, len(base)-1)]
second_nr = base[random.randint(0, len(base)-1)]

print(f"{first_nr} x {second_nr} = ")

should_repet = True
while (should_repet):
    score = int(input())

    if score == first_nr * second_nr:
        print("BARDZO DOBRZE")
        should_repet = False
            
    else:
        print("SPROBUJ JESZCZE RAZ")

