#Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
#Example: biggie_size([-1, 3, 5, -5]) returns that same list, 
#but whose values are now [-1, "big", "big", -5]

def biggie_size(li):
    for x in range (len(li)):
        if li[x]>0:
            li[x]="big"
    return li
print(biggie_size([-1,3,5,-5]))



#Count Positives - Given a list of numbers, create a function to replace the last value 
#with the number of positive values. (Note that zero is not considered to be a positive number).
#Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
#Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it

def count_positives(li):
    count =0
    for value in li:
        if value>0:
            count+=1
    li[len(li)-1] =count 
    return li
print(count_positives([-1,1,1,1]))
print(count_positives([1,6,-4,-2,-7,-2]))



#Sum Total - Create a function that takes a list and returns the sum of all the values in the list.
#Example: sum_total([1,2,3,4]) should return 10
#Example: sum_total([6,3,-2]) should return 7

def sum_total(li):
    sum=0
    for y in li:
        sum+=y
    return sum
print(sum_total([1,2,3,4]))
print(sum_total([6,3,-2]))



#Average - Create a function that takes a list and returns the average of all the values.x
#Example: average([1,2,3,4]) should return 2.5

def average(li):
    sum_ =0
    for z in li:
        sum_ = sum_ + z

    avg = sum_ / len(li)
    return avg

print(average([1,2,3,4]))
#It keeps on returning 2 I dont know why thou I have tried several ways.



#Length - Create a function that takes a list and returns the length of the list.
#Example: length([37,2,1,-9]) should return 4
#Example: length([]) should return 0

def length(li):
    return len(li)
print(length([37,2,1,-9]))
print(length([]))



#Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. 
#If the list is empty, have the function return False.
#Example: minimum([37,2,1,-9]) should return -9
#Example: minimum([]) should return False

def min(li):
    if len(li)<0:
        return False
    min_num = li[0]
    for a in li:
        if a<min_num:
            min_num = a
    return min_num

print(min([37,2,1,-9]))




#Maximum - Create a function that takes a list and returns the maximum value in the list. 
#If the list is empty, have the function return False.
#Example: maximum([37,2,1,-9]) should return 37
#Example: maximum([]) should return False

def max(li):
    if len(li)<0:
        return False
    max_num = li[0]
    for b in li:
        if b>max_num:
            max_num = b
    return max_num

print(max([37,2,1,-9]))



#Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal,
#average, minimum, maximum and length of the list.
#Example: ultimate_analysis([37,2,1,-9]) should return 
#{'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }

def ultimate_analysis(li):
    my_dictonary = {'sumTotal_': 0, 'average_': 0, 'minimum_': li[0], 'maximum_': li[0], 'length_': len(li)}
    for value_ in li:
        if my_dictonary['minimum_']>value_:
            my_dictonary['minimum_'] = value_

        if my_dictonary['maximum_']<value_:
            my_dictonary['maximum_'] = value_

        my_dictonary['sumTotal_']+= value_
        my_dictonary['average_']=my_dictonary['sumTotal_']/len(li)
    return my_dictonary

print(ultimate_analysis([37,2,1,-9]))



#Reverse List - Create a function that takes a list and return that list with values reversed. 
#Do this without creating a second list. 
#(This challenge is known to appear during basic technical interviews.)
#Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]

def reverse_list(li):
    for c in range((len(li)-1)/2):
        temp = li[c]
        li[c] = li[len(li)-1-c]
        li[len(li)-1-c] = temp
    return li

print(reverse_list([37,2,1,-9]))