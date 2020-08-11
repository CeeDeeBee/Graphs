verticies = {}


def earliest_ancestor(ancestors, starting_node):
    # initialize graph
    for edge in ancestors:
        if edge[1] in verticies.keys():
            verticies[edge[1]].append(edge[0])
        else:
            verticies[edge[1]] = [edge[0]]

    # sort sets to ensure lowest vertex is always checked first
    for key in verticies.keys():
        verticies[key].sort()

    def dfs(current_vertex):
        # verticies with no ancestors will not be in the verticies dict
        if current_vertex not in verticies.keys():
            if current_vertex == starting_node:
                return -1

            return current_vertex

        for n in verticies[current_vertex]:
            return dfs(n)

    return dfs(starting_node)
