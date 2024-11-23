# Kaggle linki

https://www.kaggle.com/code/berkinyildirim/aygaz-data-analysis-bootcamp

---

# Powerlifting Veri Analizi Projesi

## 📚 Proje Hakkında
Bu proje, Kaggle'dan alınan Powerlifting veri setini analiz ederek sporcuların performanslarını değerlendirmeyi ve veri üzerinde keşifsel analiz (EDA) gerçekleştirmeyi amaçlamaktadır. Proje, eksik veri simülasyonu, veri temizleme, görselleştirme ve istatistiksel analiz gibi adımları içermektedir. Ayrıca, veri setinden çıkarılabilecek potansiyel kullanımlara yönelik önerilerde bulunulmuştur.

---

## 🚀 Özellikler
Bu projede aşağıdaki işlemler gerçekleştirilmiştir:
1. **Veri Setinin Yüklenmesi ve İncelenmesi**:
   - Veri seti pandas kütüphanesi kullanılarak yüklenmiş ve ilk birkaç satır incelenmiştir.
   - Değişkenlerin isimleri ve türleri analiz edilmiştir.

2. **Eksik Veri Simülasyonu ve Yönetimi**:
   - Gerçek hayatta karşılaşılabilecek eksik veri durumlarını simüle etmek için veri setine rastgele eksik değerler eklenmiştir.
   - Eksik veriler:
     - Medyan değer ile doldurulmuş.
     - Kritik sütunlarda eksik veri içeren satırlar kaldırılmıştır.

3. **Veri Temizleme**:
   - Mantıksız (negatif) ve eksik değerler temizlenmiştir.
   - `Sex` sütunu kategorik bir değişkene dönüştürülmüştür.

4. **Veri Görselleştirme**:
   - Cinsiyet dağılımı çubuk grafik ile görselleştirilmiştir.
   - Yaş ve toplam kaldırış performansı arasındaki ilişki scatter plot ile analiz edilmiştir.
   - Korelasyon matrisi ısı haritası ile görselleştirilerek değişkenler arasındaki ilişkiler incelenmiştir.

5. **Keşifsel Veri Analizi (EDA)**:
   - Veri setindeki ilişkiler analiz edilmiş ve temel istatistiksel çıkarımlar yapılmıştır.

---

## 🛠️ Kullanılan Araçlar ve Teknolojiler
Bu projede aşağıdaki araçlar ve kütüphaneler kullanılmıştır:
- **Python 3.x**
- **Kütüphaneler**:
  - `pandas`: Veri manipülasyonu ve analizi.
  - `numpy`: Sayısal hesaplamalar.
  - `matplotlib`: Veri görselleştirme.
  - `seaborn`: Gelişmiş veri görselleştirme.
- **Veri Seti Kaynağı**: [Kaggle Powerlifting Veritabanı](https://www.kaggle.com/open-powerlifting-database)

---

## 📊 Sonuçlar ve Çıkarımlar
### Analiz Sonuçları:
1. **Cinsiyet Dağılımı**:
   - Erkek katılımcılar kadınlardan önemli ölçüde fazladır.
   - Bu dengesizlik analiz sonuçlarında cinsiyet farklılıklarını değerlendirirken dikkate alınmalıdır.

2. **Yaş ve Performans İlişkisi**:
   - Yaş ile toplam kaldırış arasında belirgin bir ilişki bulunmamıştır.
   - Ancak genç yaş grubundaki sporcular genelde daha yüksek kaldırış kapasitelerine sahiptir.

3. **Korelasyon Analizi**:
   - `TotalKg` (toplam kaldırış) ile diğer kaldırış türleri (`BestSquatKg`, `BestBenchKg`, `BestDeadliftKg`) arasında yüksek bir korelasyon bulunmaktadır.
   - Vücut ağırlığı (BodyweightKg) ile kaldırış performansı arasında orta düzeyde bir ilişki gözlemlenmiştir.

---

## 🧑‍💻 Nasıl Çalıştırılır?
### Gereksinimler:
- Python 3.x
- Gerekli kütüphaneleri yüklemek için:
   ```bash
   pip install pandas numpy matplotlib seaborn
