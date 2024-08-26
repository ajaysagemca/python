class employee():
    def __init__(self,dep,posi,salary):
        self.dep=dep
        self.posi=posi
        self.salary=salary
    def show(self):
        print('dep=',self.dep)
        print('posi=',self.posi)
        print('salary=',self.salary)

class information(employee):
    name='ajay'
    age='22'
    def __init__(self):
        super().__init__('engineer','posi','50,0000')
        print('name=',self.name)
        print('age',self.age)

obj=information()#'engineer','software engineer','50,0000')
obj.show()

print('zero part')
print()
class car():
    def start(self):
        print('start car')
    def stop(self):
        print('stop car')
class furtune():
    def __init__(self):
        print('hello car')

class maruti(car,furtune):
    def maruticar(self):
        type1='electric'
        print(type1)

obj=maruti()
obj.start()
obj.stop()
obj.maruticar()
print()

print('second part')
class changename():
    name='ajay'
    def cname(self,name):
        self.name=name
        print(name)

obj=changename()
obj.cname('hemant')
print('name of class changename and variable name is:-----',changename.name)
print()

print('third part')
class Student():
    def __init__(self,math,chem,phy):
        self.math=math
        self.chem=chem
        self.phy=phy
        #self.percentage= str((self.math + self.chem + self.phy)/3)+ '%'
       # print(self.percentage)
   # @property
    def calculat_per(self):
        return str((self.math + self.chem + self.phy) / 3) + '%'

obj=Student(90,99,88)
#print(obj.percentage)
p=obj.phy=99
print(p)
print(obj.calculat_per())


print()
print('fourth part')
class Student():
    def __init__(self,math,chem,phy):
        self.math=math
        self.chem=chem
        self.phy=phy
        self.percentage= str((self.math + self.chem + self.phy)/3)+ '%'
        print(self.percentage)
obj=Student(90,99,88)
print(obj.percentage)
p=obj.phy=99
print(p)

p=[1,2,3]+[4,5,6]
print(p)
print(1+3j)

print()
print('fift part')
class complex():
    def __init__(self,real,image):
        self.real=real
        self.image=image
    def shownumber(self):
        print (self.real,'i+',self.image,'j')

obj=complex(1,2)
obj.shownumber()

print()
print('six part')
class emplooyee():
    def __init__(self,dep,salary,posi ):
        self.dep=dep
        self.salary=salary
        self.posi=posi
    def shwd(self):
        print('dep =',self.dep)
        print('salary =',self.salary)
        print('posi =',self.posi)

class information(emplooyee):
    name='ajay'
    age='22'
    def __init__(self):
        super().__init__('engineer','60,000','software engineer')
        print('name:-',self.name)
        print('age:-',self.age)


#obj=emplooyee('engineer','60,000','software engineer')
obj=information()#'engineer')#,'60,000','software engineer')
obj.shwd()

print()
print('seven part')
class order():
    def __init__(self,item,price):
        self.item=item
        self.price=price
    def __gt__(self,obj1):
        return obj.item > obj1.price

obj=order('pen','10')
obj1=order('pensil','5')
print(obj > obj1)

print()
print('eight part')
class forloop():
    def loop(self):
        a=[]
        for b in range(1,50):
            a.append(b)
        print(a)
    def listcom(self):
        x=[y for y in range(1,30) if y%2==0]
        print(x)
obj=forloop()
obj.loop()
obj.listcom()



















