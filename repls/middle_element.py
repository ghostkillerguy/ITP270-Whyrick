#defining the function middle_element and giving it 1 parameter
def middle_element(lst):
  #if statement to see if there are an even or odd number of elements in the list lst
  if len(lst) % 2 == 0:
#if above answer is even we are setting the return value to be the avg of the middle two numbers of the list
    #finding the two middle numbers
    leftNum = len(lst) / 2
    rightNum = leftNum + 1
    #returning the avg
    return (lst[int(leftNum) - 1] + lst[int(rightNum) - 1]) / 2
  else:
    #if above answer is odd we are setting the return to be the middle element in the list
    midNum = (round(len(lst) / 2)) - 1
    return lst[midNum]
#printing the correct return based off of these elements listed below
print(middle_element([5,2,-10,-4,4,5]))
