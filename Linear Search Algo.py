a = ['t', 'u', 't', 'o', 'r', 'i', 'a', 'l']
x='o'
def linearsearch(a,x):
    for i in range(len(a)):
        if a[i]==x:
            return i
    return -1
print("element found at index " +str(linearsearch(a,x)))