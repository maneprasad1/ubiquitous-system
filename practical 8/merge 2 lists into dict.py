from sys import stdin, stdout, setrecursionlimit
from this import d
def inlist(): return list(map(str, stdin.readline().strip().split()))
print("This is a python program to merge 2 lists into a dictionary ")
print("-------------------------------------------------------------------------------------\n")
print("Enter the list containing keys")
key=inlist()
print("Enter the list containing vlaues: ")
val=inlist()
if len(key)==len(val):
    for i in len(key):
        d[key[i]]=val[i]
else:
    print("Number of keys are not equal to number of values")