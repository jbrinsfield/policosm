#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created in February 2017 in ComplexCity Lab

@author: github.com/fpfaende

what it does
	extract a graph from

parameters
	graph

how it works

return


"""
import sys

sys.path.insert(0, '/Users/fabien/Documents/workspace/github/policosm')

from policosm.classes.roads import Roads


def roadsGraph(filename):
    roads = Roads()
    roads.apply_file(filename)
    # osmParser = OSMParser(concurrency=4, coords_callback=roads.nodes, ways_callback=roads.edges)
    # osmParser.parse(filename)
    return roads.getGraph()


if __name__ == "__main__":
    graph = roadsGraph('../../tests/data/minimal-example.osm')
    assert len(graph.nodes()) == 5
    assert len(graph.edges()) == 4
