## Входное задание на курс coderiders.academy

---

### Руководство по запуску

#### Требования к системе: 
- ОС Linux
- Java 11+

#### Задание 1. Сортировки, сортировочки
```
  cd task01
  mvn package
  java -jar target/task01-0.1.jar
  mvn clean
```

#### Зaдание 2. Базы данных
```
  cd task02
  mvn package
  java -jar target/task02-0.1.jar
  mvn clean
```

#### Зaдание 3. Лифты
```
  cd task03
  mvn package
  java -jar target/task03-0.1.jar [-h][-v]
  mvn clean
```

Использование с ключами:

```
  -h - получение помощи
```

Пример запуска:

```
    user in ~/IdeaProjects/coderiders_academy_testcase/task03 on dev-java-task03 ● ● λ java -jar target/task03-0.1.jar -h
    Usage: java -jar task03-0.1.jar OPTIONS
    Options category 'main':
      --[no]verbose [-v] (a boolean; default: "false")
        be more verbose
    
    Options category 'misc':
      --[no]help [-h] (a boolean; default: "false")
        show this help message and exit
```

```
  -v - включение логиования и больше отладочной информации
```

Пример запуска:

```
    user in ~/IdeaProjects/coderiders_academy_testcase/task03 on dev-java-task03 ● ● λ java -jar target/task03-0.1.jar -v
    
    2021-09-19 20:53:09,337 [main] INFO  - Verbosity level increased.
    2021-09-19 20:53:09,339 [main] INFO  - Creating application...
    2021-09-19 20:53:09,339 [main] INFO  - Application.constructor
    2021-09-19 20:53:09,340 [main] INFO  - Building default building.
    2021-09-19 20:53:09,346 [main] DEBUG - Elevators in building: [Elevator(id=0, floor=1), Elevator(id=1, floor=1), Elevator(id=2, floor=1)]
    2021-09-19 20:53:09,346 [main] INFO  - Building init done. The building has 9 floors and 3 elevators.
    2021-09-19 20:53:09,346 [main] INFO  - Getting building state...
    2021-09-19 20:53:09,353 [main] DEBUG - Building created as: Building(floor_count=9, elevator_count=3, elevators_state=[[0, 1], [1, 1], [2, 1]])
    2021-09-19 20:53:09,353 [main] INFO  - Application.init done.
    2021-09-19 20:53:09,354 [main] INFO  - Creating application... done
    2021-09-19 20:53:09,354 [main] INFO  - Running application...
    2021-09-19 20:53:09,354 [main] INFO  - Enter floor number or * for exit.
    
    ...
```
