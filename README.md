# BMA Simulator
### Программа для расчета линейной сложности по алгоритму Berlekamp Массей для послеовательности случайных бит заданной длины. 

## Запуск программы происходит при помощи команды:
    python main.py

## Вводные данные и описание работы
### Вводные данные: 
С клавиавтуры вводиться длина случайной последовательности бит, которая будет сгенерирована
### Описание работы:
Программа последовательно увеличивает размер последовательности до достижения заданной длины. \
На каждой итерации перед увеличением длины программа находит линейную сложность уже имеющейся последовательности. \
После достиения заданной длины последовательности отрисовываеться график зависимости количества элементов последовательности \
от линейной сложности по алгоритму BMA. 