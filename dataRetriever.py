import csv

movementIndex = None
step = 0
threshold = 0.935

dataLibrary = []

def findMovement(inputString):
    global movementIndex, step

    #if there is a movement index 
    if movementIndex != None:
        print("foo")
        #TODO make the remaining step finding function
        similarity_of_movement = similarity(inputString, dataLibrary[movementIndex][step])
        if similarity_of_movement > threshold and len(dataLibrary[movementIndex])-1 > step:
            step += 1
            #if its at the last step
            if len(dataLibrary[movementIndex])-1 == step:
                #print movement name
                print(dataLibrary[movementIndex][step])
                #reset
                step = 0
                movementIndex = None
        else:
            step = 0
            movementIndex = None
    
    #else if there isnt't a movement index
    else:
        movementIndex = index_through_similarity(inputString)
        try:
            print(f"index: {movementIndex} | Similarity: {similarity(inputString, dataLibrary[movementIndex][0])}")
        except Exception as e:
            print(e)

        step += 1
            
            

def index_through_similarity(inputString):
    maxLikeness = 0
    index = None
    #compare all data with library data
    for i in range(len(dataLibrary)):
        #find similarity
        
        similarityVal = similarity(string, str(dataLibrary[i][0]))
        print(similarityVal, i)
        if  similarityVal > threshold:
            #if its greater than the likeness then add the index
            if similarityVal > maxLikeness:
                index = i
    return index

"""Return the similarity of two given strings in decimal """
def similarity(given, compare):
    #total
    total = len(given)
    
    
    same = 0
    try:
        
        #if they are not of the same length terminate
        #if they are not the same hand terminate
        if(total != len(compare)):
            return -1
        
        if given[total - 2] != compare[total - 2]:
            return -1
    except:
        print('error with similarity input variables')
        exit()
    
    #compare and add to same counter
    for i in range(len(given)):
        if given[i] == compare[i]:
            same += 1
    
    #calculate percentage similarity and return
    return (same/total)

def initialize():
    try:
        with open("./data.csv", 'r') as f:
            csv_reader = csv.reader(f)

            for row in csv_reader:
                dataLibrary.append(row)
                
    except Exception as e:
        print(e)