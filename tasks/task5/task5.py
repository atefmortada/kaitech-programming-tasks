def organize ():
    sensor_data_new =[]
    ids =[]
    for id,timestamp,temp, stress , dis in sensor_data:
        l1 = [ timestamp,temp, stress , dis]
        if id in ids:
            for iterator2 in sensor_data_new:
                if id == iterator2[0]:
                    iterator2.append(l1)
        else :
            l1 = [id , [timestamp,temp, stress , dis]]
            sensor_data_new.append(l1)
            ids.append(id)
    return sensor_data_new
def explore ():
    extreme_values=[]
    for iterator in sensor_data :
        l1 = []
        if iterator[2]>= ex_temp or iterator[3]>=ex_stress or iterator[4]>=ex_dis :
            l1.append(iterator[0])
            l1.append(iterator[1])
            if iterator[2]>= ex_temp:
                l1.append(iterator[2])
            else : l1.append(0)
            if iterator[3]>= ex_stress:
                l1.append(iterator[3])
            else: l1.append(0)
            if iterator[4]>=ex_dis:
                l1.append(iterator[4])
            else : l1.append(0)
            extreme_values.append(l1)

    for iterator2 in extreme_values:
        if iterator2 [2]!=0 :
            l1 = f"extreme temprature = {iterator2[2]}"
        else : l1 = "normal temperature "
        if iterator2[3]!=0:
            l2 = f"extreme stress = {iterator2[3]}"
        else : l2 = " normal stress "
        if iterator2[4]!=0 :
            l3 = f"extreme distance = {iterator2[4]}"
        else : l3 = "normal distance "
       # print(f" sensor {iterator2[0]} when read at {iterator2[1]} has {l1} and {l2} and {l3 }")
    return  extreme_values
def com1 ():
    l1 = organize()
    result = []
    for iterator1 in l1:
        list1 = []
        list1.append(iterator1[0])
        i = 1
        t1, t2, t3 = 0, 0, 0

        tem, stress, distance = 0, 0, 0
        while i < len(iterator1):
            if tem < iterator1[i][1]:
                tem = iterator1[i][1]
                t1 += 1
            if stress < iterator1[i][2]:
                stress = iterator1[i][2]
                t2 += 1
            if distance < iterator1[i][3]:
                distance = iterator1[i][3]
                t3 += 1

            i += 1
        list1.append(tem)
        list1.append(stress)
        list1.append(distance)
        result.append(list1)
    return result
def max():
    l1 = organize()
    tem, stress, distance = 0, 0, 0
    for iterator1 in l1:
        i = 1
        while i < len(iterator1):
            if tem < iterator1[i][1]:
                tem = iterator1[i][1]
            if stress < iterator1[i][2]:
                stress = iterator1[i][2]
            if distance < iterator1[i][3]:
                distance = iterator1[i][3]
            i += 1
    return tem , stress, distance
def min():
    l1 = organize()
    tem, stress, distance = max()
    for iterator1 in l1:
        i = 1
        while i < len(iterator1):
            if tem > iterator1[i][1]:
                tem = iterator1[i][1]
            if stress > iterator1[i][2]:
                stress = iterator1[i][2]
            if distance > iterator1[i][3]:
                distance = iterator1[i][3]
            i += 1
    return tem , stress, distance
def ave():
    l1 = organize()
    tem, stress, distance = 0, 0, 0
    sum_tem, sum_stress, sum_dis = 0, 0, 0
    j=0
    for iterator1 in l1:
        i = 1
        while i < len(iterator1):
            sum_tem += iterator1[i][1]
            sum_stress += iterator1[i][2]
            sum_dis += iterator1[i][3]
            i += 1
        j+=len(iterator1)-1
    ave_tem = sum_tem / j
    ave_stress = sum_stress / j
    ave_dis = sum_dis /j
    return ave_tem , ave_stress, ave_dis
def summarize():
    l1 = organize()
    result_max=["max"]
    result_min=["min" ]
    result_ave=["ave"]
    tem, stress, distance = 0, 0, 0
    for iterator1 in l1:
        maxx=[]
        minn=[]
        ave=[]
        maxx.append(iterator1[0])
        minn.append(iterator1[0])
        ave.append(iterator1[0])
        i = 1
        while i < len(iterator1):
            if tem < iterator1[i][1]:
                tem = iterator1[i][1]
            if stress < iterator1[i][2]:
                stress = iterator1[i][2]
            if distance < iterator1[i][3]:
                distance = iterator1[i][3]
            i += 1
        maxx.append(tem)
        maxx.append(stress)
        maxx.append(distance)
        result_max.append(maxx)
        i=1
        while i<len(iterator1):
            if tem > iterator1[i][1]:
                tem = iterator1[i][1]
            if stress > iterator1[i][2]:
                stress = iterator1[i][2]
            if distance > iterator1[i][3]:
                distance = iterator1[i][3]
            i += 1
        minn.append(tem)
        minn.append(stress)
        minn.append(distance)
        result_min.append(minn)
        i=1
        sum_tem , sum_stress , sum_dis = 0,0 ,0
        while i < len(iterator1):
            sum_tem +=iterator1[i][1]
            sum_stress += iterator1[i][2]
            sum_dis+= iterator1[i][3]
            i+=1
        ave_tem = sum_tem/ (len(iterator1)-1)
        ave_stress = sum_stress/ (len(iterator1)-1)
        ave_dis = sum_dis/ (len(iterator1)-1)
        ave.append(ave_tem)
        ave.append(ave_stress)
        ave.append(ave_dis)
        result_ave.append(ave)
    return result_max,result_min,result_ave
def new_organize ():
    sensor_data_new ={}
    l2=[]
    ids =[]
    for id,timestamp,temp, stress , dis in sensor_data:
        l1=(timestamp,temp, stress , dis)
        if id in ids :
            sensor_data_new[id].append(l1)
        else:
            l2.append(sensor_data_new)
            sensor_data_new[id]=[]
            sensor_data_new[id].append(l1)
            ids.append(id)
    f1 = {"s1": l2[0]["S1"]}
    f2 = {"s2": l2[0]["S2"]}
    f3 = {"s3": l2[0]["S3"]}
    lis = [f1, f2, f3]
    return lis
def unique ():
    unique_id = set()
    for iterator in sensor_data:
        if iterator[3]>13:
            new_id =   iterator[0]+" "+iterator[1]
            unique_id.add(new_id)
    return unique_id
def timetamps ():
    time =[]
    for iterator in sensor_data:
        time.append(iterator[1])
    return time
def recent ():
    l1 = organize()
    recent_reading=[]
    most_recent_list=()
    for iterator in l1 :
        i=1
        check ="0"
        while i<len(iterator):
            if iterator[i][0]>check :
                check=iterator[i][0]
                most_recent_list=(iterator[0],iterator[i])
            i+=1
        recent_reading.append(most_recent_list)
    return recent_reading
def dict1 (data):
    keys = []
    values1 = []
    for iterator in data:
        values2 = []
        keys.append(iterator[0])
        for iterator2 in iterator:
            if iterator2 == iterator[0]: continue
            values2.append(iterator2)
        values1.append(values2)
    return  dict(zip(keys,values1))
#...............................................................
ex_temp = 37
ex_stress = 14
ex_dis= .003


sensor_data = [
    ("S1", "2025-04-28 10:00", 35.2, 12.1, 0.002),
    ("S1", "2025-04-28 11:00", 36.1, 12.5, 0.0021),
    ("S3", "2025-04-28 10:00", 34.0, 11.8, 0.0025),
    ("S2", "2025-04-28 11:00", 37.2, 14.3, 0.0031),
    ("S1", "2025-04-28 12:00", 37.0, 13.0, 0.0022),
    ("S2", "2025-04-28 10:00", 36.5, 14.0, 0.003),

]
#.........................................................
import csv
import json
#......................................................
with open ('./task5.csv','w')as file :
    writer = csv.writer(file)
    writer.writerow(organize())
    writer.writerow(explore())
    writer.writerow(com1())
    writer.writerow(summarize())
    writer.writerow(new_organize())
    writer.writerow(unique())
    writer.writerow([max()[0], min()[0],ave()[0]])
    writer.writerow([max()[2]])
    writer.writerow(sorted(timetamps()))
    writer.writerow(recent())
#........................................

dict_organize = dict1(organize())
dict_com = dict1(com1())
dict_recent = dict1(recent())
#.................................................

unique_id = dict()
value=[]
key = 0
for iterator in sensor_data:
    if iterator[3] > 13:

        if key == iterator[0]:
            value . append(iterator[1])

        else :
            value.append(iterator[1])
            unique_id[iterator[0]]=value
            key = iterator[0]
#.............................................................

keys = []
values1 = []
for iterator in organize():
    values2 = []
    keys.append(iterator[0])
    for iterator2 in iterator:
        if iterator2 == iterator[0]: continue
        values2.append(iterator2[0])
    values1.append(values2)
dict_time=  dict(zip(keys, values1))

#.......................................................................
dict_statistics = {'max_tem': max()[0], 'min_tem':min()[0], 'average_tem':ave()[0]}
dict_statistics2 = {'max_dis':max()[2]}
#........................................................................

keys=[]
values2=[]
for iterator in summarize():
    for iterator2 in iterator :
        if iterator2 == 'max' or iterator2 == 'min'or iterator2 == 'ave'  :
            continue
        keys.append(iterator[0]+' '+ iterator2[0])
        values1 = []
        for iterator3 in iterator2:
            if iterator3 == 'S1' or iterator3 =='S2' or iterator3== 'S3' : continue
            values1.append(iterator3)
        values2.append(values1)

dict_summerazie = dict(zip(keys , values2))

#...................................................................................................

keys = []
values1 = []
for iterator in explore():
    values2 = []
    keys.append(iterator[0])
    for iterator2 in iterator:
        if iterator2 == iterator[0]: continue
        values2.append(iterator2)
        values1.append(values2)
dict_explore = dict(zip(keys, values1))
#...........................................................................

data = {
    'readings':[dict_organize,dict_explore,dict_summerazie,
new_organize(),unique_id,dict_statistics,dict_statistics2,dict_time,dict_recent,
 ]
}




with open ('./task5.json', 'w') as jfile :
    json.dump(data,jfile )




with open ('./task5.json', 'r') as jjfile :
    x=json.load(jjfile)
print(x)