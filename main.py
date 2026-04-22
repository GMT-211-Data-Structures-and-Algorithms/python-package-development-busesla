from src.geo_package.parser import read_geometry_file

def run():
    print("--- Geomatik Paket Testi ---")
    try:
        data = read_geometry_file('point1.txt')
        for item in data:
            print(f"Başarıyla yüklendi: {item}")
    except Exception as e:
        print(f"Hata: {e}")

if __name__ == "__main__":
    run()