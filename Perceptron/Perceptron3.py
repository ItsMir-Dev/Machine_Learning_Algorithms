#Artificial neural networks
#Perceptron Algorithm implementation in python
#Agravat Mir
#P15/42692/2017
#University of Nairobi, 2019


from csv import reader

#opening the csv file
def load_csv(filename):
    dataset = list()
    with open(filename, 'r') as file:
        csv_reader = reader(file)
        #this reads the file line by line and puts the rows into a list called dataset
        for row in csv_reader:
            if not row:
                continue
            dataset.append(row)
    return dataset


def activation(dataset):
    #set the bias for the first epoch
    b = 1
    #sets the learning rate for the algorithm
    m = 0.1
    #a count to know how many epochs the algorithm loops through
    count = 0

    #taking every element in the dataset
    for i in dataset:
        #calculate the activation of the perceptron. This is used to get the actual output for the input
        prod = float(i[0]) * float(i[1]) + b

        #this is a step that sets the output based on threshold values
        #if the activation output is greater than 0, it is set to 1. It is set to 0 is activation output is less than 0
        if prod > 0:
            a_output = 1

            #when the activation output is not 1
            if a_output != int(i[-1]) and count <= 100:
                #calculate the error in output
                error = float(i[2]) - a_output
                #the bias changes based on the error
                b = b + m * error

                #adjust the weight of the input in question
                weight = float(i[1]) + error * m * float(i[0])\

                #uodate the weight in the dataset
                i.remove(i[1])
                i.insert(1, weight)

                #increment the epoch number
                count = count + 1
            else:
                continue
        elif prod < 0:
            #if the product is less than 0, the activation output is set to 0
            a_output = 0
            #Adjust weights if the activation output is not 0
            if a_output != int(i[-1]) and count <= 100:
                #calculate the error in outputs
                error = float(i[2]) - a_output
                #change in the bias in input
                b = b + m * error
                #adjust the weight for the inout in question
                weight = float(i[1]) + error * m * float(i[0])
                #replace the weight in the dataset
                i.remove(i[1])
                i.insert(1, weight)
                #increment the epoch
                count = count + 1
            else:
                continue
        else:
            break
    #code for plotting the dataset into a graph
    #has classification error
    #if you can help in solving this it will be greatly appreciated
    #submit rectified errors to itsmir@studetns.uonbi.ac.ke
    """xb = []
    yb = []
    xr = []
    yr = []
    for i in dataset:
        if int(i[2]) == 0:
            for _ in i:
                x1 = float(i[0])
                y1 = float(i[1])
                xb.append(x1)
                yb.append(y1)
        elif int(i[2]) == 1:
            for _ in i:
                x1 = float(i[0])
                y1 = float(i[1])
                xr.append(x1)
                yr.append(y1)

    plt.plot(xr,yr, 'ro', xb,yb,'bo')
    plt.show()
    return"""

#function that runs the program
def prog():
    #loads the .csv file into the algorithm
    dataset = load_csv("data3.csv")
    #run the activation fucntion on the dataset list created
    activation(dataset)
    #print the new dataset with updated weights
    for i in dataset:
        print(i)
    exit(0)

#run the program
prog()