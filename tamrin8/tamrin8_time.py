
t1={'h':4,'m':34,'s':28}
t2={'h':1,'m':4,'s':56}
def add_time(t1,t2):
    t_final={}
    t_final['h']=t1['h']+t2['h']
    t_final['m']=t1['m']+t2['m']
    t_final['s']=t1['s']+t2['s']
    if t_final['s']>=60:
        t_final['s']-=60
        t_final['m']+=1
    elif t_final['m']>=60:
        t_final['m']-=60
        t_final['h']+=1
    return t_final

def minus(t1,t2):
    t_final={}
    t_final['h']=t1['h']-t2['h']
    t_final['m']=t1['m']-t2['m']
    t_final['s']=t1['s']-t2['s']
    if t_final['s']<=0:
        t_final['s']+=60
        t_final['m']-=1
    elif t_final['m']<=0:
        t_final['m']+=60
        t_final['h']-=1
    return t_final

def change2second(t):
    result=t['h']*3600+t['m']*60+t['s']
    return result

def change2time():
    result={}
    second=int(input('pleaz inter second: '))
    result['h']=second//3600
    result['m']=(second%3600)//60
    result['s']=(second%3600)%60
    return result

c=change2time()
print(c)



