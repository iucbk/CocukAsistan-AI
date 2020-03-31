# Quantization

Quantization işlemi elektronikte analog verilerin dijitale çevrilmesi ile ilgilidir.
Bizim bağlamımızda ise quantization verilerin bilgisayarlarımızda nasıl saklandıkları ile ilgilenir.

## Float Point vs Fixed Point

Float dediğimiz veri tipi bilgisayarlarda 32 bitlik yer kaplar. Burada float-point ve fixed-point kavramlarına değinmek gerekir.

Floating point konsepti bu [video](https://www.youtube.com/watch?v=PZRI1IfStY0)da Tom Scott ❤ tarafından oldukça iyi açıklanmış.

Computerphile'in başka bir [video](https://www.youtube.com/watch?v=f4ekifyijIg&t=651s)sunda ise ondalıklı sayıların fixed point şeklinde nasıl saklandıkları anlatılmış.

Basitçe özetlemek gerekirse eğer 32-Bitlik bir yeriniz varsa 16 biti tam sayı kalan 16 biti ise ondalıklı kısım için ayrılır. Genellikle bu oyun ve grafik programları için elverişlidir fakat büyük sayıları bu şekilde saklayamazsınız.

Fixed point konsepti ise bize ilkokulda öğretilen "ondalıklı sayıların bilimsel gösterimi"nin ikili sayı sistemlerindeki karşılığıdır. Elimizdeki belleği sign-bit (işareti belirtir), exponent (2'nin üssü belirtilir) ve mantissa (elimizdeki gerçek sayı) olarak ayırarak daha büyük aralıktaki sayıları gösterebiliriz.

Bizim yapmayı hedeflediğimiz quantization işlemi 32 bitlik float verileri 8 bitlik integer verilere dönüştürür. Bunu yaparken dönüştürülecek verilerin aralığı bilinmelidir. Bu önemlidir çünkü bu işlem basit bir yuvarlama değildir. Bu işlemde float verimizin yukarıda bahsettiğim exponent kısmı bildiğimiz range dahilinde ortak tutulur ve mantissa kısmı integere çevirilir. Elbette bu aşamada yalnızca 256 sayıya sahip olduğumuzdan bazı değerler yuvarlanır ama sahip olacağımız avantajlar karşısında bu göz ardı edilebilir. 

Quantization Avantajları
-

- Daha az bit ile yapılan aritmetik işlemler daha hızlıdır.
- 32 bitten 8 bite geçiş 4 kat fazla hafıza kazandırır.
- Küçük bit uzunlukları sayesinde daha çok bilgiyi registerlara sığdırır ve bus trafiğini azaltırız.
- Bazı mikroontrolcüler floating-point aritmetiğini desteklemez.

## Neden DNN'lerde kullanılır?


- DNN'ler gürültü ve küçük değişikliklere karşı genellikle duyarsızdır. 
- DNN parametreleri genellike küçük bir aralıktadır. (256 integere sığdırabilmek için)

## Tensorflow ve Quantization


- Önceden eğitilmiş olduğu için katmanların parametreleri rangeleri bilindiği sürece kolayca quantize edilebilir.
	**Fakat bu yeterli değildir. Quantization input ve output değerleri ile birlikte tüm sisteme uygulanmalıdır.**
- Initial input değerleri de quantize edilmelidir.
- Bir katmanın outputu genellikle bir diğerinin inputudur. Bunlar bir kaç outlier dışında belli bir range a sahiptir. bu değerler de quantization işlemine tabii tutulmalıdır. Fakat bu iç değerler oldukça önemli olduklarından işlem sırasında (artık float point değil integer aritmetiği yapılır) overflowdan kaçınmak için 32 bitlik integer değerlerine çevirilirler. Daha sonra ise 8 bitlik integere çevirilirler.
- Son outputlarda quantize edilir.
- Doğruluk artırılmak isteniyorsa bu düzenle yeniden eğitim yapılması önerilmiş. 

## Fake Quantization


Tensorflow'daki fake quantization konsepti eğitim sırasında parametreleri tune ederek (yine float biçiminde olmasına rağmen) quantization işlemine elverişli hale getirir. Aynı zmaanda fake quantization modülleri aktivasyonların aralıklarını bizim için kayıt eder.

TL;DR [Tensorflow Quantization Tutorial](https://www.tensorflow.org/lite/performance/post_training_quantization)




