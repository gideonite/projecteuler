#!/usr/bin/python

def count_lattice_paths(n):
    '''
    size of the grid -> number of paths
    '''

    paths = 0

    for i in xrange(n):
        for j in xrange(n):
            paths+=1

    return paths

print count_lattice_paths(2)
