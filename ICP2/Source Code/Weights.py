def lbstokgs():
    input_string = input("Enter a number of weights:- ")
    input_weights = []
    for i in range(int(input_string)):
        input_weights.append(input())
    output_weights = []
    for x in input_weights:
        output_weights.append(float(x)*0.453592)
    print("The Weights in lbs are are", input_weights)
    print("The Weights in kgs are", output_weights)


lbstokgs()
