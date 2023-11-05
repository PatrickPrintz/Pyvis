import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import networkx as nx
from pyvis.network import Network
import urllib.request

github_edgelist_url = 'https://raw.githubusercontent.com/CamillaSSvendsen/M2/main/congress.edgelist'

# To get access to the data in the edgelist file from the GitHub repository, we use the urllib.request library.
edgelist_file = urllib.request.urlopen(github_edgelist_url)

# We then use the NetworkX library to read the edgelist as a directed graph (DiGraph) and define it G.
G = nx.read_edgelist(edgelist_file, create_using=nx.DiGraph(), data=True)



st.title("Network Analysis for Twitter interactions for the US Congress")

st.header("In this app you can see a network analysis of the Twitter interactions between US Congress members. Pick the kind of Centrality you would like to look at from the dropdown menu and become informed", divider = "gray")


visualization_option = st.selectbox(
    "Select Visualization", 
    ["In-Degree Centrality",
     "Out-Degree Centrality",
     "Eigenvector Centrality",
     "Betweenness Centrality",
     "Community Detection"
    ]
)

# Set info message on initial site load
if visualization_option == "In-Degree Centrality":
    in_degree_centrality = nx.in_degree_centrality(G)
    in_sorted_nodes = sorted(in_degree_centrality, key=in_degree_centrality.get, reverse=True)
    in_subgraph = G.subgraph(in_sorted_nodes[:55])
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



elif visualization_option == "Out-Degree Centrality":
    # The first step in this process is to define the out-degree centrality for the nodes in G.
    out_degree_centrality = nx.out_degree_centrality(G)

    # We then sort the nodes by out-degree centrality in descending order.
    out_sorted_nodes = sorted(out_degree_centrality, key=out_degree_centrality.get, reverse=True)

    # In the last line of code we define the subgraph to include the 75 node with the highest out-degree centrality.
    out_subgraph = G.subgraph(out_sorted_nodes[:55])
       # Initiate PyVis network object
    drug_net = Network(
                       height='400px',
                       width='100%',
                       bgcolor='#222222',
                       font_color='white'
                      )

    # Take Networkx graph and translate it to a PyVis graph format
    drug_net.from_nx(out_subgraph)

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


elif visualization_option == "Eigenvector Centrality":
    # The first step in this process is to define the eigenvector centrality for the nodes in G.
    cent_eigen = nx.eigenvector_centrality(G)

    # We then sort the nodes by eigenvector centrality in descending order.
    eigen_sorted_nodes = sorted(cent_eigen, key=cent_eigen.get, reverse=True)

    # In the last line of code we define the subgraph to include the 75 node with the highest eigenvector centrality.
    eigen_subgraph = G.subgraph(eigen_sorted_nodes[:55])
       # Initiate PyVis network object
    drug_net = Network(
                       height='400px',
                       width='100%',
                       bgcolor='#222222',
                       font_color='white'
                      )

    # Take Networkx graph and translate it to a PyVis graph format
    drug_net.from_nx(eigen_subgraph)

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


elif visualization_option == "Betweenness Centrality":
    # The first step in this process is to define the betweenness centrality for the nodes in G.
    cent_between = nx.betweenness_centrality(G)

    # We then sort the nodes by betweenness centrality in descending order.
    between_sorted_nodes = sorted(cent_between, key=cent_between.get, reverse=True)

    # In the last line of code we define the subgraph to include the 75 node with the highest betweenness centrality.
    between_subgraph = G.subgraph(between_sorted_nodes[:55])

       # Initiate PyVis network object
    drug_net = Network(
                       height='400px',
                       width='100%',
                       bgcolor='#222222',
                       font_color='white'
                      )

    # Take Networkx graph and translate it to a PyVis graph format
    drug_net.from_nx(between_subgraph)

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

elif visualization_option == "Community Detection":
    
    G_undirected = G.to_undirected()
    eigenvector_centrality = nx.eigenvector_centrality(G_undirected)

    # We then sort the nodes by eigenvector centrality in descending order, and define the top 75 nodes.
    top_nodes = sorted(eigenvector_centrality, key=eigenvector_centrality.get, reverse=True)[:55]

    # In the last line of code we define the subgraph to include the 75 node with the highest betweenness centrality.
    subgraph = G_undirected.subgraph(top_nodes)



       # Initiate PyVis network object
    drug_net = Network(
                       height='400px',
                       width='100%',
                       bgcolor='#222222',
                       font_color='white'
                      )

    # Take Networkx graph and translate it to a PyVis graph format
    drug_net.from_nx(subgraph)

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


