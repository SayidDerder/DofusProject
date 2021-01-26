from Map import Map

def LoadMap(MapName: str):

    # Open txt file of map
    f = open('Maps/'+MapName+'.txt', 'r')
    
    # read the lines
    f1 = f.readlines()
    
    # Init the map variables
    name = ""
    positions = []
    
    # loop for each line in the .txt file
    for i, line in enumerate(f1):
        # First line is name
        if i == 0:
           name = line
        
        # Other lines are positions
        else:
            # Split the values
            pos = line.split()
            
            # Append to list in correct format
            positions.append((float(pos[0]), float(pos[1])))
    
    return Map(name, positions)

