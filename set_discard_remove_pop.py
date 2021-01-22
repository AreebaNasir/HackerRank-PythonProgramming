"""

Task
You have a non-empty set s and you have to execute N commands given in N lines.
Commands will be pop, remove and discard.

Input Format
First line contains integer n, number of elements in set. 
Second line contains space separated elements of set s. All elements are non-negative integers, less than or equal to 9. 
Third line contains integer N, number of commands.
Next N lines contains pop, remove and discard commands.

Constraints
0<n<20 
0<N<20

Output Format
Print sum of elements of set 's' in output.

Sample Input
9
1 2 3 4 5 6 7 8 9
10
pop
remove 9
discard 9
discard 8
remove 7
pop 
discard 6
remove 5
pop 
discard 5

Sample Output
4

"""

n = int(input())
s = set(map(int, input().split()))
N = int(input())
for i in range(N):
    #command will be a list storing both the command and the value
    #to remove from the set
    command = input().split()
    if(command[0] == "pop"):
        s.pop()
    elif(command[0] == "remove"):
        s.remove(int(command[1]))
    elif(command[0] == "discard"):
        s.discard(int(command[1]))
print(sum(s))
