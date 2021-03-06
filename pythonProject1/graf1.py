# -*- coding: utf-8 -*-
# Вывод всех путей из источника в пункт назначения.
# Этот код предоставлен Neelam Yadav
# Адаптирован Александром Драгункиным

from collections import defaultdict

# Класс направленного графа, использует представление списка смежности
class Graph:

    def __init__(self, vertices):
        # Нет. вершин
        self.V = vertices

        # словарь по умолчанию для хранения графа
        self.graph = defaultdict(list)

    # функция добавления ребра в граф
    def addEdge(self, u, v):
        self.graph[u].append(v)

    '''Рекурсивная функция для печати всех путей от 'u' до 'd'.
    visit [] отслеживает вершины в текущем пути.
    path [] хранит актуальные вершины, а path_index является текущим
    индексом в path[]'''

    def printAllPathsUtil(self, u, d, visited, path):

        # Пометить текущий узел как посещенный и сохранить в path
        visited[list(self.graph.keys()).index(u)] = True
        path.append(u)

        # Если текущая вершина совпадает с точкой назначения, то
        # print(current path[])
        if u == d:
            print(path)
        else:
            # Если текущая вершина не является пунктом назначения
            # Повторить для всех вершин, смежных с этой вершиной
            for i in self.graph[u]:
                if visited[list(self.graph.keys()).index(i)] == False:
                    self.printAllPathsUtil(i, d, visited, path)

        # Удалить текущую вершину из path[] и пометить ее как непосещенную
        path.pop()
        visited[list(self.graph.keys()).index(u)] = False

    # Печатает все пути от 's' до 'd'
    def printAllPaths(self, s, d):

        # Отметить все вершины как не посещенные
        visited = [False] * (self.V)

        # Создать массив для хранения путей
        path = []

        # Рекурсивный вызов вспомогательной функции печати всех путей
        self.printAllPathsUtil(s, d, visited, path)



# Создаём граф
# graph = {'A': ['B', 'C'],
#          'B': ['C', 'D'],
#          'C': ['D'],
#          'D': ['C'],
#          'E': ['F'],
#          'F': ['C']}
graph = {"A": ["B","D"],
         "B": ["A","C","A1"],
         "C": ["B","F","E"],
         "D": ["A","A1"],
         "A1":["D","E","C1","B1"],
         "E": ["C","A1"],
         "F": ["C","C1"],
         "C1": ["F","A1","D1"],
         "B1": ["A1","D1"],
         "D1": ["B1","C1"] }


g = Graph(len(graph.keys()))
for i, v in graph.items():
    for e in v:
        g.addEdge(i, e)

s = 'A'
d = 'D1'
print ("Ниже приведены все различные пути от {} до {} :".format(s, d))
g.printAllPaths(s, d)