num = [1,2,3,4,5,8,3,5,1,1,2,3,4,5,7,8,1,2,3,4,6,6,6,5,1,7]
#      a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z   

def minify(num : str):
    if len(num) > 1:
        count = 0
        for i in num:
            count += int(i)
        return minify(str(count))
    else:
        return str(num)



with open("namelist.txt") as namelist:
    for name in  namelist:
        textcount = 0
        for i in name.strip().upper():
            if i == " ":
                continue
            textcount += num[ord(i) - 65]
        print(f"=========== {name.strip().upper()} - {minify(str(textcount))} ===============")





