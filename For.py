# for 循环
# for number in range(1,101):
#    print (number)

# d = {'x':1,'y':2,'z':3}
# for key,value in d.items():
#    print(key, 'corresponds to', value)

# names = ['anne','beth','george','damon']
# ages = [12,45,32,102]
# for name, age in zip(names,ages):
#    print (name,"is",age,"years old")

# from math import sqrt
# for n in range(99,80,-1):
#   root = sqrt(n)
#    if root == int(root):
#        print(n)
#        break;
#    else:
#        print ("Didn't find it!")

# girls = ['alice','bernice','clarice']
# boys = ['chris','arnold','bob']
# letterGirls = {}
# for girl in girls:
#    letterGirls.setdefault(girl[0], []).append(girl)
#    print ([b+'+'+g for b in boys for g in letterGirls[b[0]]])

#fibs=[0,1]
#for i in range(8):
#    fibs.append(fibs[-2] + fibs[-1])
#print (fibs)

def fibs(num):
    result = [0,1]
    for i in range(num - 2):
        result.append(result[-2]+result[-1])
    return result
