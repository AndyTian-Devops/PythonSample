# Chapter Six: Function and parameter
##def lookup(data,lable,name):
##    return data[lable].get(name)
##
##def store(data, full_name):
##    names = full_name.split()
##    if len(names) == 2: names.insert(1,'')
##    labels = 'first', 'middle', 'last'
##for label, name in zip(labels, names):
##    people = lookup(data, label,name)
##    if people:
##        people.append(full_name)
##    else:
##        data[label][name] = [full_name]

def story(**kwds):
    return 'Once upon a time, there was a %(job)s called %(name)s' % kwds

def power(x,y,*others):
    if others:
        print ('Received redundant parameters:',others)
    return pow(x,y)

def interval(start, stop=None,step=1):
    'Imitates range() for step > 0'
    if stop is None:
        start, stop = 0, start
    result = []
    i = start
    while i < stop:
        result.append(i)
        i += step
    return result

print (story(job='king', name = 'Gumby'))
print (story(name='Sir Robin', job='brave knight'))

params = {'job':'lanange', 'name':'Python'}
print (story(**params))

del params['job']
print (story(job='stroke of genius', **params))

print (power(2,3))
print (power(3,2))
print (power(y=3,x=2))

powerparams = (5,)*2
print (power(*powerparams))

print(power(3,3,'Hello, World！'))

print(interval(10))

