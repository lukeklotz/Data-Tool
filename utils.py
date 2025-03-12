
# This file provides supporting functions sucg as getters and formatters
# as of 02/17/2025, these files support the data class

#from costGraphStyle import * 
#from revenueData import *

def formatTotalCost(coverGlass_cost, backContact_cost, absorber_cost, etl_cost):

    # Calculate the total cost
    total_cost = coverGlass_cost + backContact_cost + absorber_cost + etl_cost
    formatted_total_cost = round(total_cost, 2)

    return formatted_total_cost

'''
def getCoverGlassCost(coverGlass_method):
    data = Data()

    coverGlass = data.getCoverGlass()
    coverGlass_row = coverGlass[coverGlass["Method"] == coverGlass_method]
    coverGlass_cost = coverGlass_row["Cost"].values[0]

    return round(coverGlass_cost, 2)

def getBackContactCost(backContact_method): 
    data = Data()

    backContact = data.getBackContact() 
    backContact_row = backContact[backContact["Method"] == backContact_method]
    backContact_cost = backContact_row["Cost"].values[0]

    return round(backContact_cost, 2)

def getAbsorberCost(absorber_method):
    data = Data()

    absorber = data.getAbsorber() 
    absorber_row = absorber[absorber["Method"] == absorber_method]
    absorber_cost = absorber_row["Cost"].values[0]

    return round(absorber_cost, 2)

def getEtlCost(etl_method):
    data = Data()

    etl = data.getEtl() 
    etl_row = etl[etl["Method"] == etl_method]
    etl_cost = etl_row["Cost"].values[0]

    return round(etl_cost, 2)
 
'''