import glob
import networkx as nx
import pandas as pd

path = "network/"

#files *res* include the results for the corresponding week, with the first column being the losing team and the second team the winner
#files *net* include the edgelist of the win-loss network -- From | To | weight -- up to and including the corresponding week 

year = [2009, 2010, 2011, 2012, 2013, 2014, 2015]
# we need to build a network first
week = [3,4,5,6,7,8,9,10,11,12,13,14,15,16]

correct_preds = 0
wrong_preds = 0

for y in year:
    for w in week:
        # read the network up to that week and make predictions for the upcoming week
        G=nx.read_edgelist(path+"reg_"+str(y)+"net_week"+str(w)+".txt", nodetype=str, data=(('weight',float),),create_using= nx.DiGraph())
        pr = nx.pagerank(G, alpha=0.85)
        # predict for week w+1
        res = pd.read_csv(path+"reg_"+str(y)+"res_week"+str(w+1)+".txt",sep=" ",header=None)
        for g in range(len(res)):
            if pr[res[0].iloc[g]] > pr[res[1].iloc[g]]:
                correct_preds+=1
            else:
                wrong_preds+=1
