## The input Grid:
# Here you can change or put whatever kind of grids you want
G= [[0,1,0,1,0,0], [0,1,0,0,0,0], [0,0,0,0,1,0], [0,0,0,1,1,0]]

# ======================================================================================
# ======================================================================================

## The Graph:
# This part takes the given grid and creates a graph from it
def Graph(G):
    Graph = {}
    # Creating the Keys and its children, whether they are possible or not
    for row in range(len(G)):
        for column in range(len(G[row])):
            # Filtering the keys that has a block in the Grid
            if G[row][column] == 1:
                pass
            # Conditions for corner positions
            if row-1 < 0 and column-1 < 0:
                Graph[(row,column)] = [(row+1,column),(row,column+1)]
            elif row+1 == len(G) and column+1 == len(G[row]):
                Graph[(row,column)] = [(row-1,column),(row,column-1)]
            elif row-1 < 0 and column+1 == len(G[row]):
                Graph[(row,column)] = [(row,column-1),(row+1,column)]
            elif row+1 == len(G) and column-1 < 0:
                Graph[(row,column)] = [(row,column+1),(row-1,column)]
            # Conditions for Grid's sides positions
            elif row-1 < 0 and column > 0:
                Graph[(row,column)] = [(row+1,column),(row,column+1),(row,column-1)]
            elif row > 0 and column-1 < 0:
                Graph[(row,column)] = [(row+1,column),(row,column+1),(row-1,column)]
            elif row+1 == len(G):
                Graph[(row,column)] = [(row-1,column),(row,column+1),(row,column-1)]
            elif column+1 == len(G[row]):
                Graph[(row,column)] = [(row+1,column),(row-1,column),(row,column-1)]
            # The rest of positions in Grid
            else:
                Graph[(row,column)] = [(row+1,column),(row,column+1),(row-1,column),(row,column-1)]
    # Filtering the Keys which are located in blocks in the Grid
    for key in list(Graph):
        if G[key[0]][key[1]] == 1:
            del Graph[key]
    # Filtering the Values which are located in blocks in the Grid
    for List in Graph.values():
        for pair in list(List):
            if G[pair[0]][pair[1]] == 1:
                List.remove(pair)
    print(Graph)
    return Graph

# ======================================================================================
# ======================================================================================

## The Bredth-First-Search Algorithm & Finding the shortest Path:
def BFS(Graph):
    Start, End = (0,0), (len(G)-1,len(G[0])-1)
    try:
        ### Exploring part of the Grid:
        Distance, Stalk, Queue, Path = {}, {}, [], []
        for node in Graph:
            Distance[node] = None
        Distance[Start] = 0
        Queue.append(Start)
        while len(Queue) != 0:
            Node = Queue.pop(0)
            for Child in Graph[Node]:
                if Distance[Child] == None:
                    Queue.append(Child)
                    Distance[Child] = 1
                    Stalk[Child] = Node
        ### Finding the Shortest Path part:
        Path.append(End)
        while Path[-1] != Start:
            Path.append(Stalk[Path[-1]])
        Path.reverse()
        print("(Minimum Steps: %d, Path: %s)" % ((len(Path)-1),str(Path)))
    except:
        if G[Start[0]][Start[1]] == 1:
            print("Error: Your Starting Point is from a Block !!")
            print("(Minimum Steps: 0, Path: No Valid Path)")
        else:
            print("(Minimum Steps: 0, Path: No Valid Path)")

# ======================================================================================
# ======================================================================================

## Running part of the code:
def find_shortest_path(G):
    BFS(Graph(G))
find_shortest_path(G)
