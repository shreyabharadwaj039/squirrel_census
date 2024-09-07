import pandas

data=pandas.read_csv("squirrel_project\data.csv")
gray_fur=len(data["Primary Fur Color"]=="Gray")
black_fur=len(data["Primary Fur Color"]=="Black")
cinnamon_fur=len(data["Primary Fur Color"]=="Cinnamon")

data_dict={
  "Fur Color":["Gray","Black","Cinnamon"],
  "Count":[gray_fur,black_fur,cinnamon_fur]
}

df=pandas.DataFrame(data_dict)
df.to_csv("squirrel_project\sqirrel_count.csv")
