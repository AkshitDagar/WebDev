a=list(eval(input("enter the first list:")))
b=list(eval(input("enter the second list:")))
c=[];i=0;j=0;m=len(a);n=len(b)
while i<m and j<n:
    if a[i]<=b[j]:
        c.append(a[i])
        i+=1
    else:
        c.append(b[j])
        j+=1
while i<m:
    c.append(a[i])
    i+=1
while j<n:
    c.append(b[j])
    j+=1
print("numbers in ascending order are:",c)