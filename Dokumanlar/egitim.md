# 👩‍🏫 Özelleştirilmiş Model Eğitme Notları
TFLite'ta model eğitirken aldığımız notlar


## 🥴 Karışık Notlar 

```
ValueError: Label map id 0 is reserved for the background label
```
Hatasından dolayı label_map'ı 1'den başlatıyoruz

> TODO: Eğitim notları buraya eklenecek 👮‍♀️

## 👼 Sonuç Modeli
- [📍 Burada](../Model/tflite) tutulmakata
- [👨‍💻 Buradaki](../Scripts/get_tf_info.py) script ile giriş ve çıkış bilgileri bu şekildedir:

```py
# input shape and type
[  1 300 300   3]
<class 'numpy.float32'>

# output shape and type
[ 1 10  4]
<class 'numpy.float32'>
```

## 🔗 Faydalı Bağlantılar
- [TFLite Object Detection](https://www.tensorflow.org/lite/models/object_detection/overview)