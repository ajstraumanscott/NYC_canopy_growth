# 604 Final Project Flow Chart Diagram

from graphviz import Digraph

# Create Digraph object
dot = Digraph()

# Set node and edge styles
dot.attr("node", fontname="Handlee")
dot.attr("edge", fontname="Handlee")

# Define nodes and edges
dot.node("init", "Initialize Environment with Original Canopy", shape="rect")
dot.node("check_spots", "Planting Spots Available?", shape="oval")
dot.node("plant_trees", "Plant Saplings", shape="rect")
dot.node("grow_trees", "Grow All Trees", shape="rect")
dot.node("calc_canopy", "Calculate Canopy Coverage", shape="rect")
dot.node("hit_goal", "Does canopy cover 30%?", shape="oval")
dot.node("year", "Is it 2035?", shape="oval")
dot.node("update_year", "Update Year", shape="rect")
dot.node("end", "End Simulation", shape="diamond")

dot.edge("init", "check_spots")
dot.edge("check_spots", "end", label="No")
dot.edge("check_spots", "plant_trees", label="Yes")
dot.edge("plant_trees", "grow_trees")
dot.edge("grow_trees", "calc_canopy")
dot.edge("calc_canopy", "hit_goal")
dot.edge("hit_goal", "year", label="No")
dot.edge("hit_goal", "end", label="Yes")
dot.edge("year", "update_year", label="No")
dot.edge("year", "end", label="Yes")
dot.edge("update_year", "check_spots")

# Save as PNG
dot.render("canopy_simulation", format="png", cleanup=True)
