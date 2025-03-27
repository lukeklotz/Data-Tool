import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import dash
from dash import dcc, html, Input, Output, callback

class costData:
    def __init__(self):

        self.HTLayer     = {
            "Xiao et al 2025" : 0.00,
            "Wu et al 2024" : 4.78,
        }
        self.backContact = {
                               "Feng 2021" : 0.003, #0.0026806
                               "Ren 2021":   0.49,
                               "O'Hara 2023":0.01,  #0.000014
                               "Kim 2023" :  0.002,  #0.001842
                               "Xiao et al 2025" : 0.00,
                               "Wu et al 2024" :   0.00,
                            } 
        self.absorber    = {
                               "Feng 2021" :    1.76, 
                               "Ren 2021" :     6.12,      #6.117517
                               "O'Hara 2023" :      0.002,     #0.0017
                               "Bo Chen 2021":      5.54,
                               "Xiao et al 2025" :  3.20,
                               "Wu et al 2024"   :  0.02,
                            }
        self.glass       = {
                               "Feng 2021" : 6.18,
                               "Ren 2021" : 0.38,
                               "O'Hara 2023":    2.38,
                               "Kim 2023" : 9.131,
                               "Bo Chen 2021" : 0.03,
                               "Xiao et al 2025" : 1.50,
                               "Wu et al 2024" : 0.03,
                              }
        
    
    def getHTLayer(self):
        return self.HTLayer

    def getBackContact(self):
        return self.backContact
    
    def getAbsorber(self):
        return self.absorber

    def getGlass(self):
        return self.glass

    def getHTLayerCost(self, method):
        return self.HTLayer.get(method, 0)

    def getBackContactCost(self, method):
        return self.backContact.get(method, 0)
    
    def getBackContactType(self, method):

        for i in range(len(self.backContact)):
            if self.backContact[i][0] == method:
                return self.backContact[i][1]

        return self.backContact[0][1]

    def getAbsorberCost(self, method):
        return self.absorber.get(method, 0)

    def getGlassCost(self, method):
        return self.glass.get(method, 0)
