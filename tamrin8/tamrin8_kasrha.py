
a={'s':2, 'm':5}
b={'s':4, 'm':9}

def mull(a,b):
    result={}
    result['s']=a['s']*b['s']
    result['m']=a['m']*b['m']
    return result

def add(a,b):
    result={}
    result['s']=a['s']*b['m']+a['m']*b['s']
    result['m']=a['m']*b['m']
    return result

def minus(a,b):
    result={}
    result['s']=a['s']*b['m']-a['m']*b['s']
    result['m']=a['m']*b['m']
    return result

def division(a,b):
    result={}
    result['s']=a['s']*b['m']
    result['m']=a['m']*b['s']
    return result
   

c=division(a,b)
print(c['s'],'/',c['m'])












