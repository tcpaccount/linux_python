"""
You are given the array paths, where path[i]=[cityA, cityB] means where
exists a direct path going from cityA to cityB. Return the destination city,
that is, the city without any path outgoing to another city

It's a guarantied that the graph of paths forms a line without any loop,
therefore there will be exactly one destination

Example1:
Input: paths = [["London", "Paris"], ["Paris", "Lima"], ["Lima", "San Paulo"]]
output = "San Paulo""
--------------------------------
Example2:
Input: paths = [["Buffalo", "Baltimore"], ["Toronto", "Buffalo"], ["Baltimore", "Washington"]]
output = "Washington""
"""

def solution(paths):
    possible = []
    impossible = []
    for citya, cityb in paths:
        impossible.append(citya)
        if citya in possible:
            possible.remove(citya)
        if not cityb in impossible:
            possible.append(cityb)

    return possible[0] if len(possible) == 1 else "error"


if __name__ == "__main__":
    sample_paths1 = [["London", "Paris"], ["Paris", "Lima"], ["Lima", "San Paulo"]]
    sample_paths2 = [["Buffalo", "Baltimore"], ["Toronto", "Buffalo"], ["Baltimore", "Washington"]]
    print(solution(sample_paths1))
