""" multiplication-table.py 
Author: Jack Meehan 
Credit: To find how to get rid newline: https://gist.github.com/marcoscastro/dd176ac2b59441895369 
Assignment: Write and submit a Python program that 
prints a multiplication table."""

width = int(input('Width of multiplication table: ')) 
height = int(input('Height of multiplication table: ')) 

for i in range(1, height+1):
    for j in range(1, width+1):
        print(i*j , end=" ")