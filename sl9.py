import heapq

def a_star(graph, start, goal, heuristic):
    # Priority queue (open set)
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}

    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0

    f_score = {node: float('inf') for node in graph}
    f_score[start] = heuristic(start)

    while open_set:
        # Get the node with the lowest fScore
        _, current = heapq.heappop(open_set)

        if current == goal:
            return reconstruct_path(came_from, current)
        for neighbor, cost in graph[current].items():
            tentative_g_score = g_score[current] + cost
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristic(neighbor)
                heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return None  

def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    return path[::-1]  # Reverse the path

def heuristic(node):
    h = {  'A': 7, 'B': 6, 'C': 2, 'D': 12, 'E': 3, 'F': 0 }
    return h[node]

graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'A': 1, 'D': 1, 'E': 5},
    'C': {'A': 3, 'F': 2},
    'D': {'B': 1},
    'E': {'B': 5, 'F': 1},
    'F': {'C': 2, 'E': 1}
}

def menu():
    while True:
        print("\nMenu:")
        print("1. Find path using A*")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            start = input("Enter start node: ").strip().upper()
            goal = input("Enter goal node: ").strip().upper()

            if start not in graph or goal not in graph:
                print("Invalid nodes! Please enter nodes from the graph.")
            else:
                path = a_star(graph, start, goal, heuristic)
                if path:
                    print(f"Path from {start} to {goal}: " + " -> ".join(path))
                else:
                    print(f"No path found from {start} to {goal}.")
        elif choice == '2':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    print("Avinash Shinde, 20, TE - A")
    menu()
