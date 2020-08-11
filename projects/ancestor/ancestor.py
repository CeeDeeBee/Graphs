from util import Stack, Queue


def earliest_ancestor(ancestors, starting_node):
    # initialize graph
    verticies = {}
    for edge in ancestors:
        if edge[1] in verticies.keys():
            verticies[edge[1]].append(edge[0])
        else:
            verticies[edge[1]] = [edge[0]]

    # sort sets to ensure lowest vertex is always checked first
    # for key in verticies.keys():
    #     verticies[key].sort()

    # highest_depth = 0
    # deepest_val = 0
    # current_depth = 0
    # s = Stack()
    # s.push(starting_node)

    # while s.size() > 0:
    #     vertex = s.pop()

    #     if vertex not in verticies.keys():
    #         if current_depth > highest_depth:
    #             deepest_val = vertex
    #             highest_depth = current_depth

    #         if vertex == starting_node:
    #             return -1

    #     else:
    #         current_depth += 1
    #         for n in verticies[vertex]:
    #             s.push(n)

    # return deepest_val

    s = Stack()
    s.push([starting_node])
    deepest_path = []

    while s.size() > 0:
        path = s.pop()
        vertex = path[-1]

        if vertex not in verticies.keys():
            if vertex == starting_node:
                return -1

            if len(path) > len(deepest_path):
                deepest_path = path
            elif len(path) == len(deepest_path):
                if vertex < deepest_path[-1]:
                    deepest_path = path
        else:
            for n in verticies[vertex]:
                new_path = path.copy()
                new_path.append(n)
                s.push(new_path)

    return deepest_path[-1]
