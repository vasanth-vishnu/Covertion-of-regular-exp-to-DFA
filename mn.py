n=input()
c=0
a=[]
b=[]
l=0
us=[]
for j in range(len(n)):
    if((ord(n[j])>=97 and ord(n[j])<=122) or (ord(n[j])>=48 and ord(n[j])<=57) ) :
        c+=1
        a.append(n[j])
        us.append(n[j])
        b.append(c)
    else:
        l=0
        a.append(n[j])
        b.append(l)
k=list(zip(a,b))

m1=[]
for i in range(len(k)):
    if(k[i][0]=='('):
        d1=i
    elif(k[i][0]==')'):
        d2=i
    elif(k[i][0]=='*'):
        d3=i
     
def star():
    def v1(co):
        for i in range(co):
            m1.append(m2)
    m2=[]
    co=0     
    if(k[0][0]!='('):
        for i in range(len(k)-1):
           if(k[i+1][0]!='('):
              q9=[]
              q9.append(k[i+1][1])
              m1.append(q9)
           elif(k[i+1][0]=='('):
              for i in range(d1,d2):
                  if(ord(k[i][0])>=97 and ord(k[i][0])<=122 or (ord(k[i][0])>=48 and ord(k[i][0])<=57)):
                      co+=1
                      m2.append(k[i][1])
              
              m2.append(m2[len(m2)-1]+1)
              m1.append(m2)
              break
        v1(co)
        v2=[]
        if(k[len(k)-1][0]!='*'):
            for i in range(d3+1,len(k)):
                v2.append(k[i])
        if(len(v2)==1):
            q1=[]
            q1.append(v2[0][1]+1)
            m1.append(q1)
        else:
            for i in range(len(v2)-1):
                q2=[]
                q2.append(v2[i+1][1])
                m1.append(q2)
            if(len(v2)!=0):
                q3=[]
                q3.append(v2[len(v2)-1][1]+1)
                m1.append(q3)
    else:
        for i in range(len(k)-1):
           if(ord(k[i][0])>=97 and ord(k[i][0])<=122 or (ord(k[i][0])>=48 and ord(k[i][0])<=57)):
                co+=1
                m2.append(k[i][1])
           if(k[i][0]==')'):
                break
        m2.append(m2[len(m2)-1]+1)
        v1(co)
        v2=[]
        if(k[len(k)-1][0]!='*'):
            for i in range(d3+1,len(k)):
                v2.append(k[i])
        if(len(v2)==1):
            q4=[]
            q4.append(v2[0][1]+1)
            m1.append(q4)
        else:
            for i in range(len(v2)-1):
                q2=[]
                q2.append(v2[i+1][1])
                m1.append(q2)
            q5=[]
            q5.append(v2[len(v2)-1][1]+1)
            m1.append(q5)
    
    n1=[]  
    print("follow table")
    print("    ","var","     ","node","     ","followpos")
    for i in range(len(us)):
        n1.append(i+1)
        print("      ",us[i],"      ",i+1,"       ",m1[i])
        dy=i
    print("      ","#","      ",dy+2,"       ","null")
    x1=list(zip(n1,us))
    x2=list(zip(us,m1))
    vf=[]
    for i in range(len(us)):
        if us[i] not in vf:
            vf.append(us[i])
    def bon(mr,m1,x1,x2):
        mx=[]
        abc=[]
        for j in range(len(mr)):
            for y in range(len(m1)):
                if(mr[j]==x1[y][0]):
                    mx.append(x2[y])
        for i in range(len(mx)):
            abc.append(mx[i][0])
        ab1=set(abc)
        ab2=list(ab1)
        ab2.sort()
        kq1=[]
        ab3=[]
        for i in range(len(ab2)):
            kq=[]
           
            for j in range(len(mx)):
                if(mx[j][0]==ab2[i]):
                    for k in range(len(mx[j][1])):
                        kq.append(mx[j][1][k])
                    if ab2[i] not in ab3:
                        ab3.append(ab2[i])
                  
            kq1.append(kq)
        h2=list(zip(ab3,kq1))
        return h2
    fgin=[]
    for j in range(len(m1)):
        fgin.append(m1[j])
        
        
    for i in range(len(m1)):
        ki=bon(m1[i],m1,x1,x2)
        def mk(ki):
            for i in range(len(ki)):
                if ki[i][1] not in fgin:
                    fgin.append(ki[i][1])
                    ki1=bon(ki[i][1],m1,x1,x2)
                    mk(ki1)
        mk(ki)
    fgin1=[]
    for i in range(len(fgin)):
        if fgin[i] not in fgin1:
            fgin1.append(fgin[i])
    for i in range(len(fgin1)):
        print(fgin1[i],"==",bon(fgin1[i],m1,x1,x2))

                        
def withoutstar():
    m2=[]
    def v1(co):
        for i in range(co):
            q18=[]
            q18.append(m2[len(m2)-1]+1)
            m1.append(q18)
  
    co=0     
    if(k[0][0]!='('):
        for i in range(len(k)-1):
           if(k[i+1][0]!='('):
              q10=[]
              q10.append(k[i+1][1])
              m1.append(q10)
           elif(k[i+1][0]=='('):
              for i in range(d1,d2):
                  if(ord(k[i][0])>=97 and ord(k[i][0])<=122 or (ord(k[i][0])>=48 and ord(k[i][0])<=57)):
                      co+=1
                      m2.append(k[i][1])
              m1.append(m2)
              break
        v1(co)
        v2=[]
        if(k[len(k)-1][0]!=')'):
            for i in range(d2+1,len(k)):
                v2.append(k[i])
        if(len(v2)==1):
            q11=[]
            q11.append(v2[0][1]+1)
            m1.append(q11)
        else:
            for i in range(len(v2)-1):
                q12=[]
                q12.append(v2[i+1][1])
                m1.append(q12)
            if(len(v2)!=0):
                q13=[]
                q13.append(v2[len(v2)-1][1]+1)
                m1.append(q13)
    else:
        for i in range(len(k)-1):
           if(ord(k[i][0])>=97 and ord(k[i][0])<=122 or (ord(k[i][0])>=48 and ord(k[i][0])<=57)):
                co+=1
                m2.append(k[i][1])
           if(k[i][0]==')'):
                break
        v1(co)
        v2=[]
        if(k[len(k)-1][0]!=')'):
            for i in range(d2+1,len(k)):
                v2.append(k[i])
        if(len(v2)==1):
            q14=[]
            q14.append(v2[0][1]+1)
            m1.append(q14)
        else:
            for i in range(len(v2)-1):
                q15=[]
                q15.append(v2[i+1][1])
                m1.append(q15)
            if(len(v2)!=0):
                q16=[]
                q16.append(v2[len(v2)-1][1]+1)
                m1.append(q16)
    n1=[]    
    print("follow table")
    print("    ","var","     ","node","     ","followpos")
    for i in range(len(us)):
        n1.append(i+1)
        print("      ",us[i],"      ",i+1,"       ",m1[i])
        dy=i
    print("      ","#","      ",dy+2,"       ","null")
    x1=list(zip(n1,us))
    x2=list(zip(us,m1))
    vf=[]
    for i in range(len(us)):
        if us[i] not in vf:
            vf.append(us[i])
    def bon(mr,m1,x1,x2):
        mx=[]
        abc=[]
        for j in range(len(mr)):
            for y in range(len(m1)):
                if(mr[j]==x1[y][0]):
                    mx.append(x2[y])
        for i in range(len(mx)):
            abc.append(mx[i][0])
        ab1=set(abc)
        ab2=list(ab1)
        ab2.sort()
        kq1=[]
        ab3=[]
        for i in range(len(ab2)):
            kq=[]
           
            for j in range(len(mx)):
                if(mx[j][0]==ab2[i]):
                    for k in range(len(mx[j][1])):
                        kq.append(mx[j][1][k])
                    if ab2[i] not in ab3:
                        ab3.append(ab2[i])
                  
            kq1.append(kq)
        h2=list(zip(ab3,kq1))
        return h2
    fgin=[]
    for j in range(len(m1)):
        fgin.append(m1[j])
        
        
    for i in range(len(m1)):
        ki=bon(m1[i],m1,x1,x2)
        def mk(ki):
            for i in range(len(ki)):
                if ki[i][1] not in fgin:
                    fgin.append(ki[i][1])
                    ki1=bon(ki[i][1],m1,x1,x2)
                    mk(ki1)
        mk(ki)
    fgin1=[]
    for i in range(len(fgin)):
        if fgin[i] not in fgin1:
            fgin1.append(fgin[i])
    for i in range(len(fgin1)):
        print(fgin1[i],"==",bon(fgin1[i],m1,x1,x2))

c2=0
for i in range(len(n)):
    if(n[i]=='*'):
        c2+=1
if(c2>0):
    star()
else:
    withoutstar()