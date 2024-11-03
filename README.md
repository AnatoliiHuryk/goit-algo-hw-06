# Домашнє завдання: Аналіз та порівняння алгоритмів пошуку шляхів у графі

## Мета
Реалізувати та порівняти алгоритми пошуку в графі (DFS, BFS) та знаходження найкоротшого шляху (Дейкстра) на прикладі транспортної мережі.

## Завдання 1: Моделювання та візуалізація графу
Створено граф із вершин та ребер, що моделюють транспортну мережу. Проведено аналіз основних характеристик:
- **Кількість вершин**: 6
- **Кількість ребер**: 8
- **Ступені вершин**: надані для аналізу кожної вершини

## Завдання 2: Порівняння алгоритмів DFS та BFS
- **DFS (глибина пошуку)**: знаходить шлях, який залежить від порядку обходу та не завжди є найкоротшим.
- **BFS (ширина пошуку)**: знаходить найкоротший шлях за кількістю кроків, що може бути корисним у випадках пошуку мінімальної кількості переходів.

## Завдання 3: Алгоритм Дейкстри
Алгоритм Дейкстри реалізовано для пошуку найкоротшого шляху за вагою ребер. Він успішно знаходить шлях з мінімальною сумарною вагою, що є ефективним для зважених графів.

## Висновки
- **BFS** підходить для знаходження мінімального шляху за кількістю кроків.
- **DFS** може бути корисним у специфічних задачах обходу, але не гарантує мінімальність шляху.
- **Дейкстра** — оптимальний алгоритм для знаходження найкоротшого шляху у зважених графах.

