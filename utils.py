
# This file provides supporting functions sucg as getters and formatters
# as of 02/17/2025, these files support the data class

#from costGraphStyle import * 
#from revenueData import *

def formatTotalCost(htl_cost, backContact_cost, absorber_cost, etl_cost):

    # Calculate the total cost
    total_cost = htl_cost + backContact_cost + absorber_cost + etl_cost
    formatted_total_cost = round(total_cost, 2)

    return formatted_total_cost
