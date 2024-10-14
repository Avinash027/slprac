from collections import defaultdict
print("Avnash Shinde Roll - 20, TE - A, AI & DS Dept\n");

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    def addEdge(self, u, v):
        self.graph[u].append(v)
        print(f"Edge added from {u} to {v}")
    def DFS(self, edge, visited=None):
        if visited is None:
            visited = []
        visited.append(edge)
        for adj in self.graph[edge]:
            if adj not in visited:
                self.DFS(adj, visited)
        return visited
    def BFS(self, edge):
        visited = []
        queue = []
        queue.append(edge)
        visited.append(edge)

        while len(queue):
            s = queue.pop(0)
            for i in self.graph[s]:
                if i not in visited:
                    queue.append(i)
                    visited.append(i)
        return visited

def menu():
    g = Graph()
    while True:
        print("\nMenu:")
        print("1. Add Edge")
        print("2. Perform DFS")
        print("3. Perform BFS")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            u = int(input("Enter source node: "))
            v = int(input("Enter destination node: "))
            g.addEdge(u, v)
        elif choice == '2':
            start_node = int(input("Enter starting node for DFS: "))
            print(f"DFS traversal: {g.DFS(start_node)}")
        elif choice == '3':
            start_node = int(input("Enter starting node for BFS: "))
            print(f"BFS traversal: {g.BFS(start_node)}")
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please choose again.")

# Call the menu function
if __name__ == "__main__":
    menu()

