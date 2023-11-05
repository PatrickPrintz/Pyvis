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

st.write("""
         We have chosen to work with the "*Twitter Interaction Network for the US Congress*" dataset.

Data stems from SNAP which is a Stanford Large Network Dataset Collection.

From the webpage the dataset is described like this:\n



* This network represents the Twitter interaction network for the 117th United States Congress, both House of Representatives and Senate. The base data was collected via the Twitter’s API, then the empirical transmission probabilities were quantified according to the fraction of times one member retweeted, quote tweeted, replied to, or mentioned another member’s tweet.

From the webpage we also get the folloing dataset statistics:



* We know that the dataset consist of 475 nodes and 13.289 edges. We also know that the edges are directed and that there are edge features in form of weights. \n

The dataset doesn't have any attribes for the nodes besides the username for the Twitter account. This limited information about the nodes leads to several challenges and limitations in the network analysis.\n

Since network analysis often relies on the characteristics of the nodes to gain useful insights about the network.\n

Without node characteristics, it becomes difficult to perform attribute-based network analysis. This includes identifying influential nodes based on their attributes, such as age, gender, race, or state, which could have contributed with useful infromation in an analysis. Limitation of node characteristics reduces the interpretability of the analysis. E.g you can calculate different centralities for the nodes within the network, and highlight some key nodes, but when you do not have charateristics for the nodes, it becomes difficult to analyze if the nodes have some similarities.\n
\n\n
Some of the attributes for the nodes that could have contributed with insightful information for this dataset would be:\n
* State the originates from/represent.
* Gender
* Age
* Race
* Years of experience in the U.S. Congress
         """)

st.write("""

    In this app you can see a network analysis of the Twitter interactions between US Congress members. \n
    
         
    Pick the kind of Centrality you would like to look at from the dropdown menu and become informed 

         """)
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


if visualization_option == "In-Degree Centrality":
 st.write("In-degree centrality measures how many incoming connections that are directed towards a node. It tells us how many other nodes are connected to that node compared to all the possible incoming connections.")
 st.write("A high in-degree centrality in this graph means that a lot of the other people in the network retweets, quote-tweets, reponds to, and mentions your tweet.")
 st.write("In-degree centrality is calculated as the number of actual incoming edges to a node compared to all the possible incoming edges.")
 st.image("https://github.com/SeniorHreff/M2-Assignment/blob/main/Screenshots%20til%20app/Indegree%20tabel.JPG?raw=true")

elif visualization_option == "Out-Degree Centrality":
 st.write("Out-degree centrality measures how many outgoing connections a node has. It tells us how many other nodes that node is connected to.")
 st.write("A high out-degree centrality in this graph means that the person retweets, quote-tweets, reponds to, and/or mentions a lot of different people's tweets.")
 st.write("Out-degree centrality is calculated as the number of actual outgoing edges to a node compared to all the possible outgoing edges.")
 st.image("https://github.com/SeniorHreff/M2-Assignment/blob/main/Screenshots%20til%20app/Outdegree%20tabel.JPG?raw=true")

elif visualization_option == "Eigenvector Centrality":
 st.write("Eigenvector centrality is a key concept in network analysis. It is used to measure the influence or importance of nodes in the network. It is useful for identifying nodes that are not only well-connected but also connected to other highly central nodes. Eigenvector centrality is based on the idea that the importance of a node is determined by the importance of its neighbors.")
 st.write("Eigenvector centrality assigns a centrality score to each node in the network. This score is based on both the nodes own centrality value and the centrality value of the neighboring nodes.")
 st.image("https://github.com/SeniorHreff/M2-Assignment/blob/main/Screenshots%20til%20app/Eigenvector%20tabel.JPG?raw=true")

elif visualization_option == "Betweenness Centrality":
 st.write("""
Betweenness centrality is about detecting which nodes are crucial for the flow between nodes. Nodes with high betweenness centrality are like bridges between other pairs of nodes in the network. \n
It measures how frequently a node lies on the shortest paths between pairs of other nodes in the network.\n
To calculate the betweenness centrality of a node, you consider all pairs of nodes in the network and count how many times the node in question falls on the shortest path between them. The more often it's on these paths, the higher its betweenness centrality.\n
          """)

 
 st.image("https://github.com/SeniorHreff/M2-Assignment/blob/main/Screenshots%20til%20app/Betwenness%20tabel.JPG?raw=true")

elif visualization_option == "Community Detection":
 st.write("Community detection helps reveal the network's modular or hierarchical organization by identifying groups of nodes (communities) that are more densely connected to each other than to the rest of the network.")
 st.write("Community detection can also help to more easily identify if the network has outliers in form of nodes that do not share characteristics with other nodes or are less connected than other nodes in the network.")
 st.write("All nodes in a community does not have to be directly connected to each other")
 st.image("https://github.com/SeniorHreff/M2-Assignment/blob/main/Screenshots%20til%20app/Community%20tabel.JPG?raw=true")


with st.expander("If you want to see our Network analysis of the key node from Truth Social ") :
    st.image("https://media.newyorker.com/photos/64e7fb05eeb2b9a4560ab8c9/master/w_2560%2Cc_limit/Trump-Mugshot-Final.jpg")