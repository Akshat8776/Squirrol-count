import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
lis=data["Primary Fur Color"].to_list()
p1=0
p2=0
p3=0
for i in lis:
    if i=="Gray":
        p1+=1
    elif i=="Cinnamon":
        p2+=1
    elif i=="Black":
        p3+=1
        
print("     Primary Fur Color   Count")
print(f"     Gray               {p1}")
print(f"     Cinnamon           {p2}")
print(f"     Black              {p3}")

#Way 2
v1=len(data[data["Primary Fur Color"]=="Gray"])
v2=len(data[data["Primary Fur Color"]=="Cinnamon"])
v3=len(data[data["Primary Fur Color"]=="Black"])
print(f"{v1}    {v2}    {v3}")
data_dict={
    "Fur color":["Gray","Cinnamon","Black"],
    "Count":[v1,v2,v3]
}
df=pandas.DataFrame(data_dict)
df.to_csv("squi_count.csv")