
#This data represents revenue for solar perovskite recycling
#
#
#variable name = material TYPE
#key           = materal NAME
#value         = revenue AMOUNT

class revenueData:
    def __init__(self):
        self.coverGlassRev  = {"2-2.5mmGlass":3.75}
        self.backContactRev = {"Au(40nm)": 5.00, "Cu(150nm)": 0.34, "Ag": 0.71}
        self.absorberRev    = {"PbI":0.53, "PbSO":0.01}
        self.glassRev       = {"Glass":9.38}

    def getCoverGlassRev(self):
        return self.coverGlassRev

    def getBackContactRev(self):
        return self.backContactRev
    
    def getAbsorberRev(self):
        return self.absorberRev

    def getGlassRev(self):
        return self.glassRev

