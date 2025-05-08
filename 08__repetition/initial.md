### Здесь переписаны начальные условия для classwork_02 и homework.

Есть 4 таблицы:

Таблица Product содержит данные о производителе, номере модели и типе продукта ('PC', 'Laptop' или 'Printer'): (maker, model, type)

Каждый персональный компьютер в таблице PC идентифицируется уникальным кодом и дополнительно характеризуется своей моделью, скоростью процессора, объемом оперативной памяти, объемом жесткого диска, скоростью CD-ROM. (code, model, speed, ram, hd, cd, price)

Таблица Laptop аналогична таблице PC, за исключением того, что вместо скорости CD-ROM она содержит размер экрана (в дюймах. (code, model, speed, ram, hd, price, screen)

Для каждого принтера в таблице Printer указывается его тип вывода, технология печати, а также цена. (code, model, color,type, price)

Результат сведены в 4 запроса:
```
SELECT maker, model, type
FROM Product
WHERE type IN ('PC', 'Laptop', 'Printer');

SELECT code, model, speed, ram, hd, cd, price
FROM PC;

SELECT code, model, speed, ram, hd, price, screen
FROM Laptop;

SELECT code, model, color, type, price
FROM Printer;
```