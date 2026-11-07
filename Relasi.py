# Cartesian product
from itertools import product

A = {1, 2, 3}
B = {'a', 'b'}

cartesian = set(product(A, B))
print("A × B:", cartesian)

# Definisikan relasi sebagai himpunan pasangan
R = {(1, 'a'), (2, 'b'), (3, 'a')}
print("Relasi R:", R)

# Matriks relasi
A_list = sorted(A)
B_list = sorted(B)

print("\nMatriks Relasi R:")
print(f"{'':>4}", end="")
for b in B_list:
    print(f"{b:>4}", end="")
print()

for a in A_list:
    print(f"{a:>4}", end="")
    for b in B_list:
        print(f"{1 if (a, b) in R else 0:>4}", end="")
    print()