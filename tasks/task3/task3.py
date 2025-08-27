import math

class check :
    def result_of_eq(self, num):
        var_check1 = 0
        counter =len(parameter_equ)-1
        for iterator in parameter_equ:
            var_check1 += (math.pow(num,counter) * iterator)
            counter -= 1
        return var_check1

    def check_interval(self, start, end):
        var_check1=self.result_of_eq(start)
        var_check2=self.result_of_eq(end)
        if var_check1 * var_check2 < 0:
            return 1
        elif var_check1 == 0:
            print(var_check1, " is the root ")
            return 2
        elif var_check2 == 0:
            print(var_check2, "is the root ")
            return 3
        else:
            return 0
#.................................................................................................................
class equ(check) :
    def midpoint (self , intial , final):
        center= (intial+final)/2
        if self.result_of_eq(center)==0:
            print(center, "is the root ")
            return 0
        else: return center
#...............................................................................................................
class result_close(check) :
    def check2(self,error,root):
        result =0
        com = self.result_of_eq(root)
        if abs(com) <= error:return 1
        else : return 0

#main code ..........................................................................................................

parameter_equ = list(map(float, input("enter the parameter of equ as shape ax^n +bx^n-1 +.....+ k=0").split()))
error = float(input("enter the error allowed "))
point1 , point2 = map(float,input ("enter the interval that have the root in it ").split())

cheker1 = check()
equitions = equ()
cheker2= result_close()

state = 0
while state ==0 :
    result1 = cheker1.check_interval(point1,point2)
    if result1 ==2 or result1==3: state =2
    else:
        while result1 ==0 :
            point1, point2 = map(int, input("invalid interval please enter valid interval that have the root in it ").split())
            result1 = cheker1.check_interval(point1, point2)
        root = equitions.midpoint(point1,point2)
        if root ==0 : state=2
        else:
            if cheker1.check_interval(point1, root)==1: point2=root
            else:point1=root
            state = cheker2.check2(error , root)

if state ==2: pass
elif state==1 :
    print("the root of equ is ",root ,"with error ",error)
