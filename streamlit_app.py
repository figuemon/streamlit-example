from collections import namedtuple

from numpy import size
from streamlit_agraph import agraph, Node, Edge, Config
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""


# with st.echo(code_location='below'): Print code 
total_points = st.number_input("Number of points in spiral", 1, 5000, 2000)
num_turns = st.slider("Number of turns in spiral", 1, 100, 9)

Point = namedtuple('Point', 'x y')
data = []

points_per_turn = total_points / num_turns

for curr_point_num in range(total_points):
    curr_turn, i = divmod(curr_point_num, points_per_turn)
    angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
    radius = curr_point_num / total_points
    x = radius * math.cos(angle)
    y = radius * math.sin(angle)
    data.append(Point(x, y))

st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
    .mark_circle(color='#0068c9', opacity=0.5)
    .encode(x='x:Q', y='y:Q'))
column_nodes = pd.read_csv("./ScannerResults/2022-03-03-15-25/GraphFormatFiles/SQLColumnNode.csv")
table_nodes = pd.read_csv("./ScannerResults/2022-03-03-15-25/GraphFormatFiles/SQLTableNode.csv")
view_nodes = pd.read_csv("./ScannerResults/2022-03-03-15-25/GraphFormatFiles/SQLViewNode.csv")
procedure_nodes = pd.read_csv("./ScannerResults/2022-03-03-15-25/GraphFormatFiles/SQLProcedureNode.csv")
file_nodes = pd.read_csv("./ScannerResults/2022-03-03-15-25/GraphFormatFiles/FileNode.csv")

edges_data = pd.read_csv("./ScannerResults/2022-03-03-15-25/GraphFormatFiles/HasColumnRelationship.csv")
edges_references = pd.read_csv("./ScannerResults/2022-03-03-15-25/GraphFormatFiles/ReferencesRelationship.csv")
edges_contains = pd.read_csv("./ScannerResults/2022-03-03-15-25/GraphFormatFiles/ContainsRelationship.csv")



nodes = []
edges = []

for  index,node in column_nodes.iterrows():
    nodes.append(Node(
        id=node["id:ID"],
        label=node["Name"],
        size= 400,
        symbolType='square'
    ))

for index,node in table_nodes.iterrows():
    nodes.append(Node(
        id=node["id:ID"],
        label=node["Name"],
        size= 400,
        symboltype='triangle'
    ))
    
for  index,node in view_nodes.iterrows():
    nodes.append(Node(
        id=node["id:ID"],
        label=node["Name"],
        size= 400
    ))

for  index,node in procedure_nodes.iterrows():
    nodes.append(Node(
        id=node["id:ID"],
        label=node["Name"],
        size= 400
    ))

for  index,node in file_nodes.iterrows():
    nodes.append(Node(
        id=node["id:ID"],
        label=node["id:ID"],
        size= 400,
        svg="https://mobilizeux.blob.core.windows.net/bifrost/CSV_icon_light.svg"
    ))


for  index,edge in edges_data.iterrows():
    edges.append(Edge(
        source= edge[":START_ID"],
        target= edge[":END_ID"],
        label = "Sample Relation",
    ))
for  index,edge in edges_references.iterrows():
    edges.append(Edge(
        source= edge[":START_ID"],
        target= edge[":END_ID"],
        label = "Sample Relation",
    ))
for  index,edge in edges_contains.iterrows():
    edges.append(Edge(
        source= edge[":START_ID"],
        target= edge[":END_ID"],
        label = "Sample Relation",
    ))
config = Config(width=1000, 
                height=1500, 
                directed=True,
                nodeHighlightBehavior=True, 
                highlightColor="#F7A7A6", # or "blue"
                backgroundColor="#85aff2",
                collapsible=True,
                node={'labelProperty':'label'},
                link={'labelProperty': 'label', 'renderLabel': True}
                # **kwargs e.g. node_size=1000 or node_color="blue"
                )
agraph(nodes=nodes, 
                      edges=edges, 
                      config=config)
st.title("SQL Retrieved Nodes")
st.write(nodes)