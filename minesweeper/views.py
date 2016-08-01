from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Game
import random
import math
import json
from .utils import isvalid, floodFill
from .constants import dx, dy, MAX_ROW_SIZE_REACHED, GAME_WON, BOMB_STEPPED

def index(request):
	return render(request, "minesweeper/index.html", {})

def createGame(request):
	row = int(request.POST["row"])
	col = int(request.POST["col"])

	if row < 0 or row > 100 or col < 0 or col > 100:
		return render(request, "minesweeper/index.html", {'error': MAX_ROW_SIZE_REACHED})
	
	state = [[[' ', False] for x in range(col)] for y in range(row)]
	difficulty = 0.10
	bombCount = int(math.ceil(row*col*difficulty))

	# randomly generate bomb locations
	bombList = []
	random.seed()
	bCnt = 0
	while bCnt < bombCount:
		x = random.randint(0, row-1)
		y = random.randint(0, col-1)
		if state[x][y][0] == 'B':
			continue
		state[x][y][0] = 'B'
		bCnt += 1
		bombList.append([x, y])

	# For each bomb location, increment number arround its cell
	numCount = 0
	for bomb in bombList:
		for i in xrange(8):
			x = bomb[0] + dx[i]
			y = bomb[1] + dy[i]
			if isvalid(x, y, row, col) and state[x][y][0] != 'B':
				if state[x][y][0] == ' ':
					state[x][y][0] = 1
					numCount += 1
				else:
					state[x][y][0] += 1

	game = Game.objects.create(row=row, col=col, state=json.dumps(state), numCount=numCount, viewedNumCount=0, clickCount=0)
	return HttpResponseRedirect("/minesweeper/game/{0}".format(game.id))

def game(request, gameId):
	game = get_object_or_404(Game, pk=gameId)
	curState = json.loads(game.state)

	if game.viewedNumCount == game.numCount:	#game over already, won
		return render(request, "minesweeper/game.html", 
				{'curState' : curState, 'gameId': gameId, 'resultText': GAME_WON, 'gameOver':"true"})

	if game.numCount == -1:		#game over, lost.
		return render(request, "minesweeper/game.html", 
				{'curState' : curState, 'gameId': gameId, 'resultText': BOMB_STEPPED, 'gameOver': "true"})

	
	return render(request, "minesweeper/game.html", {'curState' : curState, 'gameId': gameId, 'gameOver': "false"})

def gameAction(request, gameId, row, col):
	row = int(row)
	col = int(col)

	game = get_object_or_404(Game, pk=gameId)
	if row < 0 or row > game.row or col < 0 or col > game.col:
		return HttpResponseRedirect("/minesweeper/game/{0}".format(game.id))
	
	curState = json.loads(game.state)
	point = curState[row][col]

	if point[1] == True:	# if cell is already visited, return empty viewCell
		result = {
			'gameOver' : False,
			'won' : False,
			'viewCell' : []
		}
		return HttpResponse(json.dumps(result), content_type="application/json")

	if point[0] == 'B':
		openCell = []
		for row in xrange(game.row):
			for col in xrange(game.col):
				openCell.append([row, col, curState[row][col][0]])
				curState[row][col][1] = True
		
		game.state = json.dumps(curState)
		game.numCount = -1	#to denote game over by loss.
		game.save()
		result = {
			'gameOver' : True,
			'won' : False,
			'resultText' : BOMB_STEPPED,
			'viewCell' : openCell
		}
		return HttpResponse(json.dumps(result), content_type="application/json")

	openCell, curState, viewedNumCount = floodFill(row, col, game)

	game.state = json.dumps(curState)
	game.viewedNumCount = viewedNumCount
	game.clickCount += 1
	game.save()

	resultText = ""
	if game.viewedNumCount == game.numCount:
		gameOver = True
		won = True
		resultText = GAME_WON + str(game.row*game.col - game.clickCount)

		openCell = []
		for row in xrange(game.row):
			for col in xrange(game.col):
				openCell.append([row, col, curState[row][col][0]])

	else:
		gameOver = False
		won = False

	result = {
		'gameOver' : gameOver,
		'won' :	won,
		'viewCell' : openCell,
		'resultText' : resultText
	}

	return HttpResponse(json.dumps(result), content_type="application/json")
