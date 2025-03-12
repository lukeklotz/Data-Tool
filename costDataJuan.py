import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import dash
from dash import dcc, html, Input, Output, callback

class costData:
    def __init__(self):
        self.coverGlassRev  = {"default":0.00}
        self.backContactRev = {
                               "Butylamine (BA) (Feng 2021)":               0.002669,
                               "Flange-Mount Immersion Heaters (Feng 2021)":0.0000116,

                               "Adhesive (Ren 2021)":                       0.49,

                               "KI solution 1.5M (O'Hara 2023)":            0.000014,

                               "CB (Kim 2023)":  0.00095,
                               "DMF (Kim 2023)": 0.000892,
                              } 
        self.absorberRev    = {
                               "Butylamine (BA) (Feng 2021)":                 0.0123,
                               "Electricity, medium voltage (Feng 2021)":     0.0073,
                               "Ethanol, without water, in 95% (Feng 2021)":  0.00005,
                               "Hydrochloric acid, without water (Feng 2021)":0.05279,
                               "Tap water (Feng 2021)":                       0.00331,
                               "Toluene (Feng 2021)":                         1.69,
                               
                               "Electricity, medium voltage (Ren 2021)": 0.000069,
                               "Lead nitrate (Ren 2021)":    0.000087,
                               "Methanol (Ren 2021)":        0.000006,
                               "Tap water (Ren 2021)":       0.000003,
                               "Zeolite, powder (Ren 2021)": 0.000002,
                               "Nitrogen, Liquid (Ren 2021)":0.013350,
                               "Ethyl acetate (Ren 2021)":   6.104,

                               "Electricity, medium voltage (O'Hara)": 0.0000023,
                               "Sulfuric Acid (O'Hara)":               0.000829,
                               "KI solution 1.5M (O'Hara)":            0.000895,

                               "Thermal delamination (hot plate) (Bo Chen 2021)":     0.00000605,
                               "Hot Blade (assumed 30 sec) (Bo Chen 2021)":           0.00000363,
                               "DMF (Bo Chen 2021)":                                  4.425,
                               "Acidic cation-exchange resin (Bo Chen 2021)":         0.0172,  
                               "Nitric acid (Bo Chen 2021)":                          0.0009625,
                               "Sodium iodide (Nal) (Bo Chen 2021)":                  1.09836,
                               }
        self.glassRev       = {
                               "Butylamine (BA) (Feng 2021)":               6.13,
                               "Ethanol, without water, in 95% (Feng 2021)":0.024,
                               "Electricity, medium voltage (Feng 2021)":   0.026,

                               "Nitrogen, Liquid (Ren 2021)":            0.01394,
                               "Tap water (Ren 2021)":                   0.0003,
                               "Zeolite, powder (Ren 2021)":             0.00397,
                               "Electricity, medium voltage (Ren 2021)": 0.3595,

                               "KI Solution 1.5M (O'Hara)":              2.38,

                               "CB (Kim 2023)":  4.709,
                               "DMF (Kim 2023)": 4.422,

                               "CB (Bo Chen 2021)": 0.004,
                               "Thermal delamination (drying) (Bo Chen 2021)": 0.03025,
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