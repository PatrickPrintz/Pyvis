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

# Define list of selection options and sort alphabetically
drug_list = ['Metformin', 'Glipizide', 'Lisinopril', ' Simvastatin',
            'Warfarin', 'Aspirin', 'Losartan', 'Ibuprofen']
drug_list.sort()

# Implement multiselect dropdown menu for option selection (returns a list)
selected_drugs = st.multiselect('Select drug(s) to visualize', drug_list)

# Set info message on initial site load
if len(selected_drugs) == 0:
    st.text('Choose at least 1 drug to start')

# Create network graph when user selects >= 1 item
else:
    # Create networkx graph object from pandas dataframe
    github_edgelist_url = 'https://raw.githubusercontent.com/CamillaSSvendsen/M2/main/congress.edgelist'

    # To get access to the data in the edgelist file from the GitHub repository, we use the urllib.request library.
    edgelist_file = urllib.request.urlopen(github_edgelist_url)

    # We then use the NetworkX library to read the edgelist as a directed graph (DiGraph) and define it G.
    G = nx.read_edgelist(edgelist_file, create_using=nx.DiGraph(), data=True)
    # We also load the json file containing an inList, inWeight, outList, outWeight, and usernameList.
    data = pd.read_json("https://raw.githubusercontent.com/CamillaSSvendsen/M2/main/congress_network_data.json")
    # From this file we are interested in the list of usernames.
    # In this step, we iterate through the edges of the graph G and add data to the DataFrame.
    # The for loop extracts the source node, the target node, and the weight for each edge in the graph, and assigns these values in the DataFrame.
    df = pd.DataFrame(columns=['Source', 'Target', 'Weight'])
    for a, b, wei in G.edges(data=True):
        source, target, weight = a, b, wei.get('weight', None)
        df = df.append({'Source': source, 'Target': target, 'Weight': weight}, ignore_index=True)
    
    # We create a new empty dataframe only consisting of column names "id" and "name"
    names_df = pd.DataFrame(columns=['node_id', 'name'])

    # We want to have a way to connect the usernames from the list in the json file to the nodes in the edgelist/dataframe.
    # We apply an index to the usernameList in the json file "data", and combine the node number in the graph to a username from the json file "data".
    i = 0
    for node in G.nodes():
        G.add_node(node, name=data['usernameList'][0][i])
        i += 1
    
    # We set up a networkx layout, to make sure, we get the same layout, evertime we load a visualization of a network.
    G_layout = nx.layout.kamada_kawai_layout(G)



    # Initiate PyVis network object
    drug_net = Network(
                       height='40px',
                       width='100%',
                       bgcolor='#333333',
                       font_color='blue'
                      )

    # Take Networkx graph and translate it to a PyVis graph format
    drug_net.from_nx(G)

    # Generate network with specific layout settings
    drug_net.repulsion(
                        node_distance=100,
                        central_gravity=0.90,
                        spring_length=11,
                        spring_strength=0.20,
                        damping=0.90
                       )

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
    components.html(HtmlFile.read(), height=800)

# Footer
st.markdown(
    """
    <br>
    <h6><a href="https://github.com/kennethleungty/Pyvis-Network-Graph-Streamlit" target="_blank">GitHub Repo</a></h6>
    <h6><a href="https://kennethleungty.medium.com" target="_blank">Medium article</a></h6>
    <h6>Disclaimer: This app is NOT intended to provide any form of medical advice or recommendations. Please consult your doctor or pharmacist for professional advice relating to any drug therapy.</h6>
    """, unsafe_allow_html=True
    )