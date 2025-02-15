import heapq
import sys

# Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    print("Sorted array:", arr)

# Prim's MST
def prim_mst(graph):
    num_vertices = len(graph)
    selected = [False] * num_vertices
    mst_matrix = [[0] * num_vertices for _ in range(num_vertices)]
    selected[0] = True
    num_edges = 0

    while num_edges < num_vertices - 1:
        min_edge = sys.maxsize
        u, v = -1, -1
        for i in range(num_vertices):
            if selected[i]:
                for j in range(num_vertices):
                    if not selected[j] and graph[i][j]:
                        if min_edge > graph[i][j]:
                            min_edge = graph[i][j]
                            u, v = i, j

        if u != -1 and v != -1:
            selected[v] = True
            mst_matrix[u][v] = graph[u][v]
            mst_matrix[v][u] = graph[v][u]
            num_edges += 1

    print("MST Matrix:")
    for row in mst_matrix:
        print(" ".join(map(str, row)))

# Kruskal's MST
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []  # List to store edges (w, u, v)

    def add_edge(self, u, v, w):
        self.graph.append((w, u, v))

    def find(self, parent, i):
        if parent[i] == i:
            return i
        else:
            parent[i] = self.find(parent, parent[i])
            return parent[i]

    def union(self, parent, rank, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)

        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

    def kruskal_mst(self):
        mst = []
        self.graph.sort()  # Sort edges by weight
        parent = list(range(self.V))
        rank = [0] * self.V

        for w, u, v in self.graph:
            root_u = self.find(parent, u)
            root_v = self.find(parent, v)
            if root_u != root_v:
                mst.append((u, v, w))
                self.union(parent, rank, root_u, root_v)

        total_weight = sum(w for _, _, w in mst)
        print("\nEdges in the MST:", mst)
        print("Total weight of the MST:", total_weight)

# Dijkstra's Algorithm
class DijkstraGraph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, w):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))

    def dijkstra(self, start, end):
        distances = {vertex: float('infinity') for vertex in self.graph}
        distances[start] = 0
        priority_queue = [(0, start)]
        predecessors = {vertex: None for vertex in self.graph}

        while priority_queue:
            current_distance, u = heapq.heappop(priority_queue)
            if current_distance > distances[u]:
                continue

            for neighbor, weight in self.graph[u]:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    predecessors[neighbor] = u
                    heapq.heappush(priority_queue, (distance, neighbor))

        path = []
        current = end
        while current is not None:
            path.append(current)
            current = predecessors[current]
        path.reverse()

        if distances[end] == float('infinity'):
            return "No path", []
        return distances[end], path

# Menu system
def menu():
    while True:
        print("\nMain Menu:")
        print("1. Sorting and MST Algorithms")
        print("2. Dijkstra's Algorithm")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            sub_menu()
        elif choice == '2':
            g = DijkstraGraph()
            num_edges = int(input("Enter number of edges: "))
            for _ in range(num_edges):
                u, v, w = input("Enter edge (u v w): ").split()
                g.add_edge(u, v, float(w))
            start = input("Enter starting vertex: ")
            end = input("Enter ending vertex: ")
            distance, path = g.dijkstra(start, end)
            if distance == "No path":
                print(f"No path from {start} to {end}")
            else:
                print(f"Shortest path from {start} to {end} is {distance}")
                print("Path:", " -> ".join(path))
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

# Sub-menu for Sorting and MST algorithms
def sub_menu():
    while True:
        print("\nSorting and MST Menu:")
        print("1. Selection Sort")
        print("2. Prim's MST")
        print("3. Kruskal's MST")
        print("4. Back to Main Menu")
        choice = input("Enter your choice: ")
        if choice == '1':
            arr = list(map(int, input("Enter numbers separated by space: ").split()))
            selection_sort(arr)
        elif choice == '2':
            num_vertices = int(input("Enter number of vertices: "))
            graph = [[0] * num_vertices for _ in range(num_vertices)]
            num_edges = int(input("Enter number of edges: "))
            for _ in range(num_edges):
                u, v, weight = map(int, input("Enter edge (u v weight): ").split())
                graph[u][v] = weight
                graph[v][u] = weight
            prim_mst(graph)
        elif choice == '3':
            vertices = int(input("Enter number of vertices: "))
            g = Graph(vertices)
            num_edges = int(input("Enter number of edges: "))
            for _ in range(num_edges):
                u, v, w = map(int, input("Enter edge (u v w): ").split())
                g.add_edge(u, v, w)
            g.kruskal_mst()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
