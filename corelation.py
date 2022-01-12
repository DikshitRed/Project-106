import csv
import plotly.express as px
import numpy as np

def plotGraph(data):
    with open ("Student Marks vs Days Present.csv") as g:
        df=csv.DictReader(g)
        fig=px.scatter(df, x="Marks In Percentage", y="Days Present")
        fig.show()

def getasList(datasource):
    marks_of_students=[]
    numberof_days_present=[]
    with open (datasource) as f:
        reader=csv.DictReader(f)
        for i in reader:
            marks_of_students.append(float(i["Marks In Percentage"]))
            numberof_days_present.append(float(i["Days Present"]))
    return {"x": marks_of_students, "y": numberof_days_present}

def correlation(dataset):
    corelation=np.corrcoef(dataset["x"],dataset["y"])
    print("The corelation between marks and days =", corelation[1,-1])

def setup():
    datasource = "Student Marks vs Days Present.csv"
    dataset= getasList(datasource)
    correlation(dataset)
    plotGraph(datasource)

setup()