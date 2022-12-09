## SET

Python set metodları, bir set içinde verileri manipüle etmeyi sağlayan fonksiyonlardır. Örnek olarak, aşağıdaki metodları sayabiliriz:

```py

add(): Bir set içine yeni bir eleman ekler.

clear(): Setin içindeki tüm elemanları siler.

copy(): Seti bir kopyasını oluşturur.

difference(): Set içindeki farklı elemanları geri döndürür.

intersection(): Setlerin kesişimi olan elemanları geri döndürür.

isdisjoint(): İki setin ortak elemanı yoksa True, aksi halde False döndürür.

issubset(): Bir setin, diğer bir set içinde bulunan alt kümesi olup olmadığını kontrol eder.

issuperset(): Bir setin, diğer bir set içinde bulunan üst kümesi olup olmadığını kontrol eder.

pop(): Set içindeki rastgele bir elemanı siler ve geri döndürür.

remove(): Belirtilen elemanı set içinden siler.

```

## DICTIONARY

Python dilinde "dictionary" yapısı, bir anahtar-değer ikilisi olarak düşünülebilen bir veri yapısıdır. Bu veri yapısında anahtarlar benzersiz (unique) olmalıdır ve anahtar değerlerine erişmek için kullanılır.

Python dilinde dictionary veri yapısına ait bazı önemli metodlar şunlardır:

```py

clear() - Bu metod, dictionary veri yapısının içeriğini tamamen temizler ve boş bir dictionary döndürür.

copy() - Bu metod, dictionary veri yapısının bir kopyasını döndürür.

fromkeys() - Bu metod, belirtilen anahtarları içeren bir dictionary oluşturur.

get() - Bu metod, belirtilen anahtarın değerini döndürür. Eğer belirtilen anahtar yoksa, belirtilen varsayılan değer döndürülür.

items() - Bu metod, dictionary veri yapısının anahtar-değer ikililerini döndürür.

keys() - Bu metod, dictionary veri yapısının anahtarlarını döndürür.

pop() - Bu metod, belirtilen anahtarın değerini döndürür ve aynı zamanda dictionary veri yapısından bu anahtarı silerek dictionary'i günceller.

popitem() - Bu metod, rastgele bir anahtar-değer ikilisini döndürür ve aynı zamanda dictionary veri yapısından bu ikiliyi silerek dictionary'i günceller.

setdefault() - Bu metod, belirtilen anahtarın değerini döndürür. Eğer belirtilen anahtar yoksa, belirtilen varsayılan değer ile birlikte bu anahtarı dictionary veri yapısına ekler.

update() - Bu metod, dictionary veri yapısını belirtilen diğer dictionary veri yapısıyla günceller. Eğer aynı anahtarlar var ise, ikinci dictionary veri yapısındaki değerler kullanılır.

```

## TUPLE

Python dilinde "tuple" yapısı, değiştirilemeyen bir veri yapısıdır. Bu veri yapısında bulunan elemanların sırası ve sayısı değiştirilemez.

Python dilinde tuple veri yapısına ait bazı önemli metodlar şunlardır:

```py

count() - Bu metod, belirtilen elemanın tuple veri yapısında kaç kere bulunduğunu döndürür.

index() - Bu metod, belirtilen elemanın tuple veri yapısında ilk olarak bulunan indeksini döndürür.

len() - Bu metod, tuple veri yapısında bulunan eleman sayısını döndürür.

max() - Bu metod, tuple veri yapısındaki en büyük elemanı döndürür.

min() - Bu metod, tuple veri yapısındaki en küçük elemanı döndürür.

sum() - Bu metod, tuple veri yapısındaki elemanların toplamını döndürür.

```

## LIST

Python list metodları, bir listeyi etkileyecek ve düzenleyecek işlemleri yapmak için kullanılan fonksiyonlardır. Örnek olarak;

```py
append(): Listeye bir eleman ekler.

extend(): Listeye bir liste ekler.

insert(): Belirtilen indekse bir eleman ekler.

remove(): Belirtilen elemanı listeden siler.

pop(): Belirtilen indeksten elemanı siler ve döndürür.

index(): Belirtilen elemanın indeksini döndürür.

count(): Belirtilen elemanın listede kaç kez tekrar ettiğini döndürür.

sort(): Listeyi sıralar.

reverse(): Listeyi tersine çevirir.

clear(): Listedeki tüm elemanları siler.

```
