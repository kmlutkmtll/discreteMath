import matplotlib.pyplot as plt
import networkx as nx

drawGraph = nx.DiGraph()

# set = [1,2,3]
# pairs = [[1,1],[2,2],[3,3],[1,3],[3,2],[1,2]]

while True:

    sizePairs = int(input("How many elements in pairs : "))
    sizeSet = int(input("How mant elements in set : "))

    if (sizePairs == -1 or sizeSet == -1):
        break

    set = []
    for x in range(sizeSet):
        set.append([])
        set[x] = int(input("Enter {}. element in set: ".format(x)))

    pairs = []
    for i in range(sizePairs):
        pairs.append([])
        for j in range(2):
            pairs[i].append([])
            pairs[i][j] = int(input("Enter {},{}. element : ".format(i,j)))


    def isReflexive(pairs):
        # We check this func : 2D array in first loop we access elements.For example [1,1].
        # If every elements of set(1,2,3) they repeat each other ([1,1],[2,2]) is reflexive
        for i in set:
            if [i,i] in pairs:
                continue
            else:
                return False
        return True


    def isAntisymmetric(pairs):
        # We return false if one of the 2 elements of the pairs is swapped and exists in this set.[[1,2],[2,1]]
        # Because it must be antisymmetric
        # We check every pair
        for i in pairs:
            if i[0] == i[1]:
                continue
            elif [i[1],i[0]] in pairs:
                return False
        return True

    def isTransitive(pairs):
        for i in pairs:
            if i[0] == i[1]:
                continue
            # we check if they start with i[1](2.elements -> [[a,b]]  so b  if let's see if it starts with the next b
            # -> [[a,b], [b,c]]
            for j in pairs:
                if j[0] == i[1]:
                    if[i[0],j[1]] in pairs:
                        continue
                    else:
                        return False
        return True

    if isReflexive(pairs) == True:
        print("Reflexive")
    else:
        print("Not reflexive")

    if isAntisymmetric(pairs) == True:
        print("Antisymmetric")
    else:
        print("Not antisymmetric")

    if isTransitive(pairs) == True:
        print("Transitive")
    else:
        print("Not transitive")


    if (isReflexive(pairs) and isAntisymmetric(pairs) and isTransitive(pairs) == True): # POset if all provide
        for i in set:
            for j in pairs:
                if i == j[0] or i == j[1]:
                    drawGraph.add_edge(i,str(j[0]) + "," + str(j[1]))

        pos = nx.spring_layout(drawGraph)
        nx.draw_networkx(drawGraph, pos)
        plt.axis("off"), plt.title("POset"), plt.show()
    else:
        print("Not POset")


