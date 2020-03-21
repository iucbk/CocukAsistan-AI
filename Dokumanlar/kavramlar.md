# 🌱 Genel Kavramlar
## 📚 Popüler Terimler

| Terim                | Açıklama                                       |
| -------------------- | ---------------------------------------------- |
| Classification       | Giriş görüntüsündeki bir objenin etiketini (sınıfını) belirtme |
| Classification and Localization | Giriş görüntüsündeki bir nesnenin etiketini ve koordinatlarını belirtme |
| Object Detection     |  Giriş görüntüsündeki birden fazla nesnenin etiketlerini ve koordinatlarını belirtme |

> Araştırırken yeni kavramlar buldukça buraya ekleyebiliriz 👷‍♂️

## 📑 Daha Detaylı

|             | Classification | Clf. and Localization | Detection              |
| ----------- | -------------- | --------------------- | ---------------------- |
| Obje sayısı | 1              | 1                     | birden fazla           |
| Girdi       | resim          | resim                 | resim                  |
| Çıktı       | etiket         | etiket + koordinatlar | etiket(ler) + koordinatlar |



## TensorFlow Lite
TensorFlow Lite is TensorFlow’s lightweight solution for mobile and embedded devices. It enables on-device machine learning inference with low latency and a small binary size. TensorFlow Lite uses many techniques for this such as quantized kernels that allow smaller and faster (fixed-point math) models.

> TODO: Bu notu çevir 🏴