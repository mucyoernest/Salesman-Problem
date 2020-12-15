

from itertools import permutations
from sys import maxsize 

#number of edges
n = 5

def routeFinder(matrix_graph, s): 

    #vertex
	v = [] 
	for i in range(n): 
		if i != s: 
			v.append(i) 

	shortest_path = maxsize 
	next_permutation=permutations(v)
	for i in next_permutation:

		cost = 0
		k = s 
		for j in i: 
			cost += matrix_graph[k][j] 
			k = j 
		cost += matrix_graph[k][s] 

		shortest_path = min(shortest_path, cost) 
		
	return shortest_path 

if __name__ == "__main__": 

	# matrix representation of graph 
	
	matrix_graph = [[0, 10, 8, 9, 7],
          [10, 0, 10, 5, 6],
          [8, 10, 0, 8, 9],
          [9, 5, 8, 0, 6],
          [7, 6, 9, 6, 0]] 
	s = 0
	print(routeFinder(matrix_graph, s))
