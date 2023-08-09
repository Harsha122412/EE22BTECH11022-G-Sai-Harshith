import numpy as np
import math

#midpoint function
def midpoint(x,y):
	return (x+y)/2

#direction
def dir_vec(A,B):
	return B-A

#given coordinates A,B,C
A=np.array([1,-1])
B=np.array([-4,6])
C=np.array([-3,-5])

#Given D,E,F are midpoints of BC,CA,AB
D=midpoint(B,C)
E=midpoint(C,A)
F=midpoint(A,B)

#intersection of lines
def line_intersect(B,E,C,F):
	m1 = dir_vec(B,E)
	m2 = dir_vec(C,F)
	p = np.zeros(2) 
	p[0] = (m2[0]*B[0]-m1[0]*C[0])/(m2[0]-m1[0])
	p[1] = (m2[1]*B[1]-m1[1]*C[1])/(m2[1]-m1[1])
	return p
G=line_intersect(B,E,C,F)
print("("+str(G[0])+","+str(G[1])+")")
