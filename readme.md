# researchMap
This is a python crawler program to grasp paper cited relationship from google scholar. 

The crawler first search google scholar by a origin paper name, and then get the url of page including papers cite the origin paper. Then grasp all the papers that cite the origin paper. In the next step, we will compare all the papers to papers already in mendeley researchMap group, if there are same papers, then we could make relationship between the papers with origin paper.

## Get Relationship between Papers
To run 
        <code>python main.py</code>
,a file named outcome.csv will be generated after successfully running.In this file there will be two rows, source and target. Source rows including source papers while target rows including papers cited by source papers.
