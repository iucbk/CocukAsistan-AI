Quantization
-
Quantization işlemi elektronikte analog verilerin dijitale çevrilmesi ile ilgilidir.
Bizim bağlamımızda ise quantization verilerin bilgisayarlarımızda nasıl saklandıkları ile ilgilenir.

Float Point vs Fixed Point
-
Float dediğimiz veri tipi bilgisayarlarda 32 bitlik yer kaplar. Burada float-point ve fixed-point kavramlarına değinmek gerekir.

Floating point konsepti bu [video](https://www.youtube.com/watch?v=PZRI1IfStY0)da Tom Scott ❤ tarafından oldukça iyi açıklanmış.

Computerphile'in başka bir [video](https://www.youtube.com/watch?v=f4ekifyijIg&t=651s)sunda ise ondalıklı sayıların fixed point şeklinde nasıl saklandıkları anlatılmış.

Basitçe özetlemek gerekirse eğer 32-Bitlik bir yeriniz varsa 16 biti tam sayı kalan 16 biti ise ondalıklı kısım için için ayrılır. Genellikle bu oyun ve grafik programları için elverişlidir fakat büyük sayıları bu şekilde saklayamazsınız.

Fixed point konsepti ise bize ilkokulda öğretilen "ondalıklı sayıların bilimsel gösterimi"nin ikili sayı sistemlerindeki karşılığıdır. Elimizdeki belleği sign-bit (işareti belirtir), exponent (2'nin üssü belirtilir) ve mantissa (elimizdeki gerçek sayı) olarak ayırarak daha büyük aralıktaki sayıları gösterebiliriz.

Bizim yapmayı hedeflediğimiz quantization işlemi 32 bitlik float verileri 8 bitlik integer verilere dönüştürür. Bunu yaparken dönüştürülecek verilerin aralığı bilinmelidir. Bu önemlidir çünkü bu işlem basit bir yuvarlama değildir. Bu işlemde float verimizin yukarıda bahsettiğim exponent kısmı bildiğimiz range dahilinde ortak tutulur ve mantissa kısmı inegere çevirilir. Elbette bu aşamada yalnızca 256 sayıya sahip olduğumuzdan bazı değerler yuvarlanır ama sahip olacağımız avantajlar karşısında bu göz ardı edilebilir. 

