
#This data represents revenue for solar perovskite recycling
#
#
#variable name = material TYPE
#key           = materal NAME
#value         = revenue AMOUNT

from costData import *

class revenueData:
    def __init__(self):
        
        self.HTLayerRev = [["Xiao et al 2025", "spiro-OMeTAD", 7.04],
                           ["Wu et al 2024", "spiro-OMeTAD", 7.04],]

        self.backContactRev = [
                            ["Feng 2021", "Ag", 2.59],
                            ["Ren 2021", "Ag", 2.59],
                            ["O'Hara 2023", "Cu", 0.01],
                            ["Kim 2023", "Gold", 93.88],
                            ["Xiao et al 2025", "Gold", 65.39],
                            ["Wu et al", "Gold", 43.15],
                            ]
        self.absorberRev    = [
                               ["Feng 2021", "MAPbI₃", 0.32],
                               ["Ren 2021", "PbI₂", 0.24],
                               ["O'Hara 2023", "Pb₃O₄", 0.01],
                               ["Bo Chen 2021", "PbI₂", 0.242],
                               ["Xiao et al 2025", "PbI₂", 6.92],
                               ["Wu et al 2024", "MAPbI3", 0.319],
                              ]

        self.glassRev       = [
                               ["Feng 2021", "ITO/Glass (Feng)", 6.92],
                               ["O'Hara 2023", "ITO/Glass (O'Hara)", 6.92],
                               ["Kim 2023", "ITO/Glass (Kim)", 6.92],
                               ["Bo Chen 2021", "ITO/Glass (Bo Chen)", 6.92],
                               ["Ren 2021", "FTO/Glass", 5.00],
                               ["Xiao et al", "SnO₂", 6.92],
                               ["Wu et al", "SnO₂", 6.92],
                              ]

    def getHTLayter(self):
        return self.HTLayerRev

    def getBackContact(self):
        return self.backContactRev
    
    def getAbsorber(self):
        return self.absorberRev

    def getGlass(self):
        return self.glassRev

    def getBackContactRev(self, method):
        for i in range(len(self.backContactRev)):
            if self.backContactRev[i][0] == method:
                return self.backContactRev[i][2]

        return self.backContactRev[0][2]

    def getBackContactType(self, method):
        for i in range(len(self.backContactRev)):
            if self.backContactRev[i][0] == method:
                return self.backContactRev[i][1]

        return self.backContactRev[0][1]

    def getAbsorberRev(self, method):  
        for i in range(len(self.absorberRev)):
            if self.absorberRev[i][0] == method:
                return self.absorberRev[i][2]

        return self.backContactRev[0][2]

    def getAbsorberType(self, method):
        for i in range(len(self.absorberRev)):
            if self.absorberRev[i][0] == method:
                return self.absorberRev[i][1]

        return self.absorberRev[0][1]

    def getGlassRev(self, method):
        for i in range(len(self.glassRev)):
            if self.glassRev[i][0] == method:
                return self.glassRev[i][2]

        return self.glassRev[0][2]
    
    def getGlassType(self, method):
        for i in range(len(self.glassRev)):
            if self.glassRev[i][0] == method:
                return self.glassRev[i][1]

        return self.glassRev[0][1]

    def getHTLayerRev(self, method):
        for i in range(len(self.HTLayerRev)):
            if self.HTLayerRev[i][0] == method:
                return self.HTLayerRev[i][2]

        return self.HTLayerRev[0][2]

    def getHTLayerType(self, method):
        for i in range(len(self.HTLayerRev)):
            if self.HTLayerRev[i][0] == method:
                return self.HTLayerRev[i][1]

        return self.HTLayerRev[0][1]