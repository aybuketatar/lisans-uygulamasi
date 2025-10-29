from rommenu import MenuSistemi
kayitli_eserler = {}

def ustveri(lisansAdi):
    print("\nEklemek İstediğin Eserin Bilgileri: ")
    
    eserAdi = input("Eser Adı: ") 

    if eserAdi in kayitli_eserler:
        print(f"\n HATA: '{eserAdi}' adında bir eser zaten kayıtlı.")
        return 
    
    YazarAdi = input("YazarAdi: ")
    eserURL = input("Eser URL'si: ")
    eserTarihi = input("Yayınlanma Tarihi (YYYY): ") 

    lisans_metni = "" 
    if lisansAdi == "CC0 1.0 (Kamu Malı)":
        lisans_metni = f"{eserAdi} by {YazarAdi} is marked CC0 1.0"
    else:
        lisans_metni = f"{eserAdi} © {eserTarihi} by {YazarAdi} is licensed under {lisansAdi}"

    kayitli_eserler[eserAdi] = {
        "yazarı": YazarAdi,
        "tarih": eserTarihi,
        "eser_url": eserURL,
        "lisans": lisansAdi,
        "lisans_metni": lisans_metni
    }
    
    print("\nESER KAYDEDİLDİ")
    print(lisans_metni)
    print("---------------------------------")


def zeropd():
    print("\nCC0 Sıfır (Zero): Kamu Malı tahsisi olarak kullanılır. Kullanımda olan son sürümü 1.0’dır. Resmi olarak Türkçe çevirisi yayınlanmıştır. Bu lisans kapsamında telif hakkı sınırlaması yoktur, kaynak atıf vermeden ticari amaç da dahil olmak üzere kopyalanabilir, düzenlenebilir, dağıtılabilir ve yeniden kullanılabilir.")
    ustveri("CC0 1.0 (Kamu Malı)")

def ccby():
    print("\n")
    print("CC BY Atıf (Attribution): CC’nin en özgür lisansıdır. Kullanımda olan son sürümü 4.0’dır. Uluslararası olarak kullanılabilir. Resmi olarak Türkçe çevirisi yayınlanmıştır. Kaynak, atıf vermek kaydıyla ticari amaç da dahil olmak üzere kopyalanabilir, düzenlenebilir, dağıtılabilir ve yeniden kullanılabilir.")
    ustveri("CC BY 4.0")

def ccbysa():
    print("\n") # Buraya bir \n ekledim, daha iyi görünüyor
    print("CC BY-SA Atıf-AynıLisanslaPaylaş (Attribution-ShareAlike): Kullanımda olan son sürümü 4.0’dır. Uluslararası olarak kullanılabilir. Resmi olarak Türkçe çevirisi yayınlanmıştır. Kaynak, atıf vermek ve aynı lisansı devam ettirmek kaydıyla ticari amaç da dahil olmak üzere kopyalanabilir, düzenlenebilir, dağıtılabilir ve yeniden kullanılabilir")
    ustveri("CC BY-SA 4.0")

def ccbynd():
    print("\n")
    print("CC BY-ND Atıf-Türetilemez (Attribution-NonDerivative): Kullanımda olan son sürümü 4.0’dır. Uluslararası olarak kullanılabilir. Resmi olarak Türkçe çevirisi yayınlanmıştır. Kaynak, atıf vermek kaydıyla ticari amaç da dahil olmak üzere kopyalanabilir, dağıtılabilir ve yeniden kullanılabilir ancak üzerinde hiçbir değişiklik yapılamaz.")
    ustveri("CC BY-ND 4.0")

def ccbync():
    print("\n")
    print("CC BY-NC Atıf-GayriTicari (Attribution-NonCommercial): Kullanımda olan son sürümü 4.0’dır. Uluslararası olarak kullanılabilir. Resmi olarak Türkçe çevirisi yayınlanmıştır. Kaynak, atıf vermek kaydıyla ticari amaç haricinde kopyalanabilir, düzenlenebilir, dağıtılabilir ve yeniden kullanılabilir.")
    ustveri("CC BY-NC 4.0")

def ccbyncsa():
    print("\n")
    print("CC BY-NC-SA Atıf-GayriTicari-AynıLisanslaPaylaş (Attribution-NonCommercial-ShareAlike): Kullanımda olan son sürümü 4.0’dır. Uluslararası olarak kullanılabilir. Resmi olarak Türkçe çevirisi yayınlanmıştır. Kaynak, atıf vermek ve aynı lisansı devam ettirmek kaydıyla ticari amaç haricinde kopyalanabilir, düzenlenebilir, dağıtılabilir ve yeniden kullanılabilir.")
    ustveri("CC BY-NC-SA 4.0")

def ccbyncnd():
    print("\n")
    print("CC BY-NC-ND Atıf-GayriTicari-Türetilemez (Attribution-NonCommercial-NonDerivative): CC’nin en az özgürlük sağlayan lisansıdır. Kullanımda olan son sürümü 4.0’dır. Uluslararası olarak kullanılabilir. Resmi olarak Türkçe çevirisi yayınlanmıştır. Kaynak, atıf vermek kaydıyla ticari amaç haricinde kopyalanabilir, dağıtılabilir ve yeniden kullanılabilir, ancak üzerinde hiçbir değişiklik yapılamaz.")
    ustveri("CC BY-NC-ND 4.0")


def eser_ara():
    print("\n--- Eser Arama ---")
    aranan_ad = input("Lisansını görmek istediğiniz eserin adını girin: ")
    eser_bilgisi = kayitli_eserler.get(aranan_ad) 
    if eser_bilgisi:
        print(f"\n--- '{aranan_ad}' Eserinin Bilgileri ---")
        print(f"Yazarı: {eser_bilgisi['yazarı']}")
        print(f"Tarihi: {eser_bilgisi['tarih']}")
        print(f"Lisans Türü: {eser_bilgisi['lisans']}")
        print(f"Oluşturulan Lisans Metni: {eser_bilgisi['lisans_metni']}")
    else:
        print(f"\n HATA !: '{aranan_ad}' adında bir eser kayıtlarda bulunamadı.")

def tum_eserleri_goster():
    print("\n Kayıtlı Tüm Eserler")
    if not kayitli_eserler:
        print("Henüz kayıtlı hiçbir eser yok.")
        return
    i = 1
    for eser_adi, bilgiler in kayitli_eserler.items():
        print(f"{i}. {eser_adi} (Lisans: {bilgiler['lisans']})")
        i += 1


menu = MenuSistemi()
menu.karsilama("Lisans Uzantısı Oluşturma Uygulaması")
menu.opsiyon_ekle("Yeni Eser: Kamu Malı / Public Domain (CC0)", zeropd)
menu.opsiyon_ekle("Yeni Eser: CC BY", ccby)
menu.opsiyon_ekle("Yeni Eser: CC BY-SA", ccbysa)
menu.opsiyon_ekle("Yeni Eser: CC BY-ND", ccbynd)
menu.opsiyon_ekle("Yeni Eser: CC BY-NC", ccbync)
menu.opsiyon_ekle("Yeni Eser: CC BY-NC-SA", ccbyncsa)
menu.opsiyon_ekle("Yeni Eser: CC BY-NC-ND", ccbyncnd)
menu.opsiyon_ekle("Kayıtlı Bir Eseri Ara", eser_ara)
menu.opsiyon_ekle("Tüm Kayıtlı Eserleri Göster", tum_eserleri_goster)

print("Program başlatılıyor...")
menu.menuOlustur()

   