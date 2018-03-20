import numpy as np
import sys

def notValue(value):
    if value == 1:
        return 0
    return 1

def main():
    training_examples = np.loadtxt(sys.argv[1])
    X = training_examples[:len(training_examples) ,:len(training_examples[0]) - 1]
    Y = training_examples[:len(training_examples), len(training_examples[0]) - 1 :]
    d = len((training_examples[0])) - 1
    h = []



    for i in range(2*d):
        h.append(1)

    for example, tag in zip(X, Y):
        predicted_y = 1
        for i in range(d):
            if h[2*i] == 1:
                predicted_y *= int(example[i])
            elif h[2*i + 1] == 1:
                predicted_y *= notValue(int(example[i]))

        if tag == 1 and predicted_y == 0:
            for i in range(d):
                if example[i] == 1:
                    h[2*i + 1] = 0
                else:
                    h[2*i] = 0
    ans = ""
    for i in range(d):
        if h[2*i] == 1:
            ans = ans + "x" + str(i+1) + ","
        elif h[2*i + 1] == 1:
            ans = ans + "not(x" + str(i+1) + ")" + ","
    ans = ans.strip(",")
    print(ans)

    file = open("output.txt","w")
    file.writelines(ans)

if __name__ == "__main__":
    main()
