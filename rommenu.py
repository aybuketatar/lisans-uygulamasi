class MenuSistemi:
    def __init__(self):
        self.baslik = "Başlık Menü"
        self.secenekler = []

    def karsilama(self, program_adi):
        self.baslik = program_adi

    def opsiyon_ekle(self, isim, fonksiyon):
        self.secenekler.append( (isim, fonksiyon) )

    def menuOlustur(self):
        while True:
            print(f"\n===== {self.baslik} =====")

            for i, (isim, _) in enumerate(self.secenekler, start=1):
                print(f"{i}: {isim}")

            cikis_numarasi = len(self.secenekler) + 1
            print(f"{cikis_numarasi}: Çıkış")

            secim_str = input("\nLütfen bir seçim yapınız: ")

            try:
                secim = int(secim_str)

                if 1 <= secim <= len(self.secenekler):
                    calistirilacak_fonksiyon = self.secenekler[secim - 1][1]
                    calistirilacak_fonksiyon()

                elif secim == cikis_numarasi:
                    print("Uygulamadan çıkılıyor...")
                    break 
                else:
                    print("Hata: Geçersiz seçim. Lütfen listeden bir numara girin.")

            except ValueError:
                print("Hata: Lütfen sadece sayı giriniz.")