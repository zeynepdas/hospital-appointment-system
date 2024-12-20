import datetime

# T.C. Kimlik Doğrulama Fonksiyonu
def tc_kimlik_dogrula(tc):
    # T.C. kimlik numarası 11 haneli ve rakamlardan oluşmalı
    if len(tc) != 11 or not tc.isdigit():
        return False
    # İlk hane sıfır olamaz
    if tc[0] == '0':
        return False
    # İlk 10 hanenin toplamının birler basamağı, 11. haneye eşit olmalı
    if sum(int(tc[i]) for i in range(10)) % 10 != int(tc[10]):
        return False
    return True

# Kullanıcı Bilgilerini Alma ve Doğrulama
while True:
    isim = input("Lütfen Adınızı Giriniz: ").strip().capitalize()
    soy_isim = input("Lütfen Soyadınızı Giriniz: ").strip().capitalize()
    kimlik_no = input("Lütfen T.C. Kimlik Numaranızı Giriniz: ").strip()

    if tc_kimlik_dogrula(kimlik_no):
        print("\n✅ T.C. Kimlik Numarası geçerli.")
        break
    else:
        print("\n❌ Geçersiz T.C. Kimlik Numarası! Lütfen tekrar deneyin.")

print("\n" + "-" * 40)
print(f"Hoşgeldiniz, {isim} {soy_isim}!")
print(f"T.C. Kimlik No: {kimlik_no}")
print("-" * 40 + "\n")

# Ağaç Yapısı Tanımları
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

class HospitalTree:
    def __init__(self, name):
        self.root = TreeNode(name)

    def add_department(self, department_name):
        department_node = TreeNode(department_name)
        self.root.add_child(department_node)

    def display(self, node=None, level=0):
        if node is None:
            node = self.root
        print("  " * level + node.value)
        for child in node.children:
            self.display(child, level + 1)

# Bölümler ve Doktorlar
hospital = HospitalTree("🏥 Yalova Devlet Hastanesi")
departments_with_doctors = {
    "Beyin ve Sinir Cerrahisi": ["Dr. Murat Yücel", "Dr. Çetin Serim","Dr. Ali Tekin"],
    "Göğüs Hastalıkları": ["Dr. Pınar Tunç", "Dr. Mine Deniz","Dr. Nurettin Kaya"],
    "Kulak Burun Boğaz Hastalıkları": ["Dr. Ali Uz", "Dr. Ftih Sarı","Dr. Sinan Tilki"],
    "Deri ve Zührevi Hastalıklar": ["Dr. Emin Ay", "Dr. Gizem Çetinkaya","Dr. Gizem Eren"],
    "Ortopedi ve Travmoloji Uzmanı": ["Dr. Murat Özcan", "Dr. Gözde Kırgın","Dr. Mustafa Bakır"],
    "Genel Cerrahi": ["Dr. Ertunç Altuntaş", "Dr. Mehmt Ali Yücesoy","Dr. Kemal Gül"],
    "Kalp ve Damar Cerrahisi": ["Dr. Şafak Şimşek", "Dr. Seçkin Sarı","Dr. Fulya Topuz"],
    "Ruh Sağlığı ve Hastalıkları": ["Dr. Ali Ulu", "Dr. Ezgi Güngör","Dr. Fatih Serin"],
    "Kadın Hastalıkları ve Doğum Uzmanı": ["Dr. Zeynep Arslan", "Dr. Kıvanç Kayhan", "Dr. Zerrin Çelik"],
    "Göz Hastalıkları": ["Dr. Elvin Çelenk", "Dr. Kadir İlker Çankaya","Dr. Esra Kındır"]
}

# Bölümleri ağaca ekleyelim (Doktorlar gizli)
for dept in departments_with_doctors.keys():
    hospital.root.add_child(TreeNode(dept))

# Bölümleri gösterelim
print("📋 Mevcut Bölümler:")
hospital.display(level=1)  # Sadece bölümleri göster (doktorları değil)

# Bölümler listesi (küçük harf ile eşleştirme için)
departments_lower = [dept.lower() for dept in departments_with_doctors.keys()]

# Linked List Node Tanımı
class Node:
    def __init__(self, doctor, department, date, time):
        self.doctor = doctor
        self.department = department
        self.date = date
        self.time = time
        self.next = None  # Sonraki randevuya bağlantı

# Linked List Tanımı
class AppointmentList:
    def __init__(self):
        self.head = None

    # Randevu ekleme
    def add_appointment(self, doctor, department, date, time):
        new_node = Node(doctor, department, date, time)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    # Randevuları gösterme
    def display_appointments(self):
        current = self.head
        if not current:
            print("\n❌ Henüz randevu alınmamış.")
        while current:
            print(f"\nDoktor: {current.doctor}")
            print(f"Bölüm: {current.department}")
            print(f"Tarih: {current.date}")
            print(f"Saat: {current.time}")
            current = current.next

# Girilen tarihin geçip geçmediğini kontrol eden fonksiyon
def check_past_date(input_date):
    try:
        # Kullanıcının girdiği tarihi datetime objesine çevir
        entered_date = datetime.datetime.strptime(input_date, "%d.%m.%Y")

        # Bugünün tarihini al
        current_date = datetime.datetime.now()

        # Tarih karşılaştırması
        if entered_date < current_date:
            return True  # Girilen tarih geçmiş
        else:
            return False  # Girilen tarih gelecekte
    except ValueError:
        print("\n❌ Geçersiz tarih formatı! Lütfen GG.AA.YYYY formatında giriniz.")
        return None  # Geçersiz tarih formatı

# Tarih alma ve kontrol etme
def get_appointment_date():
    while True:
        tarih = input("Randevu Tarihini Giriniz (GG.AA.YYYY): ").strip()
        result = check_past_date(tarih)
        if result is not None:
            if result:
                print("\n❌ Girilen tarih geçmiş bir tarihtir! Lütfen geçerli bir tarih giriniz.")
            else:
                print("\n✅ Geçerli bir tarih girdiniz.")
                return tarih  # Geçerli tarih döndürülür
        else:
            continue

# Randevu alma işlemi
appointment_list = AppointmentList()

while True:
    bölüm = input("\nRandevu Almak İstediğiniz Bölümü Seçiniz: ").strip().lower()
    if bölüm in departments_lower:
        seçilen_bölüm = list(departments_with_doctors.keys())[departments_lower.index(bölüm)]
        print(f"\n✅ {seçilen_bölüm} bölümünde randevu almak istediniz.")
        
        # Doktorları listele
        doktorlar = departments_with_doctors[seçilen_bölüm]
        print("\nBu bölümdeki doktorlar:")
        for i, doktor in enumerate(doktorlar, 1):
            print(f"{i}. {doktor}")
        
        # Doktor seçimi
        while True:
            try:
                doktor_seçim = int(input("\nRandevu almak istediğiniz doktorun numarasını seçiniz: "))
                if 1 <= doktor_seçim <= len(doktorlar):
                    seçilen_doktor = doktorlar[doktor_seçim - 1]
                    print(f"\n✅ {seçilen_doktor} doktorundan randevu almak istediniz.")
                    break
                else:
                    print("\n❌ Geçersiz bir seçim yaptınız. Lütfen tekrar deneyin.")
            except ValueError:
                print("\n❌ Lütfen geçerli bir sayı girin.")
        
        # Randevu tarihi ve saatini alalım
        print("\nRandevu Tarihi ve Saati Seçiniz.")
        randevu_tarih = get_appointment_date()

        # Saat alımı ve doğrulama
        while True:
            saat = input("Randevu Saatini Giriniz (HH.MM): ").strip()
            try:
                # Saat formatını doğrulama
                datetime.datetime.strptime(saat, "%H.%M")
                break  # Saat geçerli, çıkıyoruz
            except ValueError:
                print("\n❌ Geçersiz saat formatı! Lütfen HH:MM formatında giriniz.")

        # Randevuyu listeye ekleyelim
        appointment_list.add_appointment(seçilen_doktor, seçilen_bölüm, randevu_tarih, saat)
        break
    else:
        print("\n❌ Geçersiz bir bölüm girdiniz. Lütfen tekrar deneyin.")

# Randevularınızı görüntüleyelim
print("\nRandevularınız:")
appointment_list.display_appointments()

print("\nRandevunuz başarıyla alınmıştır. Sağlıklı günler dileriz! 🌟")
