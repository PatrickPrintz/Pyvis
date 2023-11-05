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


# We define the URL for the raw edgelist file from our created GitHub repository..
github_edgelist_url = 'https://raw.githubusercontent.com/CamillaSSvendsen/M2/main/congress.edgelist'

# To get access to the data in the edgelist file from the GitHub repository, we use the urllib.request library.
edgelist_file = urllib.request.urlopen(github_edgelist_url)

# We then use the NetworkX library to read the edgelist as a directed graph (DiGraph) and define it G.
G = nx.read_edgelist(edgelist_file, create_using=nx.DiGraph(), data=True)
# The default is undirected graph.
# data=True is necessary since the edgelist file contains additional information (data) associated with the edges. The additional information is weight.



# Read dataset (CSV)

# Set header title
st.title('Network Graph Visualization of Drug-Drug Interactions')

# Initiate PyVis network object
drug_net = Network()


# Take Networkx graph and translate it to a PyVis graph format
drug_net.from_nx(G)

# Generate network with specific layout settings
drug_net.repulsion(node_distance=420)
# Save and read graph as HTML file (on Streamlit Sharing)

try:
    path = '/tmp'
    drug_net.save_graph(f'{path}/pyvis_graph.html')
    HtmlFile = open(f'{path}/pyvis_graph.html', 'r', encoding='utf-8')

    # Save and read graph as HTML file (locally)
except:
    path = '/html_files'
    drug_net.save_graph(f'{path}/pyvis_graph.html')
    HtmlFile = open(f'{path}/pyvis_graph.html', 'r', encoding='utf-8')


# Load HTML file in HTML component for display on Streamlit page
components.html(HtmlFile.read(), height=435)