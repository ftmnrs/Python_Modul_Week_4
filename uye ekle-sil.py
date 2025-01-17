import json
import uuid


def new_func():
    FILE_PATH = "uyeler.json"
    return FILE_PATH

FILE_PATH = new_func()


def initialize_json_file():
    try:
        with open(FILE_PATH, 'r') as file:
            json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        with open(FILE_PATH, 'w') as file:
            json.dump([], file)


def uye_ekle():
    uye_id = str(uuid.uuid4())
    ad = input("Ad: ")
    soyad = input("Soyad: ")
    tel= input("telefon numarani gir:")
    dogumtarih=input("dogum tarihi (gg/aa/yy):")
    yeni_uye = {
        "id": uye_id,
        "ad": ad,
        "soyad": soyad,
        "tel" : tel,
        "dogumtar": dogumtarih
         }

    
    with open(FILE_PATH, 'r+') as file:
        try:
            uyeler = json.load(file)
        except json.JSONDecodeError:
            uyeler = []
        uyeler.append(yeni_uye)
        file.seek(0)
        json.dump(uyeler, file, indent=4)
    print(f"Yeni üye eklendi: {ad} {soyad}, ID:{uye_id[-6:]}")


def uye_sil():
    son_id_kisim = input("Silmek istediğiniz üyenin ID'sinin  girin: ")
    ad = input("Üyenin adı: ")
    soyad = input("Üyenin soyadı: ")
    
    with open(FILE_PATH, 'r+') as file:
        try:
            uyeler = json.load(file)
        except json.JSONDecodeError:
            uyeler = []

        
        yeni_uyeler = [
            uye for uye in uyeler
            if not (uye["id"].endswith(son_id_kisim) and uye["ad"].lower() == ad.lower() and uye["soyad"].lower() == soyad.lower())
        ]

        if len(uyeler) == len(yeni_uyeler):
            print(f"Üye bulunamadı: Ad: {ad}, Soyad: {soyad}, ID : {son_id_kisim}")
            return

        file.seek(0)
        file.truncate()
        json.dump(yeni_uyeler, file, indent=4)
    print(f"Üye silindi: Ad: {ad}, Soyad: {soyad}, ID : {son_id_kisim}")