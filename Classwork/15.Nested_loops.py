n = int(input("enter size: "))

# for rows in range(n):
#     for cols in range(n):
#         print("*",end = " ")
#     print()
'''
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
'''

# for rows in range(n):
#     for cols in range(n):
#         print(rows,end = " ")
#     print()
'''
0 0 0 0 0 
1 1 1 1 1
2 2 2 2 2
3 3 3 3 3
4 4 4 4 4
'''

# for rows in range(n):
#     for cols in range(n):
#         print(cols,end = " ")
#     print()

'''
0 1 2 3 4 
0 1 2 3 4
0 1 2 3 4
0 1 2 3 4
0 1 2 3 4
'''

# for rows in range(n):
#     for cols in range(rows + 1):
#         print(rows,end = " ")
#     print()

'''
0
1 1
2 2 2
3 3 3 3
4 4 4 4 4
'''
# for rows in range(n):
#     for cols in range(n - rows):
#         print(rows,end = " ")
#     print()

'''
enter size: 9
0 0 0 0 0 0 0 0 0 
1 1 1 1 1 1 1 1
2 2 2 2 2 2 2
3 3 3 3 3 3
4 4 4 4 4
5 5 5 5
6 6 6
7 7
8
'''

# for rows in range(n):
#     for space in range(n - rows -1):
#         print(" ",end = " ")
#     for cols in range(rows+1):
#         print("*",end = " ")
#     print()

'''
enter size: 5
        * 
      * *
    * * *
  * * * *
* * * * *
'''
# for rows in range(n):
#     for spaces in range(rows):
#         print(" ",end = " ")
#     for cols in range(n - rows):
#         print("*",end = " ")
#     print()

'''
* * * * * * * * * 
  * * * * * * * * 
    * * * * * * * 
      * * * * * * 
        * * * * * 
          * * * * 
            * * * 
              * * 
                * 
'''
# repeteation method
# for rows in range (n):
#   print(" " * rows,end = " " )
#   print("*" * (n-rows),end = " ")
#   print()
'''
enter size: 5
 ***** 
  ****
   ***
    **
     *
'''


# for rows in range(n):
#     for cols in range(rows + 1):
#         print("*",end = " ")
#     print()
# for rows in range(1,n):
#     for cols in range(n - rows):
#         print('*',end = " ")
#     print()

'''
enter size: 5
* 
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
'''

# for rows in range(n):
#   if rows <= n//2:
#     print("*" * (rows+1),end = " ")
#   else:
#     print("*" * (n-rows),end = " ")
#   print()

'''
enter size: 17
* 
**
***
****
*****
******
*******
********
*********
********
*******
******
*****
****
***
**
*
'''

# for rows in range(n):
#   for cols in range(n):
#     if rows == 0 or rows == (n-1) or cols == 0 or cols == n-1:
#       print("*",end= " ")
#     else:
#       print(" ",end = " ")
#   print()
'''
enter size: 10
* * * * * * * * * * 
*                 *
*                 *
*                 *
*                 *
*                 * 
*                 *
*                 *
*                 *
* * * * * * * * * *
'''


# for rows in range(n):
#   for cols in range(n):
#     if rows == 0 or rows == (n-1) or rows == n // 2 or cols == 0 or cols == n-1 or cols == n // 2:
#       print("*",end= " ")
#     else:
#       print(" ",end = " ")
#   print()
'''
  enter size: 19
* * * * * * * * * * * * * * * * * * * 
*                 *                 * 
*                 *                 *
*                 *                 * 
*                 *                 *
*                 *                 * 
*                 *                 *
*                 *                 *
*                 *                 * 
* * * * * * * * * * * * * * * * * * *
*                 *                 * 
*                 *                 *
*                 *                 *
*                 *                 * 
*                 *                 *
*                 *                 *
*                 *                 * 
*                 *                 *
* * * * * * * * * * * * * * * * * * *
'''


# for rows in range(n):
#   for cols in range(n):
#     if rows == 0 or rows == (n-1) or rows + cols == n-1:
#       print("*",end= " ")
#     else:
#       print(" ",end = " ")
#   print()

'''
enter size: 10
* * * * * * * * * * 
                *
              *
            *
          *         
        *
      *             
    *
  *                 
* * * * * * * * * *
'''


# for rows in range(n):
#   for cols in range(n):
#     if rows == cols or rows + cols == n-1:
#       print("*",end= " ")
#     else:
#       print(" ",end = " ")
#   print()
'''
enter size: 9 
*               * 
  *           *
    *       *
      *   *       
        *
      *   *
    *       *
  *           *
*               *
'''

for rows in range(n):
  for cols in range(n - rows):
    print('*',end = " ")
  print()
for rows in range(1,n):
  for cols in range(rows+1):
    print("*",end = " ")
  print()
