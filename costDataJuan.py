import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import dash
from dash import dcc, html, Input, Output, callback

class costData:
    def __init__(self):
        self.coverGlassRev  = {"Thermal Delamination (McCalmot et al.)":0.04,
                               "Hot Knife (McCalmot et al.)":           0.10,
                               "Autoclaving (McCalmot et al.)":         0.44}
        self.backContactRev = {
                               "Back Contact (Feng 2021)" : 0.0026806,
                               "Back Contact (Ren 2021)":   0.49,
                               "Back Contact (O'Hara 2023)":0.000014,
                               "Back Contact (Kim 2023)" : 0.001842,
                              } 
        self.absorberRev    = {
                               "Absorber (Feng 2021)" :    1.76, 
                               "Absorber (Ren 2021)" :     6.117517,
                               "Absorber (O' Hara)" :      0.0017,
                               "Absorber (Bo Chen 2021)" : 5.54153218,
                               }
        self.glassRev       = {
                               "Glass (Feng 2021)" : 6.18,
                               "Glass (Ren 2021)" : 0.38,
                               "Glass (O'Hara)":    2.38,
                               "Glass (Kim 2023)" : 9.131,
                               "Glass (Bo Chen 2021)" : 0.03,
                              }

    def getCoverGlass(self):
        return self.coverGlassRev

    def getBackContact(self):
        return self.backContactRev
    
    def getAbsorber(self):
        return self.absorberRev

    def getGlass(self):
        return self.glassRev
    
    def getCoverGlassCost(self, method):
        return self.coverGlassRev.get(method, 0)

    def getBackContactCost(self, method):
        return self.backContactRev.get(method, 0)

    def getAbsorberCost(self, method):
        return self.absorberRev.get(method, 0)

    def getGlassCost(self, method):
        return self.glassRev.get(method, 0)