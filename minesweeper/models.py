from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Game(models.Model):
	'''
		Stores current state of the minesweeper game.

		row - row size of board
		col - column size of board
		numCount - 
		state - [*] how did we arrive at 100000
	'''
	row = models.IntegerField()
	col = models.IntegerField()
	numCount = models.IntegerField()
	viewedNumCount = models.IntegerField()
	clickCount = models.IntegerField()
	state = models.CharField(max_length=100000)