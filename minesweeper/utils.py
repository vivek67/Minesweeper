import json
from .constants import dx, dy

def isvalid(x, y, row, col):
	'''
		Check if a cell falls inside the board
	'''
	return x >= 0 and x < row and y >= 0 and y < col


def floodFill(startRow, startCol, game):
	'''
		Returns list of cells that needs to be opened up [[row, col, its-value] ... ]
	'''
	queue = [[startRow, startCol]]
	curState = json.loads(game.state)
	curState[startRow][startCol][1] = True 
	
	viewedNumCount = game.viewedNumCount
	openCells = []

	while len(queue) != 0:
		u, v = queue[0]
		queue = queue[1:]
		openCells.append([u, v, curState[u][v][0]])

		if str(curState[u][v][0]).isdigit():
			viewedNumCount += 1

		if curState[u][v][0] == ' ':
			for i in xrange(8):
				x = u + dx[i]
				y = v + dy[i]
				if isvalid(x, y, game.row, game.col) and curState[x][y][1] == False:
					if curState[x][y][0] != 'B':
						curState[x][y][1] = True
						queue.append([x, y])

	return (openCells, curState, viewedNumCount)