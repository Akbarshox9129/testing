# Searching Algorithms
# Linear Search
def linearsearch(nums,x):
    for i in range(len(nums)):
        if nums[i]==x:
            return i
    return -1
son=int(input("son= "))
numbers=[5,3,7,1,9,6,4,8,2]
if linearsearch(numbers,son)!=-1:
    print(son,linearsearch(numbers,son),"-indexda joylashgan")
else:
    print("Topilmadi")
# Binary Search
def binarysearch(nums,l,r,x):
    if r>=l:
        mid=l+(r-l)//2
        if nums[mid]==x:
            return mid
        elif nums[mid]<x:
            return binarysearch(nums,mid+1,r,x)
        else:
            return binarysearch(nums,l,mid-1,x)
    else:
        return "Topilmadi"
n=int(input("n= "))
ls=[1,8,9,12,52,145,689,1000]
print(binarysearch(ls,0,len(ls)-1,n))