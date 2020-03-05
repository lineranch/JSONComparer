import sys, json
from scipy import spatial

"""
Python File Abstract 
    Turn both of the documents into vectors and calculate similarity

Details    
    Create a bag for each JSON document
    Create a set of all possible values between both JSON documents
    Turn each bag into a vector based on the set
    Calculate the similarity between the vectors
    
Side Note
    This file uses scipy to calculate the cosine similarity
    
Author
    Hunter Line
"""


# Create dictionaries of the JSON file
def readJson(file):

    with open(file, 'r') as f:
        JSON = json.load(f)

    return JSON

# This function will recursively add every possible data value to it's respective JSON bag
def createBag(JSON, key, bag):

    if isinstance(JSON, dict):
        for k, v in JSON.items():
            if isinstance(v, (dict,list)):
                createBag(v, key, bag)
            else:
                bag.append(v)
    elif isinstance(JSON, list):
        for i in JSON:
            createBag(i, key, bag)
    else:
        bag.append(JSON[key])

# This function will return a number between 0 and 1 based off of the similarity between the two vectors
def compareJSONFiles(JSON1, JSON2):

    bagJSON1, bagJSON2, bank = [], [], []

    # Create a bag for each JSON
    for key in JSON1.keys():
        createBag(JSON1, key, bagJSON1)

    for key in JSON2.keys():
        createBag(JSON2, key, bagJSON2)

    # Turn each JSON into a vector
    bank = list(set().union(bagJSON1, bagJSON2))
    vectorJSON1 = dict().fromkeys(bank, 0)
    vectorJSON2 = dict().fromkeys(bank, 0)

    # Add values to the vectors
    for i in bagJSON1:
         vectorJSON1[i] += 1

    for i in bagJSON2:
         vectorJSON2[i] += 1

    vectorJSON1 = list(vectorJSON1.values())
    vectorJSON2 = list(vectorJSON2.values())

    # Using algebraic properties of the dot product, return the similarity calculation
    return 1 - spatial.distance.cosine(vectorJSON1, vectorJSON2)

def main():
    # Read JSON documents via command line
    JSON1 = readJson(sys.argv[1])
    JSON2 = readJson(sys.argv[2])

    print(compareJSONFiles(JSON1, JSON2))

if __name__ == '__main__':
    main()