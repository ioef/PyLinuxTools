#!/usr/bin/env python
'''
Creation of the word count Linux utility in python
'''
import sys


def printStats(filename):
    #data = sys.stdin.read()
    with open(filename,'r') as data:
        data = data.read()
        chars = len(data)
        words = len(data.split())
        lines = len(data.split('\n'))

    print "\nThe file includes {0} characters, {1} words and {2} lines".format(chars,words,lines)


def main():
    if len(sys.argv) !=2:
         print "Wrong number of arguments. Exiting..."
         print "usage: wc.py filename"
         sys.exit(1)

    printStats(sys.argv[1])

if __name__ =='__main__':
    main()
