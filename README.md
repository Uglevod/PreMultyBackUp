# PreMultyBackUp
Pre Multy BackUp


Есть куча мультиязычных проектов питон, нода, пхп.
от этого есть каталоги модулей и виртуальных окружений и композера.

Для того что бы сделать компактный бекап нужно что бы не было лишнего.
Для этого с начала выстраиватся дерево каталогов с разрешенным содержанием и названиями.
+ в базе можно посмотреть количество файлов в каждой - на предмет какого нибудь сбора иконок с количеством в 1801 штуку.
Добавить в исключения в ручную.

это степ 1 (st1... )

data.json - данные исходной и папки  где будет формироваться копия.


далее создать структуру  - ст3

ст5 - сканируем наполнения разрешенных папок - и формируем спиок файлов для копирования

ст7 - копирование файлов

и далее ручками в архив и на полку. 
и радуемся тому что теперь есть бэкап.

Можно дополнять своими условиями отсева негодных папок, это делается легко на 1 шаге.
в котором есть дублированный код

1 - это скан корневой для источника директори
2 - это уже проходка по поддиректориям
можно добавлять свои особые условия и в 

сделано через базу, os.walk был отброшен - так как хотелось оптимизировать по времени и исключить из обхода директории с виртуальными окружениями уже на старте,
при рабате с базой удалось этого достичь 
+ при работе с базой увеличивается читабельность и понятность кода.

Фаил реквариментс отсутвует
но если вы работали с MySQL через MySQLAlchemy, проблем возникунуть не должно.
