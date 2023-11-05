import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import networkx as nx
from pyvis.network import Network
import urllib.request

# Read dataset (CSV)
# Set header title
st.title('Network Graph Visualization of Drug-Drug Interactions')

# Define list of selection options and sort alphabetically
drug_list = ['Metformin', 'Glipizide', 'Lisinopril', 'Simvastatin',
            'Warfarin', 'Aspirin', 'Losartan', 'Ibuprofen']
drug_list.sort()

# Implement multiselect dropdown menu for option selection (returns a list)
selected_drugs = st.multiselect('Select drug(s) to visualize', drug_list)

# Set info message on initial site load
if len(selected_drugs) == 0:
    st.text('Choose at least 1 drug to start')

# Create network graph when user selects >= 1 item
else:
    #G = nx.cycle_graph(10)
    github_edgelist_url = 'https://raw.githubusercontent.com/CamillaSSvendsen/M2/main/congress.edgelist'

    # To get access to the data in the edgelist file from the GitHub repository, we use the urllib.request library.
    edgelist_file = urllib.request.urlopen(github_edgelist_url)

    # We then use the NetworkX library to read the edgelist as a directed graph (DiGraph) and define it G.
    G = nx.read_edgelist(edgelist_file, create_using=nx.DiGraph(), data=True)
    # Create networkx graph object from pandas dataframe
    in_degree_centrality = nx.in_degree_centrality(G)

    # We then sort the nodes by in-degree centrality in descending order.
    in_sorted_nodes = sorted(in_degree_centrality, key=in_degree_centrality.get, reverse=True)

    # In the last line of code we define the subgraph to include the 75 node with the highest in-degree centrality.
    in_subgraph = G.subgraph(in_sorted_nodes[:10])
    
    # Initiate PyVis network object
    drug_net = Network(
                       height='400px',
                       width='100%',
                       bgcolor='#222222',
                       font_color='white'
                      )

    # Take Networkx graph and translate it to a PyVis graph format
    drug_net.from_nx(in_subgraph)

    # Generate network with specific layout settings
    drug_net.repulsion(
                        node_distance=420,
                        central_gravity=0.33,
                        spring_length=110,
                        spring_strength=0.10,
                        damping=0.95
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
    components.html(HtmlFile.read(), height=435)

# Footer
st.markdown(
    """
    <br>
    <h6><a href="https://github.com/kennethleungty/Pyvis-Network-Graph-Streamlit" target="_blank">GitHub Repo</a></h6>
    <h6><a href="https://kennethleungty.medium.com" target="_blank">Medium article</a></h6>
    <h6>Disclaimer: This app is NOT intended to provide any form of medical advice or recommendations. Please consult your doctor or pharmacist for professional advice relating to any drug therapy.</h6>
    """, unsafe_allow_html=True
    )