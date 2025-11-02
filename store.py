import os
import json
from time import sleep

# === Fungsi Tampilan Awal ===
def show_banner():
    banner_path = "assets/icon.txt"
    if os.path.exists(banner_path):
        with open(banner_path, "r") as icon:
            print(icon.read())
    else:
        print("=== Termux Package Store ===")
    print("-" * 50)

# === Fungsi Memuat Data Paket ===
def load_packages():
    data_path = "data/packages.json"
    if not os.path.exists(data_path):
        print("[!] File data/packages.json tidak ditemukan!")
        return {}
    with open(data_path, "r") as file:
        return json.load(file)

# === Fungsi Menampilkan Menu Kategori ===
def choose_category(packages):
    print("Pilih kategori:")
    for i, category in enumerate(packages, start=1):
        print(f"[{i}] {category}")
    try:
        choice = int(input("\nMasukkan nomor kategori: "))
        return list(packages.keys())[choice - 1]
    except (ValueError, IndexError):
        print("\n[!] Pilihan tidak valid!")
        return None

# === Fungsi Menampilkan Daftar Paket dan Install ===
def install_package(packages, category):
    print(f"\nPaket dalam kategori: {category}")
    for p in packages[category]:
        print(f" - {p}")

    install = input("\nKetik nama paket untuk install (atau kosongkan untuk batal): ").strip()
    if install:
        print(f"\n🔧 Menginstal paket: {install} ...\n")
        sleep(0.5)
        os.system(f"pkg install {install} -y")
    else:
        print("\n❌ Tidak ada paket yang dipilih.")

# === Fungsi Utama ===
def main():
    os.system("clear")
    show_banner()
    packages = load_packages()

    if not packages:
        return

    category = choose_category(packages)
    if category:
        install_package(packages, category)
    else:
        print("\nKeluar dari program.")

# === Jalankan ===
if __name__ == "__main__":
    main()
