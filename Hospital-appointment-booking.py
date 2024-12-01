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

# Hastane ve Bölümler
hospital = HospitalTree("🏥 Yalova Devlet Hastanesi")
departments = [
    "Beyin ve Sinir Cerrahisi",
    "Göğüs Hastalıkları",
    "Kulak Burun Boğaz Hastalıkları",
    "Deri ve Zührevi Hastalıklar",
    "Ortopedi ve Travmoloji Uzmanı",
    "Genel Cerrahi",
    "Kalp ve Damar Cerrahisi",
    "Ruh Sağlığı ve Hastalıkları",
    "Kadın Hastalıkları ve Doğum Uzmanı",
    "Göz Hastalıkları"
]

# Bölümleri Ekleyelim
for dept in departments:
    hospital.add_department(dept)

# Bölümleri Gösterelim
print("📋 Mevcut Bölümler:")
hospital.display()

# Randevu Alma
departments_lower = [dept.lower() for dept in departments]
while True:
    bölüm = input("\nRandevu Almak İstediğiniz Bölümü Seçiniz: ").strip().lower()
    if bölüm in departments_lower:
        seçilen_bölüm = departments[departments_lower.index(bölüm)]
        print(f"\n✅ {seçilen_bölüm} bölümünde randevu almak istediniz.")
        break
    else:
        print("\n❌ Geçersiz bir bölüm girdiniz. Lütfen tekrar deneyin.")

print("\nRandevunuz başarıyla alınmıştır. Sağlıklı günler dileriz! 🌟")
