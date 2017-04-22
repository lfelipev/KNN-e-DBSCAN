import csv
import math
from random import shuffle

class flower():
    def __init__(self, sepal_l, sepal_w, petal_l, petal_w, type):
        self.sepal_l = sepal_l
        self.sepal_w = sepal_w
        self.petal_l = petal_l
        self.petal_w = petal_w
        self.type = type

def euclidian(subject1, subject2):
    sum = pow(subject1.sepal_l - subject2.sepal_l, 2) + \
            pow(subject1.sepal_w - subject2.sepal_w, 2) + \
            pow(subject1.petal_l - subject2.petal_l, 2) + \
            pow(subject1.petal_w - subject2.petal_w, 2)
    result = math.sqrt(sum)

    return result

def classify(subjects, subject, k):
    if k%2 == 0:
        k = k - 1
        if k <= 0:
            k = 1

    index = 0

    dist_tuple = []

    for i in subjects:
        dist = euclidian(i, subject)
        dist_tuple.append((dist, index))
        dist_tuple.sort(key=lambda tup: tup[0])
        index = index + 1

    types = [0,0,0]
    countK = 0

    for j in dist_tuple:
        if countK == k:
            break

        type = subjects[j[1]].type

        if type == "Iris-setosa":
            types[0] = types[0] + 1
        elif type == "Iris-versicolor":
            types[1] = types[1] + 1
        else:
            types[2] = types[2] + 1

        countK = countK + 1

    if types[0] >= types[1] and types[0] >= types[2]:
        type_classified = "Iris-setosa"
    elif types[1] >= types[0] and types[1] >= types[2]:
        type_classified = "Iris-versicolor"
    else:
        type_classified = "Iris-virginica"

    return type_classified

def main():
    subjects = list()
    trainning_subjects = list()
    k = 7
    accuracy = 0
    vp = 0
    trainning = 100
    tests = 150 - trainning

    matrix = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]

    with open('iris.csv', 'r') as csvfile:
        lines = csv.reader(csvfile)
        for row in lines:
            subjects.append(flower(float(row[0]), float(row[1]), float(row[2]), float(row[3]), row[4]))

    shuffle(subjects)

    for i in range(0,trainning):
        trainning_subjects.append(subjects[i])

    for j in range(trainning, 150):
        subject = subjects[j]

        type = classify(trainning_subjects, subject, k)

        if subject.type == type:
            vp = vp + 1
            if type == "Iris-setosa":
                matrix[0][0] = matrix[0][0] + 1
            elif type == "Iris-versicolor":
                matrix[1][1] = matrix[1][1] + 1
            else:
                matrix[2][2] = matrix[2][2] + 1
        elif subject.type == "Iris-setosa":
            if type == "Iris-versicolor":
                matrix[0][1] = matrix[0][1] + 1
            else:
                matrix[0][2] = matrix[0][2] + 1
        elif subject.type == "Iris-versicolor":
            if type == "Iris-setosa":
                matrix[1][0] = matrix[1][0] + 1
            else:
                matrix[1][2] = matrix[1][2] + 1
        else:
            if type == "Iris-setosa":
                matrix[2][0] = matrix[2][0] + 1
            else:
                matrix[2][1] = matrix[2][1] + 1

    print("Matriz de Confusão")
    print("   A,  B, C")
    print("A {}".format(matrix[0]))
    print("B {}".format(matrix[1]))
    print("C {}".format(matrix[2]))

    #True Positive Rate
    #False Negative Rate
    TPRA = matrix[0][0]/(matrix[0][0] + matrix[0][1] + matrix[0][2]) *100
    TPRB = matrix[1][1] / (matrix[1][0] + matrix[1][1] + matrix[1][2]) * 100
    TPRC = matrix[2][2] / (matrix[2][0] + matrix[2][1] + matrix[2][2]) * 100
    FNRA = matrix[0][0] / (matrix[0][0] + matrix[1][0] + matrix[2][0]) * 100
    FNRB = matrix[1][1] / (matrix[0][1] + matrix[1][1] + matrix[2][1]) * 100
    FNRC = matrix[0][0] / (matrix[0][2] + matrix[2][1] + matrix[2][2]) * 100
    print("--")
    print("Precision(A): {0:.2f}%".format(TPRA))
    print("Precision(B): {0:.2f}%".format(TPRB))
    print("Precision(C): {0:.2f}%".format(TPRC))
    print("--")
    print("Recall(A): {0:.2f}%".format(FNRA))
    print("Recall(B): {0:.2f}%".format(FNRB))
    print("Recall(C): {0:.2f}%".format(FNRC))
    print("--")
    print('Acertos {} em {} testes.'.format(vp, tests))
    accuracy = (vp/float(tests)) * 100
    errors = (tests - vp)/float(tests) * 100
    print('Accuracy: {0:.2f}%'.format(accuracy))
    print('Taxa de erro: {0:.2f}%'.format(errors))

if __name__ == '__main__':
    main()