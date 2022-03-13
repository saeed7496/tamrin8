
def add_complexnumber(x,y):
    result={}
    result['real']=x['real']+y['real']
    result['imaginary']=x['imaginary']+y['imaginary']
    return result

def mull_complexnumber(x,y):
    result={}
    result['real']=(x['real']*y['real'])-(x['imaginary']*y['imaginary'])
    result['imaginary']=(x['real']*y['imaginary'])+(x['imaginary']*y['real'])
    return result

def minus_complexnumber(x,y):
    result={}
    result['real']=x['real']-y['real']
    result['imaginary']=x['imaginary']-y['imaginary']    
    return result

a={'real':-4, 'imaginary':5}
b={'real':3, 'imaginary':2}
x=minus_complexnumber(a,b)
print(x)






