# Tree-menu test project
## _Древовидное меню, реализованное на custom  template tag_


## Особенности

> В админке (http://localhost/admin) можно создать несколько меню 
> и компонентов. Компоненты могут быть родителями других компонентов.
> При клике на каждое меню происходит переход на его страницу.
> В главное меню можно вернуться по соответствующей кнопке.

> Приложение работает на данных из БД (все компоненты, 
> которые относятся к определенному меню, отображаются на его странице).

> Используется рекурсивный алгоритм для построения меню на основе элементов модели. 
> Он использует рекурсию для обхода иерархии меню и вставки подменю в соответствующие пункты меню.

## Стэк

- Python 3.9
- Django 3.2.24
- Django Templates
- SQLite3

## Развернуть проект 
Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/jisdtn/test-UpTrader-tree-menu
```

```
cd test-UpTrader-tree-menu
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

```
source venv/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить backend проекта:

```
python3 manage.py runserver
```
### Примеры запросов.

```commandline
http://localhost/admin
```
```commandline
http://localhost/menu
```

## License

MIT


