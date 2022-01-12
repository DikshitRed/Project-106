import csv
import plotly.express as px
import numpy as np

def plotGraph(data):
    with open ("cups of coffee vs hours of sleep.csv") as g:
        df=csv.DictReader(g)
        fig=px.scatter(df, x="Coffee in ml", y="sleep in hours", color="week")
        fig.show()

def getasList(datasource):
    cups_of_coffee=[]
    hours_of_sleep=[]
    with open (datasource) as f:
        reader=csv.DictReader(f)
        for i in reader:
            cups_of_coffee.append(float(i["Coffee in ml"]))
            hours_of_sleep.append(float(i["sleep in hours"]))
    return {"x": cups_of_coffee, "y": hours_of_sleep}

def correlation(dataset):
    corelation=np.corrcoef(dataset["x"],dataset["y"])
    print("The corelation between coffee and sleep =", corelation[1,-1])

def setup():
    datasource = "cups of coffee vs hours of sleep.csv"
    dataset= getasList(datasource)
    correlation(dataset)
    plotGraph(datasource)

setup()