# missionaries-and-cannibals

## Problem Description
3 Missionaries and 3 Cannibals are on one side of a river, along with a boat
that can hold one or two passengers.

Find a way to transport everyone to the other side of the river, without ever
leaving a group of Missionaries in one place outnumbered by the Cannibals in
that place.

## Usage

## Dependencies
* <a href="https://www.python.org/downloads/release/python-360/">Python 3.6</a>

## Problem Formulation

### Initial State
Three cannibals and three missionaries are on the left island along with the boat.

The state of the program can be represented by:
*An array L of size 2, where L[0] is the number of missionaries on the left island and L[1] is the number of cannibals on the left island
*An array R of size 2, where R[0] is the number of missionaries on the right island and R[1] is the number of cannibals on the right island.
*An integer B where B=0 indicates the boat is on the left island and B=1 indicates the boat is on the right island.

### Actions
The actions available to the agent are based upon the current position of the boat and the distribution of cannibals and missionaries. The agent’s subset of available actions are determined based off the application of the problem’s current state.The agent’s action include more cannibals/missionaries than available on the current side and cannot perform an action that would result in a state where the missionaries are outnumbered.
1. Move boat across the river with 1 missionary, 1 cannibal
2. Move boat across the river with 2 missionaries
3. Move boat across the river with 2 cannibals
4. Move boat across the river with 1 missionary
5. Move boat across the river with 1 cannibal

### Transition Model
The boat that carries the missionaries and or cannibals from one island to the other.

The next state is determined by the current state: (# of cannibals/missionaries on left, # of cannibals/missionaries on right, and the position of the boat in) and the action (combination of passengers to take).

### Goal Test
The goal of the problem is to move all missionaries and cannibals from the left island to the right island. We can check whether or not a given state is the goal state by checking the amount of missionaries and cannibals on the left side. If there are 0 missionaries and 0 cannibals on the left island, then they must be on the right island therefore fulfilling the requirements of the problem.

We can verify this by checking n(L[0]) = 0 and n(L[1]) = 0

### Path Cost
The act of moving the boat = 1, path cost is # of times boat moves across the river, therefore the path cost is equal to the number of actions from the initial state to the goal state.



