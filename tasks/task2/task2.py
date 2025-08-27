# opp ............................................................................................................
class parent :
    @staticmethod      #give newparameter2
    def f1 (parameters1,parameters2):
        newparameter1 =[]
        newparameter2 =[]
        if parameters1[0]!=0:
            f1 = parameters2[0]/parameters1[0]
            for iterator1 in parameters1:
                newparameter1.append(f1*iterator1)
            for iterator2 in range(4):
                newparameter2.append(parameters2[iterator2]-newparameter1[iterator2])
        else : newparameter2 =parameters1
        return  newparameter2
#...................................................................................................................
class child1 (parent): #give newparameter4
    pass
class equ :
    @staticmethod   #give newparameter6
    def sol ():
        newparameter5=[]
        newparameter6=[]
        if newparameter4[1] != 0:
            f3 = newparameter2[1] / newparameter4[1]
            for iterator5 in newparameter4:
                newparameter5.append(f3 * iterator5)
            for iterator6 in range(4):
                newparameter6.append(newparameter2[iterator6] - newparameter5[iterator6])
        else:
            newparameter6 = newparameter4
        return newparameter6
#.................................................................................................................
class solution :
    @staticmethod   #give solution
    def solu ( ):
        if newparameter6[2] == 0:
            z = 0
        else:
            z = newparameter6[3] / newparameter6[2]
        if newparameter4[1] == 0 and newparameter2[1] == 0:
            y = 0
        elif newparameter4[1] != 0:
            y = (newparameter4[3] - z * newparameter4[2]) / newparameter4[1]
        elif newparameter2[1] != 0:
            y = (newparameter2[3] - z * newparameter2[2]) / newparameter2[1]
        if parameters1[0] != 0:
            x = (parameters1[3] - z * parameters1[2] - y * parameters1[1]) / parameters1[0]
        elif parameters2[0] != 0:
            x = (parameters2[3] - z * parameters2[2] - y * parameters2[1]) / parameters2[0]
        elif parameters3[0] != 0:
            x = (parameters3[3] - z * parameters3[2] - y * parameters3[1]) / parameters3[0]
        else:
            x = 0

        return x, y, z
# main code ...........................................................................................................


parameters1 = list(map(int, input("enter the parameters of first equ as shape nx+my+lz=k ").split()))
parameters2 = list(map(int, input("enter the parameters of first equ as shape nx+my+lz=k ").split()))
parameters3 = list(map(int, input("enter the parameters of first equ as shape nx+my+lz=k ").split()))

e1 = parent()
e2=child1()
s1 = equ()
s2=solution()

newparameter2=e1.f1(parameters1,parameters2)
newparameter4=e2.f1(parameters3,parameters2)
newparameter6 =s1.sol()
l1=s2.solu()

print("the root of this systems of equ is : ")
print(" x = ", l1[0])
print(" y = ", l1[1])
print(" z = ", l1[2])

