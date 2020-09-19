from heapq import heappush, heappop, heapify
def connectSticks(sticks):
	"""
	General idea: use heap, pop 2 cheapest sticks from the top, sum up and push the sum back. Until there is a single element in the heap
	"""
	heapify(sticks)
	final_cost = 0
	while len(sticks) > 0:
		cur_cost = heappop(sticks) + heappop(sticks)
		final_cost += cur_cost
		heappush(sticks, cur_cost)
	return final_cost