a=[1,2,3,7,5]
pal=True
s=0
for i in a:
    if i>1:
        pal=True
        
        for x in range(2,int(i**0.5)+1):
            if i% x==0:
                pal=False
                break
        if pal:
            s=s+i
print(s)
            
        
