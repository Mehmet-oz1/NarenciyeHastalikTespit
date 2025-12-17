# 🍊 Narenciye Hastalık Tespiti ve Analizi (Citrus Disease Detection)

![Project Banner](docs/banner.png)

> **Proje Özeti:** Bu proje, görüntü işleme ve derin öğrenme teknikleri kullanılarak narenciye bitkilerindeki (portakal, limon, mandalina vb.) hastalıkları yaprak görüntüleri üzerinden otomatik olarak tespit etmeyi amaçlar. Geliştirilen Yapay Zeka modeli, **Streamlit** ile hazırlanmış kullanıcı dostu bir web arayüzü üzerinden hizmet vermektedir.

## 📋 İçindekiler
- [Proje Hakkında](#-proje-hakkında)
- [Veriseti ve Sınıflar](#-veriseti-ve-sınıflar)
- [Proje Mimarisi](#-proje-mimarisi)
- [Kullanılan Teknolojiler](#-kullanılan-teknolojiler)
- [Kurulum](#-kurulum)
- [Kullanım](#-kullanım)
- [İletişim](#-iletişim)

---

## 📌 Proje Hakkında
Tarım sektöründe bitki hastalıklarının erken teşhisi, ürün kaybını önlemek için hayati önem taşır. Bu proje, narenciye yapraklarının fotoğraflarını analiz ederek bitkinin sağlık durumunu saniyeler içinde belirleyen bir yapay zeka çözümü sunar.

Proje süreci şu adımları içerir:
1.  **Görsel Veri İşleme:** Yaprak görüntülerinin modele uygun hale getirilmesi (Boyutlandırma, filtreleme).
2.  **Model Eğitimi:** CNN (Convolutional Neural Network) tabanlı derin öğrenme mimarisi ile görüntülerin sınıflandırılması.
3.  **Web Arayüzü:** Son kullanıcının fotoğraf yükleyip anlık sonuç alabileceği Streamlit paneli.

## 📂 Veriseti ve Sınıflar
Model, yaprak görüntülerini analiz ederek aşağıdaki 4 durumu tespit edebilmektedir:

* **Healthy (Sağlıklı):** Herhangi bir hastalık belirtisi göstermeyen yapraklar ve meyveler.
* **Sick (Hastalıklı):** Herhangi bir hastalık belirtisi gösteren yapraklar ve meyveler.

## 🏗 Proje Mimarisi
Proje aşağıdaki akış şemasına göre çalışmaktadır:
`Görüntü Yükleme -> Ön İşleme (OpenCV) -> Yapay Zeka Analizi (TensorFlow/CNN) -> Sonuç Gösterimi (Streamlit)`

## 🛠 Kullanılan Teknolojiler
Projede aşağıdaki kütüphaneler ve araçlar kullanılmıştır:

* **Dil:** Python 3.x
* **Arayüz & Dashboard:** Streamlit
* **Derin Öğrenme:** TensorFlow, Keras
* **Görüntü İşleme:** OpenCV, Pillow
* **Veri Analizi:** Pandas, NumPy
* **Görselleştirme:** Matplotlib
* **Versiyon Kontrol:** Git & GitHub

## 🚀 Kurulum

Projeyi yerel makinenizde çalıştırmak için:

1.  **Repoyu klonlayın:**
    ```bash
    git clone [https://github.com/Mehmet-oz1/NarenciyeHastalikTespit.git](https://github.com/Mehmet-oz1/NarenciyeHastalikTespit.git)
    cd NarenciyeHastalikTespit
    ```

2.  **Sanal ortam oluşturun (Önerilen):**
    ```bash
    python -m venv venv
    # Windows için:
    venv\Scripts\activate
    # Mac/Linux için:
    source venv/bin/activate
    ```

3.  **Gerekli kütüphaneleri yükleyin:**
    ```bash
    pip install -r requirements.txt
    ```

## 💻 Kullanım

Kurulum tamamlandıktan sonra web arayüzünü başlatmak için terminale şu komutu girin:

```bash
streamlit run main.py

```

*(Not: Ana dosya isminiz farklıysa `main.py` kısmını `app.py` veya ilgili dosya ismiyle değiştiriniz.)*

Tarayıcınızda otomatik olarak `http://localhost:8501` adresi açılacak ve analiz ekranı gelecektir.

---

## 📧 İletişim

Herhangi bir soru veya geri bildirim için:

* **Geliştirici:** Mehmet ÖZ
* **GitHub:** [Mehmet-oz1](https://github.com/Mehmet-oz1)

```

```
