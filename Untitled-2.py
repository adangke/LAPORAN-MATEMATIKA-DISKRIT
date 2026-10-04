# nama = "Sari"       # str
# umur = 19            # int
# ipk = 3.75           # float
# mahasiswa_aktif = True  # bool

# print(nama, umur, ipk, mahasiswa_aktif)

# P = True
# Q = False

# print(not P)
# print(P and Q)
# print(P or Q)
# print(P != Q)

# username_benar = True
# password_benar = True
# akun_aktif = True

# login = username_benar and password_benar and akun_aktif

# print("Status login:", login)

# nilai = [True, False]

# print("P     Q     P and Q   P or Q   not P")
# for p in nilai:
#     for q in nilai:
#         print(f"{p!s:<5} {q!s:<5} {p and q!s:<8} {p or q!s:<8} {not p!s}")


# def memenuhi_syarat(formulir, nilai, kehadiran, sanksi):
#     return formulir and nilai >= 60 and kehadiran >= 75 and not sanksi

# data = (True, 72, 80, False)
# print("Dapat mengikuti praktikum:", memenuhi_syarat(*data))

# from itertools import product

# A = {1, 2, 3, 4}
# B = {3, 4, 5, 6}
# U = set(range(1, 9))

# print("Union       :", A | B)
# print("Intersection:", A & B)
# print("Difference  :", A - B)
# print("Complement  :", U - A)
# print("Cardinality :", len(A))
# print("Subset?     :", A <= U)
# print("A x B       :", set(product(A, B)))


python = {"Ani", "Budi", "Citra"}
java = {"Budi", "Deni"}
sql = {"Ani", "Deni", "Eka"}
semua_mahasiswa = {"Ani", "Budi", "Citra", "Deni", "Eka", "Fajar"}

python_saja = python - (java | sql)
python_dan_java = python & java
minimal_satu = python | java | sql
tidak_menyukai_ketiganya = semua_mahasiswa - (python | java | sql)

print("Python saja:", python_saja)
print("Python dan Java:", python_dan_java)
print("Minimal satu teknologi:", minimal_satu)
print("Tidak menyukai ketiganya:", tidak_menyukai_ketiganya)

