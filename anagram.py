__author__ = 'weiweiduan'
from itertools import *
import sys

openfiles = open('anagram_out.txt',"w")

outcome = []
outcome_sort = []

def swap(string, a, b):
    temp = string[a]
    string[a] = string[b]
    string[b] = temp

def permutation(string, begin, end):
    if(begin == end):
        tmpt = ''
        for i in string:
            tmpt += i
        outcome.append(tmpt)
    else:
        for i in range(begin,end):
            swap(string, begin, i)
            permutation(string, begin+1, end)
            swap(string, begin, i)

string = sys.argv[1]
inputstr = []
for i in string:
    inputstr.append(i)
permutation(inputstr,0,len(string))

# for i in outcome:
#     print i

outcome_sort = sorted(outcome)


for i in outcome_sort:
    # print i
    openfiles.writelines(i)
    openfiles.writelines('\n')

# '''compare the outcome to the solution'''
# inputfiles = open('sol.txt','r')
#
# sol = []
# for line in inputfiles:
#     sol.append(line[0:6])
#
# for i in range(len(sol)):
#     if sol[i] != outcome_sort[i]:
#         print "wrong"
#         print sol[i], outcome_sort[i]
#         break
# print len(outcome_sort),len(sol)