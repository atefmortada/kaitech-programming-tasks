import pandas as p
import matplotlib.pyplot as pt
sensor_data = [
    ("S1", "2025-04-28 10:00", 35.2, 12.1, 0.002),
    ("S1", "2025-04-28 11:00", 36.1, 12.5, 0.0021),
    ("S3", "2025-04-28 10:00", 34.0, 11.8, 0.0025),
    ("S2", "2025-04-28 11:00", 37.2, 14.3, 0.0031),
    ("S1", "2025-04-28 12:00", 37.0, 13.0, 0.0022),
    ("S2", "2025-04-28 10:00", 36.5, 14.0, 0.003),
]
data= p.DataFrame(sensor_data , index=[1,2,3,4,5,6],columns=["sensor_id","timestamp","temperature","stress","displacement"])
data["timestamp"]=p.to_datetime(data["timestamp"])
data = data.set_index("sensor_id")
print(data)
stat=data.groupby("sensor_id").mean()
print(stat)
max_temp=stat[stat["temperature"]==stat["temperature"].max()]
print(max_temp)
data["timestamp"]=data["timestamp"].dt.hour
sensor1=data.loc["S1"]
sensor2=data.loc["S2"]
sensor3=data.loc["S3"]
pt.figure("line")
pt.plot(sensor1["timestamp"],sensor1["temperature"],color="blue",marker="^",linestyle="solid", label="sensor1")
pt.plot(sensor2["timestamp"],sensor2["temperature"],color="black",marker=">",linestyle="dashed", label="sensor2")
pt.plot(sensor3["timestamp"],sensor3["temperature"],color="red", marker="*",linestyle="dashdot", label="sensor3")
pt.title("temperature monitor")
pt.xlabel("hours")
pt.ylabel("temp c")
pt.legend()
pt.grid(True)
pt.figure("scatter")
pt.scatter(sensor1["stress"],sensor1["displacement"],color="blue",marker="^")
pt.scatter(sensor2["stress"],sensor2["displacement"],color="black",marker="*")
pt.scatter(sensor3["stress"],sensor3["displacement"],color="red",marker=">")
pt.title("stress x displacement")
pt.xlabel("stress")
pt.ylabel("displacement")
pt.grid(True)
pt.show()
