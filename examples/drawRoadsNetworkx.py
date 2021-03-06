#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created in February 2017 in ComplexCity Lab

@author: github.com/fpfaende

what it does
clean roads graph created from osm file

parameters
graph

how it works
1 - remove nodes without geographic informations (latitude or longitude)
2 - remove self referencing edges (loop on itself)
3 - remove isolated nodes (degree is 0 )

return
graph minus alone or non-conform nodes

'''
import sys
sys.path.insert(0, '/Users/fabien/Documents/workspace/github/policosm')

import matplotlib.pyplot as plt
import colorlover as cl

from policosm.extractors.roadsGraph import *
import policosm.geoNetworks as pocogeo
from policosm.functions import *

colors = [ (r/255,v/255,b/255) for r,v,b in cl.to_numeric(cl.scales['9']['seq']['Purples'])]
edgeWidth=[1,1,1,1,1,2,2,3,3]

def drawRoads(G, edgeColorAttribute='level', edgeColorScale=9, nodeColorAttribute=None, nodeColorScale=None):
		
	pos={}
	for n in G.nodes():
		pos[n] = (G.node[n]['longitude'],G.node[n]['latitude'])

	# nodes
	nx.draw_networkx_nodes(G,pos,node_size=0,alpha=0.8,color=colors[-1])

	# edges
	for i in range(0,9):
		selectedEdges = [(u,v) for (u,v,d) in G.edges(data=True) if d['level'] == i]
		selectedColors = [colors[i] for e in selectedEdges]
		nx.draw_networkx_edges(G,pos,edgelist=selectedEdges,width=edgeWidth[i],edge_color=selectedColors)
	
	plt.show()


if __name__ == "__main__":
	# filename = '/Volumes/Fabien/Research/cities-pictures/data/France/1-pbf/74173.pbf'
	filename = '/Users/fabien/Documents/workspace/SHU-communities/data/shanghai.pbf'
	graph = roadsGraph(filename)
	print (nx.info(graph))
	
	graph = pocogeo.clean(graph)
	print (nx.info(graph))


	graph = pocogeo.simplify_with_rdp(graph)
	print (nx.info(graph))
	nx.write_gexf(graph, '/Users/fabien/Documents/workspace/SHU-communities/data/shanghai.gexf')
	# plotRoadsGraphPNG(graph,filename.split('/')[-1].split('.')[-2])
	#drawRoads(graph)




