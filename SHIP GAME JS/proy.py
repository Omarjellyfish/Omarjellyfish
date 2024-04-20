
s='11011'
if len(s)==2:
    print(s)

if s[0]=='0':
    case=0
    hm={
        '01':0,
        '010':0}
else:
    case=1
    hm={
        '10':0,
        '101':0}

if case==0:
    hm['01']=s.count('01')
    hm['010']=s.count('010')
    pass
else:
    hm['10']=s.count('10')
    hm['101']=s.count('101')
    pass

print(hm)
if sum(hm.values())==0:
    if case==1:
        print(1)
else:
    print(0)
