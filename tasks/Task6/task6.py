import  tkinter as tk
sensor_data = [
    ("S1", "2025-04-28 10:00", 35.2, 12.1, 0.002),
    ("S1", "2025-04-28 11:00", 36.1, 12.5, 0.0021),
    ("S3", "2025-04-28 10:00", 34.0, 11.8, 0.0025),
    ("S2", "2025-04-28 11:00", 37.2, 14.3, 0.0031),
    ("S1", "2025-04-28 12:00", 37.0, 13.0, 0.0022),
    ("S2", "2025-04-28 10:00", 36.5, 14.0, 0.003),
]
#.........................  fun of organize readings  .................................................
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
def explore ():
    extreme_values=[]
    for iterator in sensor_data :
        l1 = []
        if iterator[2]>= 36.5 or iterator[3]>=13.5  :
            l1.append(iterator[0])
            l1.append(iterator[1])
            if iterator[2]>= 36.5:
                l1.append(iterator[2])
            else : l1.append("null")
            if iterator[3]>= 13.5:
                l1.append(iterator[3])
            else: l1.append("null")
            extreme_values.append(l1)

    for iterator2 in extreme_values:
        if iterator2 [2]!=0 :
            l1 = f"extreme temprature = {iterator2[2]}"
        else : l1 = "normal temperature "

        return  extreme_values
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
def timetamps ():
    time =[]
    for iterator in sensor_data:
        time.append(iterator[1])
        time.sort()
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

#.......................................  fun of buttons  ...............................................
def show_readings ():
    data=new_organize()
    readings1,readings2,readings3=data[0]['s1']
    readings4 ,readings5 = data[1]['s2']
    readings6=data[2]['s3'][0]
    result.config(text=f"the reading of sensor 1 : {readings1} {readings3} {readings2} \n the readings os sensor2 : {readings4} {readings5} \n the readings os sensor3 {readings6}")

def show_unique ():
    sensor1,sensor2 , sensor3= explore()
    result.config(text=f"these sensor have extreme values: \n  {sensor1} \n {sensor2} \n {sensor3}")

def show_max ():
    data_max = max()
    result.config(text=f" max temperature of all readings is {data_max[0]} \n max stress of all readings is {data_max[1]} \n max distance of all readings  is {data_max[2]}")

def show_summarize ():
    max , min , average = summarize()
    result.config(text=f"max temperature of s1 : {max[1][1]} \n min temperature of s1 : {min[1][1]} \n average temprature of s1 : {average[1][1]} \n "
                       f"max temperature of s2 : {max[3][1]} \n min temperature of s1 : {min[3][1]} \n average temprature of s1 : {average[3][1]}\n "
                       f"max temperature of s3 : {max[2][1]} \n min temperature of s1 : {min[2][1]} \n average temprature of s1 : {average[2][1]} \n"
                       f" max displacement of s1 : {max[1][3]} \n max displacement of s2 : {max[3][3]} \n max displacement of s3 : {max[2][3]}\n")

def show_sensor():
    sensor1 , sensor2 = unique()
    result.config(text=f"these sensors have stress > 13 :\n {sensor1} \n {sensor2}")

def show_time():
    data= "\n".join(timetamps())
    result.config(text=f"the timestamps are : {data}" )

def show_recent():
    data = recent()
    result.config(text=f"the most resnt readings of sensor1 : {data[0]} \n the most resnt readings of sensor2 : {data[1]} \n the most resnt readings of sensor3 : {data[2]} ")

#.......................................code...........................................................

root = tk.Tk()
root.title("readings sensors ")
root.geometry("400x400")
main_title = tk.Label(root , text="this is analysis for data from sensor ... done by atef mortada",bg="#8B4513",fg="black", font="25",pady=5,padx=5)
main_title.pack(pady=5)
result= tk.Label(root, font=("Helvetica",15),fg="#000080")
result.pack(pady=5)
button1= tk.Button(root, text="enter to show readings for each sensor " , pady=2,padx=2,bg="#40E0D0",font=("Arial",15), command=show_readings)
button1.pack(pady=5,fill="x")
button2= tk.Button(root, text="enter to show extreme readings of sensors " , pady=2,padx=2,bg="#40E0D0",font=("Arial",15), command=show_unique)
button2.pack(pady=5,fill="x")
button3 = tk.Button(root, text="enter to show max readings of all sensors " , pady=2,padx=2,bg="#40E0D0",font=("Arial",15), command=show_max)
button3.pack(pady=5,fill="x")
button4 = tk.Button(root, text="enter to show summarize of important reading " , pady=2,padx=2,bg="#40E0D0",font=("Arial",15), command=show_summarize)
button4.pack(pady=5,fill="x")
button5 = tk.Button(root, text="enter to show senors have stress > 13 " , pady=2,padx=2,bg="#40E0D0",font=("Arial",15), command=show_sensor)
button5.pack(pady=5,fill="x")
button6 = tk.Button(root, text="enter to show timestamps of all sensors " , pady=2,padx=2,bg="#40E0D0",font=("Arial",15), command=show_time)
button6.pack(pady=5,fill="x")
button7 = tk.Button(root, text="enter to show recent reading per sensor  " , pady=2,padx=2,bg="#40E0D0",font=("Arial",15), command=show_recent)

root.mainloop()





