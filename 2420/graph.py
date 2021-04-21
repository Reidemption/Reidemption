class Queue:
    def __init__(self):
        self.A = []

    def Enqueue(self, x):
        self.A.append(x)

    def Dequeue(self):
        if len(self.A) > 0:
            return self.A.pop(0)
        return False

    def IsEmpty(self):
        if len(self.A) > 0:
            return False
        return True

class Graph:
    def __init__(self, vectors): #
        self.Neighbors = []
        for i in range(vectors):
            self.Neighbors.append([])

    def AddEdge(self, From, To): #
        self.Neighbors[From].append(To)

    def FindPath(self, Start, End): # #Breadth First Search Algorithm
        queue = Queue()
        From = []
        for i in range(len(self.Neighbors)):
            From.append(-1)
        From[Start] = Start
        queue.Enqueue(Start)
        while not queue.IsEmpty():
            current_vertex = queue.Dequeue()
            if current_vertex == End:
                path = []
                path.append(current_vertex)
                #build path and return it
            for n in range(len(self.Neighbors[current_vertex])): #for each neighbor n of c:
                if n != -1: #if n has not been visitited
                    n = current_vertex #mark n as visited from current_vertex.
                    queue.Enqueue(n) #enqueue n
            
        return None

def main():
    with open('graph.txt','r') as graph:
        graphlist = graph.readlines()
        vertexes = graphlist[0]
        g = Graph(vertexes)
        edges = graphlist[1]
        for i in range(edges):
            x = graphlist[i+2]
            x.split(' ')
            g.AddEdge(int(x[0]),int(x[1]))
        testcases = graphlist[len(edges)+1]
        for i in range(testcases):
            y = graphlist[i+4]
            y.split(' ')
            g.FindPath(int(y[0]),int(y[1]))