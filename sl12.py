class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.edges = []
    
    def add_edge(self, u, v, w):
        # Ensure vertices are within valid range
        if u >= self.V or v >= self.V or u < 0 or v < 0:
            print(f"Error: Invalid edge ({u}, {v})")
            return
        self.edges.append((w, u, v))
    
    def find(self, parent, i):
        if parent[i] == i:
            return i
        else:
            parent[i] = self.find(parent, parent[i])
            return parent[i]
    
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1
    
    def kruskal(self):
        result = []
        i = 0  # Initial index of sorted edges
        e = 0  # Initial count of edges in MST
        
        # Sort all edges in non-decreasing order of their weight
        self.edges.sort()
        
        parent = list(range(self.V))
        rank = [0] * self.V
        
        while e < self.V - 1:
            if i >= len(self.edges):
                print("Error: Index i is out of range for edges list.")
                break
            (w, u, v) = self.edges[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e = e + 1
                result.append((u, v, w))
                self.union(parent, rank, x, y)
        
        # Print the resulting MST
        if result:
            print("Edges in MST:")
            for u, v, w in result:
                print(f"{u} -- {v} == {w}")
        else:
            print("No edges in MST")

def main():
    import sys
    
    
    # Get the number of vertices
    vertices = int(input("Enter number of vertices: "))
    
    g = Graph(vertices)
    
    while True:
        # Display menu
        print("\nMenu:")
        print("1. Add Edge")
        print("2. Find MST using Kruskal's Algorithm")
        print("3. Find MST using Prim's Algorithm")
        print("4. Exit")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            u = int(input("Enter start vertex: "))
            v = int(input("Enter end vertex: "))
            w = int(input("Enter weight of the edge: "))
            g.add_edge(u, v, w)
        
        elif choice == 2:
            g.kruskal()
        
        elif choice == 3:
            print("Prim's Algorithm not implemented yet.")
        
        elif choice == 4:
            print("Exiting.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

