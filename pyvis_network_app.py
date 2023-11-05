import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import networkx as nx
from pyvis.network import Network
import pyvis
import json
import urllib.request # This library is used to get access to the edgelist file in the GitHub repository
from pyvis.network import Network
import holoviews as hv
from holoviews import opts
hv.extension('bokeh')
from bokeh.plotting import show


import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import networkx as nx
from pyvis.network import Network


# Set header title
st.title('Network Graph Visualization of Drug-Drug Interactions')

github_edgelist_url = 'https://raw.githubusercontent.com/CamillaSSvendsen/M2/main/congress.edgelist'

# To get access to the data in the edgelist file from the GitHub repository, we use the urllib.request library.
edgelist_file = urllib.request.urlopen(github_edgelist_url)

# We then use the NetworkX library to read the edgelist as a directed graph (DiGraph) and define it G.
G = nx.read_edgelist(edgelist_file, create_using=nx.DiGraph(), data=True)

# We also load the json file containing an inList, inWeight, outList, outWeight, and usernameList.
data = pd.read_json("https://raw.githubusercontent.com/CamillaSSvendsen/M2/main/congress_network_data.json")

# From this file, we are interested in the list of usernames.
# In this step, we iterate through the edges of the graph G and add data to the DataFrame.
# The for loop extracts the source node, the target node, and the weight for each edge in the graph and assigns these values in the DataFrame.
df = pd.DataFrame(columns=['Source', 'Target', 'Weight'])
for a, b, wei in G.edges(data=True):
    source, target, weight = a, b, wei.get('weight', None)
    df = df._append({'Source': source, 'Target': target, 'Weight': weight}, ignore_index=True)

# We create a new empty dataframe only consisting of column names "id" and "name"
names_df = pd.DataFrame(columns=['node_id', 'name'])

# We want to have a way to connect the usernames from the list in the json file to the nodes in the edgelist/dataframe.
# We apply an index to the usernameList in the json file "data", and combine the node number in the graph to a username from the json file "data".
i = 0
for node in G.nodes():
    G.add_node(node, name=data['usernameList'][0][i])
    i += 1
    
# We set up a networkx layout, to make sure, we get the same layout, evertime we load a visualization of a network.


import gravis as gv
import networkx as nx

g = nx.cycle_graph(10)
g.graph['node_color'] = 'blue'
g.nodes[1]['title'] = 'Number 1'
g.nodes[1]['group'] = 1
g.nodes[3]['title'] = 'I belong to a different group!'
g.nodes[3]['group'] = 10
g.nodes[3]['color'] = 'orange'
g.add_node(20, size=20, title='couple', group=2, color='red')
g.add_node(21, size=15, title='couple', group=2, color='red')
g.add_edge(20, 21, weight=5)
g.add_node(25, size=25, label='lonely', title='lonely node', group=3, color='green')

gv.d3(g)
HtmlFile = open(gv.d3(g), encoding='utf-8')
components.html(HtmlFile.read(), height=1200)
