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
        print(f" sensor {iterator2[0]} when read at {iterator2[1]} has {l1} and {l2} and {l3 }")
    return  extreme_values
def com1 ():
    l1 = organize()
    for iterator1 in l1 :
        i=1
        t1,t2,t3=0,0,0
        tem, stress, distance = 0, 0, 0
        while i < len(iterator1):
            if tem < iterator1[i][1]:
                tem = iterator1[i][1]
                t1+=1
            if    stress < iterator1[i][2]:
                stress = iterator1[i][2]
                t2+=1
            if distance <   iterator1[i][3]:
                distance = iterator1[i][3]
                t3+=1

            i+=1
        print(f" the max value of sensor {iterator1[0]} is temperature = {tem} at {iterator1[t1][0]} and stress {stress} at {iterator1[t2][0]} and distance {distance} at {iterator1[t3][0]}")
def com2():
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
    print(f" the max value of sensors  is temperature = {tem} and stress {stress}  and distance {distance} ")
def summarize():
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
        print(f" the max value of sensor {iterator1[0]}  is temperature = {tem} and stress {stress}  and distance {distance} ")
        i=1
        while i<len(iterator1):
            if tem > iterator1[i][1]:
                tem = iterator1[i][1]
            if stress > iterator1[i][2]:
                stress = iterator1[i][2]
            if distance > iterator1[i][3]:
                distance = iterator1[i][3]
            i += 1
        print( f" the min value of sensor {iterator1[0]}  is temperature = {tem} and stress {stress}  and distance {distance} ")
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
        print(f" sensor {iterator1[0]} has averege temperature {ave_tem} and average stress {ave_stress} and averege distance {ave_dis}")
def new_organize ():
    sensor_data_new ={}
    ids =[]
    for id,timestamp,temp, stress , dis in sensor_data:
        l1=(timestamp,temp, stress , dis)
        if id in ids :
            sensor_data_new[id].append(l1)
        else:
            sensor_data_new[id]=[]
            sensor_data_new[id].append(l1)
            ids.append(id)
    return sensor_data_new
def unique ():
    unique_id = set()
    for iterator in sensor_data:
        if iterator[3]>13:
            new_id =   iterator[0]+" "+iterator[1]
            unique_id.add(new_id)
    return unique_id
def statistics ():
    l1 = organize()
    tem, stress, distance = 0, 0, 0
    for iterator1 in l1:
        i = 1
        while i < len(iterator1):
            if tem < iterator1[i][1]:
                tem = iterator1[i][1]
            if distance < iterator1[i][3]:
                distance = iterator1[i][3]
            i += 1
        print(f" the max value of sensor {iterator1[0]}  is temperature = {tem} and distance {distance} ")

        i = 1
        while i < len(iterator1):
            if tem > iterator1[i][1]:
                tem = iterator1[i][1]
            i+=1
        print( f" the min value of sensor {iterator1[0]}  is temperature = {tem}")
        i = 1
        sum_tem, sum_stress, sum_dis = 0, 0, 0
        while i < len(iterator1):
            sum_tem += iterator1[i][1]
            i+=1
        ave_tem = sum_tem /  (len(iterator1)-1)
        print(f"the averege of sensor {iterator1[0]} is temperature = {ave_tem}")
def timetamps ():
    time =[]
    for iterator in sensor_data:
        time.append(iterator[1])
    return time
def sort (time):
    i=0
    while i<len(time) :
        j=i+1
        while j<len(time) :
            if time[i]>time[j]:
                step = time[i]
                time[i]=time[j]
                time[j]= step
            j+=1
        i+=1
    return time
def recent ():
    l1 = organize()
    recent_reading=[]
    for iterator in l1 :
        i=1
        check ="0"
        while i<len(iterator):
            if iterator[i][0]>check :
                check=iterator[i][0]
                most_recent=tuple(iterator[i])
            i+=1
        recent_reading.append(most_recent)
    return recent_reading


sensor_data = [
    ("S1", "2025-04-28 10:00", 35.2, 12.1, 0.002),
    ("S1", "2025-04-28 11:00", 36.1, 12.5, 0.0021),
    ("S3", "2025-04-28 10:00", 34.0, 11.8, 0.0025),
    ("S2", "2025-04-28 11:00", 37.2, 14.3, 0.0031),
    ("S1", "2025-04-28 12:00", 37.0, 13.0, 0.0022),
    ("S2", "2025-04-28 10:00", 36.5, 14.0, 0.003),

]
# assume extreme value of tempreture is 37 or more and for stress is 14 or more  and for displacement is .003 or more
ex_temp = 37
ex_stress = 14
ex_dis= .003
print(organize())
print("...................................................................................")
explore()
print(".....................................................................................")
com1()
print(".......................................................................................")
com2()
print(".......................................................................................")
summarize()
print(".......................................................................................")
print(new_organize())
print(".......................................................................................")
print(unique())
print(".......................................................................................")
statistics()
print(".......................................................................................")
print(timetamps())
print(".......................................................................................")
print(sort(timetamps()))
print(".......................................................................................")
print(recent())