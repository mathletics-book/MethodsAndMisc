##################################################################### 
### Download the web pages for the games that you want		  ###
# Author: Konstantinos Pelechrinis                                  #
# Date: 07/26/2017                                                  #
# Input files: a file with the game IDs		                    #
##################################################################### 

import os

f_in = open("games2016","r")

for line in f_in:
	linef = line.rstrip().rsplit("\"")
	gameID = linef[7]
	print gameID
	os.system("curl https://www.basketball-reference.com/boxscores/"+gameID+".html > 2016-17/"+gameID)
