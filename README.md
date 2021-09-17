## Входное задание на курс coderiders.academy

---

### Руководство по запуску

### 1. Запуск как ПО

#### Требования к системе: 
- ОС Linux
- Python 3.8+

#### Задание 1. Сортировки, сортировочки
```
  cd task01
  python3 -m venv venv
  source venv/bin/activate
  python3 task01.py
  deactivate
```

#### Зaдание 2. Базы данных
```
  cd task02
  python3 -m venv venv
  source venv/bin/activate
  pip3 install --upgrade pip
  pip3 install -r requirements.txt
  python3 task02.py
  deactivate
```

#### Зaдание 3. Лифты
```
  cd task03
  python3 -m venv venv
  source venv/bin/activate
  pip3 install --upgrade pip
  pip3 install -r requirements.txt
  pip3 install -e .
  python3 task03.py [-h][-v]
  deactivate
```

Использование с ключами:

```
  -h - получение помощи
```

Пример запуска:

```
  (venv) ~/coderiders_academy_testcase/task03 on dev-python ● ● λ python3 task03.py -h

  usage: task03.py [-h] [-v]

  code.riders academy test case 3. Elevators, elevators everywhere.

  optional arguments:
    -h, --help  show this help message and exit
    -v          Be more verbose.

```

```
  -v - включение логиования и больше отладочной информации
```

Пример запуска:

```
  (venv) ~/coderiders_academy_testcase/task03 on dev-python ● ● λ python3 task03.py -v

  2021-09-13 23:02:09.467 | INFO     | __main__:main:15 - Verbosity level increased.
  2021-09-13 23:02:09.468 | INFO     | __main__:main:20 - Creating application...
  2021-09-13 23:02:09.468 | INFO     | app:__init__:7 - Application.init
  2021-09-13 23:02:09.468 | INFO     | src.building:__init__:7 - Building init.
  2021-09-13 23:02:09.468 | DEBUG    | src.building:__init__:11 - Elevators in building: [Elevator(id=0, floor=1), Elevator(id=1, floor=1), Elevator(id=2, floor=1)]
  2021-09-13 23:02:09.468 | SUCCESS  | src.building:__init__:12 - Building init done. The building has 9 floors and 3 elevators.
  2021-09-13 23:02:09.469 | INFO     | src.building:get_state:16 - Getting building state...
  2021-09-13 23:02:09.469 | DEBUG    | app:__init__:9 - Building created as: Building(floor_count=9, elevator_count=3, elevators_state=[(0, 1), (1, 1), (2, 1)])
  2021-09-13 23:02:09.469 | SUCCESS  | app:__init__:10 - Application.init done.
  2021-09-13 23:02:09.469 | SUCCESS  | __main__:main:22 - Creating application... done
  2021-09-13 23:02:09.469 | INFO     | __main__:main:24 - Running application...
  2021-09-13 23:02:09.469 | INFO     | app:run:13 - Enter floor number or * for exit.

  ...

```

### 1.1 Запуск проверки по правилам PEP8

```
 python3 -m venv venv
 source venv/bin/activate
 pip3 install --upgrade pip
 pip3 install -r requirements.txt
 make pep8
 deactivate
```



---

### 2. Блокнот Google Colaboratory (Colab) (Jupyter notebook)

Блокнот можно посмотреть по [этой ссылке](https://colab.research.google.com/drive/1MlQQA1SeHE6Z4uqhooKq0AJTqYnwP09B?usp=sharing).
