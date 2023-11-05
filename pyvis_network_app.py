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
import networkx as nx
import networkx as nx
from pyvis.network import Network


# Set header title
st.title('Network Graph Visualization of Drug-Drug hej Interactions')



nx_graph = nx.cycle_graph(10)
nx_graph.nodes[1]['title'] = 'Number 1'
nx_graph.nodes[1]['group'] = 1
nx_graph.nodes[3]['title'] = 'I belong to a different group!'
nx_graph.nodes[3]['group'] = 10
nx_graph.add_node(20, size=20, title='couple', group=2)
nx_graph.add_node(21, size=15, title='couple', group=2)
nx_graph.add_edge(20, 21, weight=5)
nx_graph.add_node(25, size=25, label='lonely', title='lonely node', group=3)

nt = Network('500px', '500px')
nt.from_nx(nx_graph)
nt.show('nx.html')

