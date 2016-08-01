from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Game(models.Model):
	'''
		Stores current state of the minesweeper game.

		row - row size of board
		col - column size of board
		numCount - number of cells that has a digit on their face
		viewedNumCount - number of cells with digit that has been visited. Acts as boundary on BFS.
		clickCount - numer of (valid) clicks user made to reach current cell. (Used for score.)
		state - is json blob that captures current state of the board. The state is representated as 3D list.
				the 3rd dimention has 2 elements. [cellContent, visited]
				
				cellContent can be one of
				'B'	- denotes bomb
				[0-9] - a number on that cell
				' ' - empty cell

				visited says if the above cell is visited or visible to the user.
				
	'''
	row = models.IntegerField()
	col = models.IntegerField()
	numCount = models.IntegerField()
	viewedNumCount = models.IntegerField()
	clickCount = models.IntegerField()
	state = models.CharField(max_length=100000)
