import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import dash
from dash import dcc, html, Input, Output, callback

class Data:
    def __init__(self):
        self.dataObject = pd.read_excel("DATA_EMMA.xlsx", sheet_name=11)
        self.filtered_data = self.dataObject[["Unnamed: 14", "Method", "Cost"]] 
        self.labels = self.filtered_data["Unnamed: 14"].dropna().unique()

    def getCoverGlass(self): 
        return self.filtered_data.iloc[0:3]

    def getBackContact(self):
        return self.filtered_data.iloc[3:6]
    
    def getAbsorber(self):
        return self.filtered_data.iloc[6:10]

    def getEtl(self):
        return self.filtered_data.iloc[10:11]
    
