
#This data represents revenue for solar perovskite recycling
#
#
#variable name = material TYPE
#key           = materal NAME
#value         = revenue AMOUNT

from costData import *

class revenueData:
    def __init__(self):
        self.coverGlassRev  = {"2-2.5mm Glass (McCalmot et al.)":3.75}

        self.backContactRev = {
                               "Feng 2021":2.59,
                               "Ren 2021":2.59,
                               "O'Hara 2023":0.01,
                               "Kim 2023":93.88,
                               } 

        self.absorberRev    = {
                               "Feng 2021":0.32,
                               "Reng 2021":0.24,
                               "O'Hara":0.01}

        self.glassRev       = {
                               "ITO/Glass (Feng 2021)":6.92,
                               "ITO/Glass (O'Hara 2023)":6.92,
                               "ITO/Glass (Kim 2023)":6.92,
                               "ITO/Glass (Bo Chen 2021)":6.92,
                               "FTO/Glass (Reng 2021)":5.00,
                               }

    def getCoverGlass(self):
        return self.coverGlassRev

    def getBackContact(self):
        return self.backContactRev
    
    def getAbsorber(self):
        return self.absorberRev

    def getGlass(self):
        return self.glassRev

    def getCoverGlassRev(self, method):
        return self.coverGlassRev.get(method, 0)

    def getBackContactRev(self, method):
        
        if method in self.backContactRev.keys():
            return self.backContactRev.get(method, 0)

        return self.backContactRev.get(method, 0)

    def getAbsorberRev(self, method):

        if method in self.absorberRev.keys():
            return self.absorberRev.get(method, 0)
        
        return self.absorberRev.get(method, 0)

    def getGlassRev(self, method):
        return self.glassRev.get(method, 0)

