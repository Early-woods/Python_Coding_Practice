'''
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]

'''

def spiralOrder(a):
    #Setting Boundaries for the given matrix
    m = len(a)
    n = len(a[0])
    
    t = 0
    b = m-1
    l = 0
    r = n - 1
    dr = 0
    
    """ 
    t: top of the matrix
    b: botom of the matrix
    l: left of the matrix
    r: Right of yhe matrix
    dr: printing direction
    m: Number of rows in the matrix
    n: Number of Columns in the matrix
    
    """
    
    while (t <= b and l <=r):
        
        if dr ==0:
            for i in range(l,r+1):
                print (a[t][i], end=" ")
            t +=1
            dr = 1
            
        elif dr ==1:
            for i in range(t,b+1):
                print (a[i][r], end=" ")
            r -=1 
            dr = 2
            
        elif dr ==2:
            for i in range(r,l-1,-1):
                print (a[b][i], end=" ")
            b -=1
            dr = 3
            
        elif dr ==3:
            for i in range(b,t-1,-1):
                print (a[i][l], end=" ")
            l +=1
            dr = 0


matrix = [
    [1,2,3,4,5,6,7],
    [8,9,0,1,2,3,4],
    [5,6,7,8,9,0,1],
    [2,3,4,5,6,7,8],
    [9,0,1,2,3,4,5]
    ]
print(spiralOrder(matrix))