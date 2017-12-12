'''
3 Missionaries and 3 Cannibals are on one side of a river, along with a boat that can hold one or two passengers.

Find a way to transport everyone to the other side of the river, without ever
leaving a group of Missionaries in one place outnumbered by the Cannibals in
that place.

Joshua Nguyen
Brett Behring
Donovan Prehn
'''
from copy import deepcopy

POSSIBLE_ACTIONS = [[1,1],[0,2],[2,0],[0,1],[1,0]]

class State():
	
	def __init__(self, left, boat, right):
		self.left=left;
		self.boat = boat;
		self.right=right;
		self.prev = None
		
	def __str__(self):
		return("({},{}) - ({},{}) - {}".format(self.left[0],self.left[1],self.right[0],self.right[1],self.boat))
	
	def isValidState(self):	
		#If the cannibals outnumber missionaries on the left or right side
		if(0 < self.left[0] < self.left[1] or 0 < self.right[0] < self.right[1]):
			return False	
		
		#ensure that more M/C are not transported than exist on a side
		if(self.left[0]<0 or self.left[1]<0 or self.right[0]<0 or self.right[1]<0):
			return False
		
		return True

	def __eq__(self, other):
		return (self.left[0]==other.left[0] and self.left[1] == other.left[1] and self.right[0]==other.right[0] and self.right[1]==other.right[1] and self.boat==other.boat)
		
	def __hash__(self):
		return hash((self.left[0],self.left[1],self.boat,self.right[0],self.right[1]))
	
	def __str__(self):
		return("({},{}) - ({},{}) - {}".format(self.left[0],self.left[1],self.right[0],self.right[1],self.boat))
	
	def isGoalState(self):
		#if all the cannibals and missionaries have been transported across along with the boat
		return(self.left[0]==0 and self.left[1]==0)

def nextStates(current):
	nodes=[]

	for action in POSSIBLE_ACTIONS:
		
		nextState = deepcopy(current)
		nextState.prev=current
		
		#boat will be on the opposite side
		nextState.boat = 1-current.boat
		
		#Moving from left to right
		if(current.boat==0):

			#Right population increases
			nextState.right[0]+=action[0]
			nextState.right[1]+=action[1]
			
			#Left population decreases
			nextState.left[0]-=action[0]
			nextState.left[1]-=action[1]
		
		#Moving from right to left
		elif(current.boat==1):
			
			#Right population decreases
			nextState.right[0]-=action[0]
			nextState.right[1]-=action[1]
			
			#Left population increases
			nextState.left[0]+=action[0]
			nextState.left[1]+=action[1]
		
		if nextState.isValidState():
			nodes.append(nextState)

	return nodes
	
def bfs(root):
	
	if root.isGoalState():
		return root
	
	visited = set()
	queue = [root]

	while queue:
		state = queue.pop()
		if state.isGoalState():
			return state
		
		visited.add(state)
		
		for child in nextStates(state):
			if child in visited:
				continue

			if child not in queue:
				queue.append(child)

def main():
	initial_state = State([3,3],0,[0,0])
	state = bfs(initial_state)
	
	#build path
	path=[]
	while state:
		path.append(state)
		state = state.prev
		
	
	#reverse path
	path=path[::-1]
	
	#print state change
	for state in path:
		if state.boat:
			print("""{:3} |         b| {:3}\n{:3} |          | {:3}""".format("c"*state.left[1], "c"*state.right[1], "m"*state.left[0], "m"*state.right[0]))
		else:
			print("""{:3} |b         | {:3}\n{:3} |          | {:3}""".format("c"*state.left[1], "c"*state.right[1], "m"*state.left[0], "m"*state.right[0]))
		print("--"*10)

if __name__ == "__main__":
	main()