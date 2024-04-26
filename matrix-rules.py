



"""

write a function which calculates the input array passes at least one rule as below.



1-horizontal: each row is identical.



2-vertical: each column is identical.



3-diagonal left: each item is identical to the one on its upper left or bottom right.



4-diagonal right: each item is identical to the one on its upper right or bottom left.







Example: 



Input:AA BB CC



Output: pass 







AA



BB



CC



// This is part of horizontal







Input:AB AB AB



Output: pass 







AB



AB



AB



// This is part of vertical







Input: ABC CAB BCA



Output: pass



// This is part of diagonal left 







Input: ABC BCA KAB 



Output: fail



// none of rules passes.



"""


# code here

def HorizontalCheck(arr, row=0):
    if row + 1 != len(arr):
        for i in range(len(arr[row])):
            if arr[row][i] != arr[row][0]:
                return False
        return HorizontalCheck(arr, row + 1)
    
    return True

def VerticalCheck(arr, col):
    if col != len(arr[0]):
        for i in range(len(arr)):
            if arr[i][col] != arr[0][col]:
                return False
        return VerticalCheck(arr, col+1)
    return True

def  DiagonalLeft(arr, row):
    if row + 1 > len(arr):
        return True
    elif row == 0:
        for i in range(len(arr[row])):
            if i + 1 >= len(arr[row]):
                continue
            else:
                if arr[row][i] != arr[row + 1][i + 1]:
                    return False
        return DiagonalLeft(arr, row + 1)
    elif row + 1 == len(arr):
        for i in range(len(arr[row])):
            if i == 0:
                continue
            else:
                if arr[row][i] != arr[row - 1][i - 1]:
                    return False
        return DiagonalLeft(arr, row + 1)
    else:
        for i in range(len(arr[row])):
            if i == 0:
                if arr[row][i] != arr[row + 1][i + 1]:
                    return False
            elif i + 1 >= len(arr[row]):
                if arr[row][i] != arr[row - 1][i - 1]:
                    return False
            else:
                if arr[row][i] != arr[row - 1][i - 1] or arr[row][i] != arr[row + 1][i + 1]:
                    return False
        return DiagonalLeft(arr, row + 1)
    
def  DiagonalRight(arr, row):
    if row + 1 > len(arr):
        return True
    # first row
    elif row == 0:
        for i in range(len(arr[row])):
            if i == 0:
                continue
            else:
                if arr[row][i] != arr[row + 1][i - 1]:
                    return False
        return DiagonalRight(arr, row + 1)
    # last row
    elif row + 1 == len(arr):
        for i in range(len(arr[row])):
            if i + 1 >= len(arr[row]):
                continue
            else:
                if arr[row][i] != arr[row - 1][i + 1]:
                    return False
        return DiagonalRight(arr, row + 1)
    # middle row
    else:
        for i in range(len(arr[row])):
            if i == 0:
                if arr[row][i] != arr[row - 1][i + 1]:
                    return False
            elif i + 1 >= len(arr[row]):
                if arr[row][i] != arr[row + 1][i - 1]:
                    return False
            else:
                if arr[row][i] != arr[row - 1][i + 1] or arr[row][i] != arr[row + 1][i - 1]:
                    return False
        return DiagonalRight(arr, row + 1)

    
verCheck = VerticalCheck([["A","A"],["A","B"],["A","B"]], 0)
horCheck = HorizontalCheck([["A","A"],["B","B"],["C","C"]], 0)
dLeftCheck = DiagonalLeft([["A","B","C"],["C","A","B"],["B","C","A"]], 0)
dRightCheck = DiagonalRight([["A","B","C"],["B","C","A"],["C","A","B"]], 0)
print(dRightCheck)
if verCheck or horCheck or dLeftCheck:
    print("passed")
else:
    print("fail")




"""def ArrayCheck(arr):
    horCheck = True
    verCheck = True
    leftCheck = True
    for i in range(len(arr)):
        print(arr[i])
        #horizontal check
        for ver in arr:
            if arr[i] != ver:
                horCheck = False
        for j in range(len(arr[i])):
            # vertical check
            for col in arr:
                if arr[i][j] != col[j]:
                    verCheck = False
            # diagonal left check
            if j == 0:
                if i < len(arr):  
                    if arr[i][j] !=  arr[i + 1][j + 1]:
                        leftCheck = False
            elif j == len(arr[i]):
                if i > 0:
                    if arr[i][j] != arr[i - 1][j - 1]:
                        leftCheck = False
            else:
                print(i)   
                if i == 0:
                    if arr[i][j] != arr[i+1][j+1]:
                        leftCheck = False
                elif i == len(arr):
                    if arr[i][j] != arr[i-1][j-1]:
                        leftCheck = False
                else:
                    if arr[i][j] != arr[i - 1][j - 1] or arr[i][j] != arr[i+1][j+1]:
                        leftCheck = False
            
a = [["A","B","C"],["C","A","A"],["B","C","A"]]
ArrayCheck(["ABC","CAB","BCA"])

                


ABC
CAB
BCA

"""

'''
PLEASE MAKE SURE THAT YOUR OUTPUT MATCHES EXACTLY WITH THE DESIRED OUTPUT
PLEASE MAKE SURE TO CLEAN IRREVELANT ITEMS FROM YOUR CODE OUTPUT

If the question requires parameters, please read them from sys.argv, for example
print ('Argument List:', str(sys.argv))

If an integer parameter is expected; do not forget to to parse accordingly,
for example: a = int(sys.argv[1])

If a collection of parameters are used, please read them from arguments list, parse them and use
placing them in the correct collection

You can use input box below to manually set custom inputs for your program,enter the
inputs by leaving a space between them, like 1 2 3...
'''
