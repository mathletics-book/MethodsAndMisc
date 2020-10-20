##################################################################### 
### Extracting GameIDs for each game				  ###
# Author: Konstantinos Pelechrinis                                  #
# Date: 07/26/2017                                                  #
# Input argument: The month for which we are looking to get data    #
##################################################################### 

#!/bin/sh

curl https://www.basketball-reference.com/leagues/NBA_2017_games-$1.html > $1
cat $1 | grep "<tr ><th scope=\"row\" class=\"left \" data-stat=\"date_game\" csk=\"" >> games2016
python getGameIDs.py

for file in `ls 2016-17/*`; do
	python htmlparse.py $file
done 
 
