# Python Collection Types

- List
- Dictionary
- Tuple
- Set

## List

Lists are mutable sequences, typically used to store collections of items (where the precise degree of similarity will vary by application).
Listeler, tipik olarak öğe koleksiyonlarını depolamak için kullanılan değişken dizilerdir (burada kesin benzerlik derecesi uygulamaya göre değişir).

```py
list3 = ["Apple", 1, 3.5, True, [1, 3], {"Ready": "yes"}]
```

### creating a list:

Lists may be constructed in several ways:

- Using a pair of square brackets to denote the empty list: []
- Using the type constructor: list() or list(iterable)
  Listeler birkaç şekilde oluşturulabilir:
- Boş listeyi belirtmek için bir çift köşeli parantez kullanma: []
- Tip yapıcısını kullanma: list() veya list(iterable)

```py
a = list()
print(a)
print(type(a))

name = "rafe stefano"

list1 = ["apple", "banana", "cherry"]
list2 = list(name)

new_list1 = list(list1)
new_list2 = [list1]

print(new_list1)
print(new_list2)
```

The constructor builds a list whose items are the same and in the same order as iterable’s items.
Yapıcı, öğeleri yinelenebilir öğelerle aynı ve aynı sırada olan bir liste oluşturur.

- list('abc') returns ['a', 'b', 'c']
- list( (1, 2, 3) ) returns [1, 2, 3]

### basic operations with list:

Python has a set of built-in methods that you can use on lists:
Python, listelerde kullanabileceğiniz bir dizi yerleşik yönteme sahiptir:

```py
clear()	  # Removes all the elements from the list
copy()	  # Returns a copy of the list
```

- The copy() method in Python returns a copy of the List. We can copy a list to another list using the = operator, however copying a list using = operator means that when we change the new list the copied list will also be changed, if you do not want this behaviour then use the copy() method instead of = operator.
- Python'daki copy() yöntemi, Listenin bir kopyasını döndürür. = operatörünü kullanarak bir listeyi başka bir listeye kopyalayabiliriz, ancak = operatörünü kullanarak bir listeyi kopyalamak, yeni listeyi değiştirdiğimizde kopyalanan listenin de değişeceği anlamına gelir, bu davranışı istemiyorsanız, o zaman copy() yöntemini kullanın = operatörü yerine.

```py
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

count()	  # Returns the number of elements with the specified value # Belirtilen değere sahip öğe sayısını döndürür
extend()  # Add the elements of a list (or any iterable), to the end of the current list # Bir listenin öğelerini (veya yinelenebilir herhangi bir öğeyi) geçerli listenin sonuna ekleyin
index()	  # Returns the index of the first element with the specified value # Belirtilen değere sahip ilk öğenin dizinini döndürür
pop(index)	  # Removes the element at the specified position, assigning the popped item to a new variable # Belirtilen konumdaki öğeyi kaldırır, açılan öğeyi yeni bir değişkene atar
reverse() # Reverses the order of the list # Listenin sırasını tersine çevirir
```

How to reach a value inside a list:
Bir liste içindeki bir değere nasıl ulaşılır:

```py
# Reach to the index no 1 inside inner list:
# İç listedeki 1 numaralı dizine ulaşın:
a = ['ali', 2, [1,2], 7]
a[2][1]
2
```

How to join two list:

```py
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)
# or
list1.extend(list2)
print(list1)

# ['a', 'b', 'c', 1, 2, 3]
```

(document list)[https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range]
(more on list)[https://docs.python.org/3/tutorial/datastructures.html#more-on-lists]

## Dictionary

Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is ordered, changeable and does not allow duplicates.

Dictionaries are written with curly brackets, and have keys and values:

Sözlükler, veri değerlerini anahtar:değer çiftlerinde depolamak için kullanılır.

Sözlük, düzenli, değişken ve tekrarlara izin vermeyen bir koleksiyondur.

Sözlükler süslü parantezlerle yazılır ve anahtarları ve değerleri vardır:

```py
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
# {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

# You can access the items of a dictionary by referring to its key name, inside square brackets:
# Bir sözlüğün öğelerine, köşeli parantez içindeki anahtar adına bakarak erişebilirsiniz:
x = thisdict["model"]
print(x)
# Mustang

# If there is not such a key, it will raise key error. To avoid this use get() method.
# Eğer böyle bir key yoksa key hatası verir. Bunu önlemek için get() yöntemini kullanın.


# There is also a method called get() that will give you the same result:
# Size aynı sonucu verecek olan get() adlı bir yöntem de vardır:
x = thisdict.get("model")
print(x)
# Mustang

# If not, then it will return None (if get() is used with only one argument).
# Default None can be changed to a worning message:
# Değilse, Yok döndürür (eğer get() yalnızca bir bağımsız değişkenle kullanılırsa).
# Varsayılan Hiçbiri eskiyen bir mesaj olarak değiştirilebilir:
thisdict.get("bran", "There is no such a key!")


# The keys() method will return a list of all the keys in the dictionary.
x = thisdict.keys()
print(x)
# dict_keys(['brand', 'model', 'year'])
# Keys can be displayed on a loop:
# Keys bir döngüde görüntülenebilir:
for key in  thisdict.keys():
  print(key)


# Add a new item to the original dictionary, and see that the keys list gets updated as well:
# Orijinal sözlüğe yeni bir öğe ekleyin ve anahtar listesinin de güncellendiğini görün:
thisdict["color"] = "white"


# You can change the value of a specific item by referring to its key name:
# Anahtar adına bakarak belirli bir öğenin değerini değiştirebilirsiniz:
thisdict["year"] = 2022

# The update() method will update the dictionary with the items from the given argument. The argument must be a dictionary, or an iterable object with key:value pairs.
# update() yöntemi, sözlüğü verilen argümandaki öğelerle güncelleyecektir. Argüman bir sözlük veya anahtar:değer çiftlerine sahip yinelenebilir bir nesne olmalıdır.
thisdict.update({"year": 2020})

# Adding an item to the dictionary is done by using a new index key and assigning a value to it:
# Sözlüğe öğe eklemek, yeni bir dizin anahtarı kullanarak ve ona bir değer atayarak yapılır:
thisdict["color"] = "red"

# The pop() method removes the item with the specified key name:
# pop() yöntemi, belirtilen anahtara sahip öğeyi kaldırır
thisdict.pop("model")

# The popitem() method removes the last inserted item
# popitem() yöntemi son eklenen öğeyi kaldırır
thisdict.popitem()


# The del keyword removes the item with the specified key name:
# Del anahtar sözcüğü, belirtilen anahtar adına sahip öğeyi kaldırır:
del thisdict["model"]

# The del keyword can also delete the dictionary completely.

# The clear() method empties the dictionary.
# del anahtar sözcüğü de sözlüğü tamamen silebilir.

# clear() yöntemi sözlüğü boşaltır.
```

- Reaching list item is the same with lists

Dictionary Methods (search in google)

Python has a set of built-in methods that you can use on dictionaries.

- Erişim listesi öğesi, listelerle aynıdır

Sözlük Yöntemleri (google'da arayın)

Python, sözlüklerde kullanabileceğiniz bir dizi yerleşik yönteme sahiptir.

```py
clear()	# Removes all the elements from the dictionary
get()	# Returns the value of the specified key
items()	# Returns a list containing a tuple for each key value pair
keys()	# Returns a list containing the dictionary's keys
values()	# Returns a list of all the values in the dictionary
pop()	# Removes the element with the specified key
popitem()	# Removes the last inserted key-value pair
update()	# Updates the dictionary with the specified key-value pairs

```

## Tuples

- Less memory
- Stable, unchanged values
- Faster
- Daha az hafıza
- Kararlı, değişmeyen değerler
- Daha hızlı

Tuples are immutable sequences, typically used to store collections of heterogeneous data.
Demetler, tipik olarak heterojen veri koleksiyonlarını depolamak için kullanılan değişmez dizilerdir.

Tuples may be constructed in a number of ways:

- Using a pair of parentheses to denote the empty tuple: ()
- Using a trailing comma for a singleton tuple: "a", or ("a",)
- Separating items with commas: "a", "b", "c" or ("a", "b", "c")
- Using the tuple() built-in: tuple() or tuple(iterable)

Demetler çeşitli şekillerde inşa edilebilir:

- Boş demeti belirtmek için bir çift parantez kullanmak: ()
- Tek bir demet için sondaki virgül kullanma: "a" veya ("a",)
- Öğeleri virgülle ayırma: "a", "b", "c" veya ("a", "b", "c")
- Yerleşik Tuple()'ı kullanma: Tuple() veya Tuple(yinelenebilir)

Tuple items are ordered, unchangeable, and allow duplicate values.
Demet öğeleri sıralıdır, değiştirilemez ve yinelenen değerlere izin verir.

To create a tuple with only one item, you have to add a comma after the item
Yalnızca bir öğe içeren bir demet oluşturmak için öğeden sonra virgül eklemeniz gerekir.

```py
thistuple = ("apple",)
print(type(thistuple))

# NOT a tuple
thistuple = ("apple")
print(type(thistuple))

# A tuple with strings, integers and boolean values:
tuple1 = ("abc", 34, True, 40, "male")

# Print the second item in the tuple:
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
```

Python has two built-in methods that you can use on tuples.

```py
count()	# Returns the number of times a specified value occurs in a tuple
# Bir demette belirli bir değerin oluşma sayısını döndürür
index()	# Searches the tuple for a specified value and returns the position of where it was found
# Tuple'ı belirtilen bir değer için arar ve bulunduğu konumu döndürür
```

```py
# Join two tuples:
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

# ('a', 'b', 'c', 1, 2, 3)
```

## Set

Sets are used to store multiple type of items in a single variable.
A set is a collection which is both unordered and unindexed.
Sets are written with curly brackets.
A set can contain different data types:
You cannot access items in a set by referring to an index or a key.

It is possible to use the set() constructor to make a set.

Kümeler, birden çok öğe türünü tek bir değişkende depolamak için kullanılır.
Küme, hem sıralanmamış hem de dizinlenmemiş bir koleksiyondur.
Kümeler süslü parantezlerle yazılır.
Bir küme farklı veri türleri içerebilir:
Bir dizideki öğelere bir dizine veya anahtara başvurarak erişemezsiniz.

Bir küme oluşturmak için set() yapıcısını kullanmak mümkündür.

```py
# Create a Set
thisset = {"apple", "banana", "cherry"}

# Get the number of items in a set:
print(len(thisset))

# To add one item to a set use the add() method.
thisset.add("orange")

# To remove an item in a set, use the remove(), or the discard() method.
thisset.remove("banana")
thisset.discard("banana")

# If the item to remove does not exist, discard() will NOT raise an error.
# Kaldırılacak öğe mevcut değilse, throw() bir hata YÜKSELTMEZ.

# Remove the last item by using the pop() method:
# Pop() yöntemini kullanarak son öğeyi kaldırın:

# Sets are unordered, so when using the pop() method, you do not know which item that gets removed.
# Kümeler sırasızdır, bu nedenle pop() yöntemini kullanırken hangi öğenin kaldırılacağını bilemezsiniz.
```

Python has a set of built-in methods that you can use on sets.

```py
add()	# Adds an element to the set
clear()	# Removes all the elements from the set
copy()	# Returns a copy of the set
difference()	# Returns a set containing the difference between two or more sets
difference_update()	# Removes the items in this set that are also included in another, specified set
# Belirtilen başka bir kümede bulunan öğeleri bu kümeden kaldırır
discard()	# Remove the specified item
intersection()	# Returns a set, that is the intersection of two other sets
# Diğer iki kümenin kesişimi olan bir küme döndürür
intersection_update()	# Removes the items in this set that are not present in other, specified set(s)
# Belirtilen diğer küme(ler)de bulunmayan öğeleri bu kümeden kaldırır
isdisjoint()	# Returns whether two sets have a intersection or not
# İki kümenin kesişimi olup olmadığını döndürür
issubset()	# Returns whether another set contains this set or not
# Başka bir kümenin bu kümeyi içerip içermediğini döndürür
issuperset()	# Returns whether this set contains another set or not
# Bu kümenin başka bir küme içerip içermediğini döndürür
pop()	# Removes an element from the set
remove()	# Removes the specified element
symmetric_difference()	# Returns a set with the symmetric differences of two sets
# İki kümenin simetrik farkları olan bir küme döndürür
symmetric_difference_update()	# inserts the symmetric differences from this set and another
# bu kümeden ve diğerinden simetrik farkları ekler
union()	# Return a set containing the union of sets
# Kümelerin birleşimini içeren bir küme döndür
update()	# Update the set with the union of this set and others.
# Seti bu setin ve diğerlerinin birleşimiyle güncelleyin.
```

```py
a = {1, 2, 3, 10, 32, 100}
b = {1, 2, 32}

a.difference(b)
a.intersection(b)
a.union(b)
```

## Sets vs Lists vs Tuples and Dictionary

![Data Types](data_types.png)

## Summary

- List

  - Intro
  - Creating List
    - []
    - list()
  - Basic operations with list
    - append()
    - insert()
    - remove()
    - sort()
    - len()
    - pop()
    - extend()
    - index()
    - count()
  - Accessing Lists
    - Indexing
    - Slicing
    - Negative Indexing & Slicing

- Dictionary

  - Intro
  - Creating Dictionary

    - {}
    - dict()

  - Basic operations with list

    - clear()
    - get()
    - items()
    - keys()
    - pop()
    - popitem()
    - update()

  - Accessing Dictionaries
    - nested dicts

- Tuples

  - Intro
  - Creating Tuples

    - ()
    - tuple()

  - Basic operations with tuple
    - accessings items with indexing
    - count()
    - index()

- Set

  - Intro
  - Creating Sets

    - {}
    - set()

  - Basic operations with tuple
    - add()
    - remove()
    - discard
    - pop()
    - intersection()
    - union()
    - difference()
