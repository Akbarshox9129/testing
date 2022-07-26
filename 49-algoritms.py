# Sorting Algorithms
# Bubble Sort
def bubblesort(nums):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[j]<nums[i]:
                nums[i],nums[j]=nums[j],nums[i]
# Selection Sort
def selectionsort(nums):
    for i in range(len(nums)):
        min=i
        for j in range(min+1,len(nums)):
            if nums[j]<nums[min]:
                min=j
        nums[min],nums[i]=nums[i],nums[min]
sonlar=[4,9,1,6,7,3,4]
#bubblesort(sonlar)
#selectionsort(sonlar)
#insertionsort(sonlar)
print(sonlar)