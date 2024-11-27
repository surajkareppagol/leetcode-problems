# Author: Suraj K

from typing import *

# ATTEMPT 1 - 502 / 758

# class Node:
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next


# class Solution:
#     def findChampion(self, n: int, edges: List[List[int]]) -> int:
#         if len(edges) == 0 and n > 1:
#             return -1

#         if n == 1:
#             return 0
#         elif n == -1:
#             return -1

#         # Create Nodes and Graph
#         nodes = [i for i in range(n)]

#         dag_nodes = []

#         for i in range(n):
#             dag_nodes.append(Node(i))

#         for i, j in edges:
#             dag_nodes[i].next = dag_nodes[j]

#         # print(nodes)

#         # Traverse all nodes
#         for i in range(n):
#             # If not in nodes continue
#             if i not in nodes:
#                 continue
#             else:
#                 # Start traversing from a node
#                 dag_node = dag_nodes[i]
#                 if dag_node.next:
#                     dag_node = dag_node.next
#                 else:
#                     continue

#                 while True:
#                     if dag_node.data in nodes:
#                         nodes.remove(dag_node.data)

#                     if dag_node.next:
#                         dag_node = dag_node.next
#                     else:
#                         break

#         # print(nodes)

#         if len(nodes) == 1:
#             return nodes[0]
#         else:
#             return -1

# ATTEMPT 2


class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        dag = {}

        for i in range(n):
            dag[i] = []

        for i, j in edges:
            dag[j].append(i)

        # print(dag)
        stronger = 0
        champion = -1

        for i in range(n):
            if not dag[i]:
                stronger += 1
                champion = i

        if stronger == 1:
            return champion
        else:
            return -1


s = Solution()

print(s.findChampion(3, [[0, 1], [1, 2]]))
print(s.findChampion(4, [[0, 2], [1, 3], [1, 2]]))
print(s.findChampion(3, [[0, 1]]))
print(s.findChampion(1, []))
print(s.findChampion(3, [[0, 2], [0, 1]]))
