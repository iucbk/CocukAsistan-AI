# 📖 Script Dokümanı
## 🔃 OIDv4 To VOC XML format
- 👨‍💻 OpenImages veri setinin etiketlemesini VOC formatına çeviren script
- 🚩 Scripte [buradan](./OIDv4_to_VOC.py) erişebilirsiniz
- 💻 CLI scriptidir
- 💁 [Atri](https://github.com/AtriSaxena/OIDv4_to_VOC)'ye teşekkürler
### 👩‍🔧 Kullanım

**🏗️ Bulunması gereken dosya yapısı:**
```
<sınıf_ismi>
  |___ Label
  |  |___ label_dosyası1.txt   
  |  |___ label_dosyası2.txt   
  |  |___ label_dosyası3.txt   
  |  |___ ...   
  |___ resim_dosyası1.jpg
  |___ resim_dosyası2.jpg
  |___ resim_dosyası3.jpg
  |___ ...
```

**▶️ Çalıştırma:**
```bash
python OIDv4_to_VOC.py --sourcepath <kaynak_klasörün_yolu> --dest_path <hedef_klasörün_yolu>
```

## 🤸‍♀️ Yeniden Adlandrıma
- 👨‍💻 OpenImages veri setinin etkletlerini ve resim dosyalarını karşılıklı olarak yeniden adlandıran script
- 🚩 Scripte [buradan](./rename.py) erişebilirsiniz
- 💻 CLI scriptidir

**▶️ Çalıştırma:**
```bash
python rename.py --sourcepath <kaynak_klasörün_yolu> --id <başa_yazılacak_isim>
```

