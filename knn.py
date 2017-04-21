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

class tuple():
    def __init__(self, dist, index):
        self.dist = dist
        self.index = index

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

    dist_subjects = set()

    index = 0

    dist_tuple = []

    for i in subjects:
        dist = euclidian(i, subject)
        dist_tuple.append((dist, index))
        sorted(dist_tuple, key=lambda dist: dist[1])
        dist_subjects.add(tuple(dist, index))
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
    k = 3
    accuracy = 0
    trainning = 50
    tests = 150 - trainning

    with open('iris.csv', 'r') as csvfile:
        lines = csv.reader(csvfile)
        for row in lines:
            subjects.append(flower(float(row[0]), float(row[1]), float(row[2]), float(row[3]), row[4]))

    shuffle(subjects)

    for i in range(0,trainning):
        trainning_subjects.append(subjects[i])

    for j in range(0, tests):
        subject = subjects[j]

        type = classify(trainning_subjects, subject, k)

        if subject.type == type:
            accuracy = accuracy + 1

        print('Classe esperada: ' + subjects[j].type)
        print('Classe obtida: ' + type)

    print('Acertos {} em {} testes.'.format(accuracy, trainning))
    accuracy = accuracy/float(trainning) * 100
    print('Accuracy: {0:.2f}%'.format(accuracy))

if __name__ == '__main__':
    main()