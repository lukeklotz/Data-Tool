import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import dash
from dash import dcc, html, Input, Output, callback

class costData:
    def __init__(self):
        self.coverGlass  = {
                               "Thermal Delamination (McCalmot et al.)":0.04,
                               "Hot Knife (McCalmot et al.)":           0.10,
                               "Autoclaving (McCalmot et al.)":         0.44
                               }
        self.backContact = {
                               "Feng 2021" : 0.003, #0.0026806
                               "Ren 2021":   0.49,
                               "O'Hara 2023":0.01,  #0.000014
                               "Kim 2023" :  0.002,  #0.001842
                              } 
        self.absorber    = {
                               "Feng 2021" :    1.76, 
                               "Ren 2021" :     6.12,      #6.117517
                               "O'Hara 2023" :      0.002,     #0.0017
                               }
        self.glass       = {
                               "Glass (Feng 2021)" : 6.18,
                               "Glass (Ren 2021)" : 0.38,
                               "Glass (O'Hara)":    2.38,
                               "Glass (Kim 2023)" : 9.131,
                               "Glass (Bo Chen 2021)" : 0.03,
                              }

    def getCoverGlass(self):
        return self.coverGlass

    def getBackContact(self):
        return self.backContact
    
    def getAbsorber(self):
        return self.absorber

    def getGlass(self):
        return self.glass
    
    def getCoverGlassCost(self, method):

        return self.coverGlass.get(method, 0)

    def getBackContactCost(self, method):
        
        return self.backContact.get(method, 0)

    def getAbsorberCost(self, method):
        return self.absorber.get(method, 0)

    def getGlassCost(self, method):
        return self.glass.get(method, 0)