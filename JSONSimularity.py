import sys, json

# Create dictionaries of the JSON file
def readJson(file):
    with open(file, 'r') as f:
        JSON = json.load(f)

    return JSON

def compareJSONFiles(JSON1, JSON2):
    return None

def main():
    JSON1 = readJson(sys.argv[1])
    JSON2 = readJson(sys.argv[2])

    print(JSON1['breweries'][0])
    #print(JSON2['state'])

    print(compareJSONFiles(JSON1, JSON2))

if __name__ == '__main__':
    main()