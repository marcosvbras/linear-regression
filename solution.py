# -*- coding: utf-8 -*-

import csv
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt

def calculate_b0_b1(training):
    sum_x = 0
    sum_y = 0
    sum_pow_x = 0
    sum_x_y = 0
    result = []
    size = len(training)

    for coordinate in training:
        x, y = coordinate
        sum_x += x
        sum_y += y
        sum_pow_x += (x**2)
        sum_x_y += (x * y)

    b1 = ((sum_x * sum_y) - (size * sum_x_y)) / ((sum_x**2) - (size * sum_pow_x))
    b0 = (sum_y - (b1 * sum_x)) / size

    return (b0, b1)

def calculate_linear_regression(b0, b1, x):
    return b0 + (b1 * x)

def calculate_standard_deviation(test, b0, b1):
    deviation = 0

    for coordinate in test:
        x, yi = coordinate
        deviation += (yi - calculate_linear_regression(b0, b1, x)) ** 2

    return deviation

def readData(file):
    data_set = []

    with open(file) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=';')

        index = 0

        for row in readCSV:
            if index == 0:
                index = 1
                continue

            average = (float(row[3]) + float(row[4]) + float(row[5])) / 3
            row.append(average)
            data_set.append(row)

    return data_set

def show_chart(dataset, b0, b1, type_label):
    xs = [entry[0] for entry in dataset]
    ys_r = [calculate_linear_regression(b0, b1, x) for x in xs]
    plt.title('Média das Provas x ' + type_label)
    plt.xlabel(type_label.title())
    plt.ylabel('Média das provas')
    plt.plot(xs, ys_r)
    plt.show()

data = readData('AnaliseEstudo.csv')

training_length = round(len(data) * 0.7)

training = data[:training_length]
test = data[training_length:]

### Idade;TempoEstudo;Faltas;Prova1;Prova2;Prova3

AGE = 0
STUDY_TIME = 1
ABSENCE = 2

# Média das Provas x Idade
training_age = [(float(t[AGE]), float(t[6])) for t in training]
test_age = [(float(t[AGE]), float(t[6])) for t in test]

b0, b1 = calculate_b0_b1(training_age)
print(calculate_standard_deviation(test_age, b0, b1))
show_chart(training_age + test_age, b0, b1, "Idade")

# Média das Provas x Tempo de Estudo
training_study_time = [(float(t[STUDY_TIME]), float(t[6])) for t in training]
test_study_time = [(float(t[STUDY_TIME]), float(t[6])) for t in test]

b0, b1 = calculate_b0_b1(training_study_time)
print(calculate_standard_deviation(test_study_time, b0, b1))
show_chart(training_study_time + test_study_time, b0, b1, "Tempo de Estudo")

# Média das Provas x Faltas
training_absences = [(float(t[ABSENCE]), float(t[6])) for t in training]
test_absences = [(float(t[ABSENCE]), float(t[6])) for t in test]

b0, b1 = calculate_b0_b1(training_absences)
print(calculate_standard_deviation(test_absences, b0, b1))
show_chart(training_absences + test_absences, b0, b1, "Faltas")