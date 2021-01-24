"""

You are given a set A and N other sets.
Your job is to find whether set A is a strict superset of each of the N sets.

Print True, if A is a strict superset of each of the N sets. Otherwise, print False.

A strict superset has at least one element that does not exist in its subset.

"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
A = set(map(int,input().split()))
n = int(input())
result = False
for i in range(n):
    B = set(map(int,input().split()))
    if(B.issubset(A) and (len(A) != len(B))):
        result = True
    else:
        result = False
        break
print(result)
        
