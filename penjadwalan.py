def fpb(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def kpk(a, b):
    return abs(a * b) // fpb(a, b)

def jadwal_backup(interval_a, interval_b, durasi_pantau=120):
    """
    Menentukan jadwal backup bersama dua server.
    Menampilkan semua momen backup dalam rentang durasi pantau.
    """
    waktu_bersama = kpk(interval_a, interval_b)

    # Buat jadwal backup masing-masing server
    jadwal_a = set(range(0, durasi_pantau + 1, interval_a))
    jadwal_b = set(range(0, durasi_pantau + 1, interval_b))

    # Momen backup bersamaan
    bersamaan = sorted(jadwal_a & jadwal_b)

    print(f"Server A: backup setiap {interval_a} menit")
    print(f"Server B: backup setiap {interval_b} menit")
    print()
    print(f"FPB({interval_a}, {interval_b}) = {fpb(interval_a, interval_b)}")
    print(f"KPK({interval_a}, {interval_b}) = {waktu_bersama}")
    print()
    print(f"Pertama kali backup bersamaan: menit ke-{waktu_bersama}")
    print()
    print(f"Jadwal backup bersamaan dalam {durasi_pantau} menit ke depan:")
    print(bersamaan)

# Kasus utama: Server A = 12 menit, Server B = 18 menit
jadwal_backup(12, 18)

print()
print("=" * 50)
print()

# Kasus tambahan: Server C = 15 menit, Server D = 20 menit
jadwal_backup(15, 20)