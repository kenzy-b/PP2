def histogram(arr):
    for i in arr:
        print("*"*i)
n=input("Numbers: ")
mylist=list(map(int,n.split()))
histogram(mylist)