import os # used for render hosting
from revenueData import *
from updateCharts import *
#from utils import *

app = dash.Dash(__name__)

#this is necessary for deployment on render
server = app.server

#load data
costData = costData()
revData = revenueData()

displayCostGraph(app, costData, revData)

update_cost_graph(app)
update_revenue_graph(app)

# Run the app
if __name__ == "__main__":
    #app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000))) #use for render hosting
    app.run(debug=True) #use for local development
