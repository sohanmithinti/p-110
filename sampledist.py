import plotly.figure_factory as ff
import csv
import pandas as pd 
import statistics
import random 
import plotly.graph_objects as go

reader = pd.read_csv("temp.csv")
data = reader["temp"].tolist()

mean = statistics.mean(data)
std = statistics.stdev(data)

print(mean)
print(std)

data1 = []
for i in range(0, 1000):
    index = random.randint(0, len(data))
    value = data[index]
    data1.append(value)
print(data1)    

mean1 = statistics.mean(data1)
std1 = statistics.stdev(data1)

print("mean of sample data = ", mean1)
print("std of smaple data = ", std1)

graph = ff.create_distplot([data1], ["temp"], show_hist = False)
graph.add_trace(go.Scatter(x = [mean, mean1], y = [0, 1], mode = "lines", name = "mean"))
graph.show()
