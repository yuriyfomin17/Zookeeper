quantity_of_atoms = int(input())
final_quantity = int(input())

count = 0

while final_quantity <= quantity_of_atoms:
    quantity_of_atoms /= 2
    count = count + 1

print(12 * count)
