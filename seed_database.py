"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system('dropdb ratings')
# More code will go here

##START HERE: https://fellowship.hackbrightacademy.com/materials/pt9g/exercises/ratings-v2/index-2.html 
# "Seed the Database"