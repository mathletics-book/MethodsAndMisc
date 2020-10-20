##################################################################### 
### Extracting the four factors from a basketball-reference page  ###
# Author: Konstantinos Pelechrinis                                  #
# Date: 07/26/2017                                                  #
# Input files: a basketball-reference.com game page		    #
##################################################################### 

import bs4
import sys

# read the HTML file
html = open(sys.argv[1]).read()

# extract the body of the HTML file
body=bs4.BeautifulSoup(html, "lxml").find('body')

body_children = body.findChildren()


# find the four factors -- they are enclosded in tfoot tag
# the following is the list with the box score stats
# 0: basic box score visiting team
# 1: advanced box score visiting team
# 2: basic box score home team
# 3: advanced box score home team
t = body_children[0].findAll('tfoot')

visiting = ""
home = "" 

visiting = visiting+str(t[0].findAll('td')[-2].text)+","+str(t[1].findAll('td')[2].text)+","+str(t[1].findAll('td')[4].text)+","+str(t[1].findAll('td')[5].text)+","+str(t[1].findAll('td')[5].text)
home = home+str(t[2].findAll('td')[-2].text)+","+str(t[3].findAll('td')[2].text)+","+str(t[3].findAll('td')[4].text)+","+str(t[3].findAll('td')[5].text)+","+str(t[3].findAll('td')[5].text)

# find the teams that area playing
t = body_children[0].findAll('table')

v = t[0].findAll('caption')[0]
h = t[2].findAll('caption')[0]

vteam = str(v).split('(')[0].rstrip().split('>')[1]
hteam = str(h).split('(')[0].rstrip().split('>')[1]


visiting = vteam+","+visiting
home = hteam+","+home

print visiting, home
