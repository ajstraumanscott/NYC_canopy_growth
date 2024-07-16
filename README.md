# NYC Tree Canopy Simulation

data604_final

by AJ Strauman-Scott

For CUNY SPS Summer 2024

## Project Overview

This repository contains the final project for the Data 604 course at CUNY SPS, Summer 2024, completed by AJ Strauman-Scott. The project involves simulating the growth of New York City's urban canopy as saplings are planted and time passes. The goal is to achieve the NYC Urban Forest Agenda's June 2021 goal to achieve 30% tree canopy coverage across the city's land area by 2035.

## Files in the Repository

1. [strauman-scott_nyc_tree_canopy_simulation.pdf](githublink here) - A detailed document outlining the simulation, methodology, and findings.
2. [strauman-scott_nyc_tree_canopy_simulation.ipynb](github link here) - The Jupyter Notebook containing the simulation code.
3. [strauman-scott_nyc_tree_canopy_slidedeck.pdf](github link here) - The slidedeck presentation summarizing the project and its findings.

## Assignment Instructions

The project involved creating a discrete event simulation using SimPy, focusing on the following elements:

1. **State the Problem and Its Significance**
2. **Provide a Flow-Chart Model**
3. **Simulate the Process for Appropriate Iterations**
4. **Justify the Validity of the Model**
5. **State Conclusions and Findings**
6. **Generate Appropriate Graphs**

## Project Outline

The model recreates the currently NYC canopy and then plants trees and models their growth to determine how many much be planted each year to achieve the desired canopy coverage/

A simulation was developed using Python and the SimPy package. It includes:
- Initialization of environment and variables
- Computation of existing canopy growth based on observed changes from 2010 to 2017
- Modeling of growth of existing canopy plus growth of saplings (consisting of five different randomly assigned tree species with varying growth rates) planted during previous years.

An parameter sweep was conducted to find the minimum number of saplings that can be planted each year to achieve 30% canopy coverage. 

When the sweep returned values that exceeded the number of available planting spots in the city, the model was expanded to plant a tree in every available spot by 2035 and continue to monitor growth until 30% canopy is achieved.

The model was validated using historical data comparison and sensitivity analysis.

---

**Works Cited**

Department of Parks and Recreation (DPR). n.d. “Forestry Planting Spaces.” https://opendata.cityofnewyork.us/.
NYC Parks. 2020. “Tracking the Tree Canopy.” https://storymaps.arcgis.com/stories/5353de3dea91420faaa7faff0b32206b.
———. 2021. “Tree Procurement.” https://static.nycgovparks.org/images/pagefiles/52/Tree_Procurement.pdf.
———. 2023. “NYC Parks Announces Highest Tree Planting Total in Six Years.” Press Release. https://www.nycgovparks.org/news/press-releases?id=22083.
Treglia, M. L., M. Acosta-Morel, D. Crabtree, K. Galbo, T. Lin-Moges, A. Van Slooten, and E. N. Maxwell. 2021. “The State of the Urban Forest in New York City.” The Nature Conservancy. https://doi.org/10.5281/zenodo.5532876.