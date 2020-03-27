# 🕵️‍♀️ Obje Algılama Üzerine Notlar
## ⭐ Popüler Modeller
- RCNN (seri olarak)
- SSD
- YOLO

## ⭕ Bölge Tabanlı Ağların Özeti

| 💠 Algoritma    | 📃 Özet                                                           | 👮‍♀️ Sınırlandırma       |
| --------------- | ------------------------------------------------------------------ | ---------------------- |
| 🔷 R-CNN        |  Görüntülerden _selective search_ kullanarak 2000 bölge çıkartır  | Yüksek hesaplama süresi |
| 💫 Fast R-CNN   |  Görüntü _feature maps_ çıkarmak için bir kez CNN'e geçirilir ve sonra bölgeler _selective search_ ile çıkarılır | Selective search yavaştır |
| ➰ Faster R-CNN |  _Selective search_ yöntemini RPN ile değiştirir                  | Yavaş (nispeten, yeterince hızlı değil)  |


## 🤸‍♀️ SSD

SSD obje algılama algoritması 2 bölümden oluşur:
- Feature map'leri çıkarma
- Convolution filtrelerini tespit edilen objelere uygulama.

## 😉 YOLO
Özet: Sistem giriş görüntüsünü S × S grid'e böler. Bir objenin merkezi bir hücreye düşerse, bu hücre bu objeyi algılar.


## 🤹‍♀️ Karşılaştırma 
| Algoritma                      | 🏃‍♀️ Hız    | 🧐 Doğruluk  |
| ------------------------------ | --------- | ------------- |
| ⭕ Bölge tabanlı algoritmalar  | 🛴 Düşük  | 🚀 Yüksek    |
| 😉 YOLO                        | 🚀 Yüksek | 🛴 Düşük |
| 🤸‍♀️ SSD                         | ✈️ Orta  | ✈️ Orta |


### 📢 Not
- 🤹‍♀️ Bu karşılaştırma, modellerin genel karşılaştırılmasıdır
- 👮‍♀️ **İhityaçlara** ve elde bulunan **kaynaklara** göre seçim yapılmalı

## 👩‍⚖️ Seçtiğimiz Model
[SSD + Mobilenet](https://tfhub.dev/tensorflow/ssd_mobilenet_v1/1)

## 🔗 Referanslar
- [🕵️‍♀️ Obje Algılama Temelleri](https://dltr.asmaamir.com/8-objealgilama)