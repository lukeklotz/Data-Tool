
#This data represents revenue for solar perovskite recycling
#
#
#variable name = material TYPE
#key           = materal NAME
#value         = revenue AMOUNT

from costDataJuan import *

class revenueData:
    def __init__(self):
        self.coverGlassRev  = {"2-2.5mm Glass (Emma)":3.75}
        self.backContactRev = {"Au(40nm) (Emma)": 5.00, 
                               "Cu(150nm) (Emma)": 0.34, 
                               "Ag (Emma)": 0.71,
                               "Ag (Feng 2021)":2.59,
                               "Ag (Ren 2021)":2.59,
                               "Cu (O'Hara 2023)":0.000041,
                               "Gold (Kim 2023)":93.88,
                               "PbI₂ (Ren 2021)":0.24} 
        self.absorberRev    = {"PbI₂ (Emma)":0.53, 
                               "PbSO (Emma)":0.01,
                               "MAPbI₃ (Feng 2021)":0.32,
                               "PbI₂ (Reng 2021)":0.24,
                               "Pb₃O₄ (O'Hara)":0.01}
        self.glassRev       = {"Glass (Emma)":9.38,
                               "ITO/Glass (Feng 2021)":6.92,
                               "FTO/Glass (Reng 2021)":5.00,
                               "ITO/Glass (O'Hara 2023)":6.92,
                               "ITO/Glass (Kim 2023)":6.92,
                               "ITO/Glass (Bo Chen 2021)":6.92}

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
        return self.backContactRev.get(method, 0)

    def getAbsorberRev(self, method):
        return self.absorberRev.get(method, 0)

    def getGlassRev(self, method):
        return self.glassRev.get(method, 0)

