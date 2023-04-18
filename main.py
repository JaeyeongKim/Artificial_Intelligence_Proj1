import csv
import sys
import re
from collections import defaultdict
#for learning curve
from matplotlib import pyplot as plt

sys.stdin = open("stop_word.txt", "r")


def NBC(t_percent):
    global max_train_line
    word_num_dict = defaultdict(int)
    rating_five_word_num_dict = defaultdict(int)
    rating_one_word_num_dict = defaultdict(int)
    num_of_five = 0
    num_of_one = 0
    train_line = ((max_train_line*t_percent)//100)+1

    with open('train.csv', newline='') as f:
        reader = csv.reader(f)
        line_num = 0

        for row in reader:
            if line_num == 0:
                line_num += 1
                continue
            if line_num == train_line:
                break
            #Convert all text to lowercase
            line = row[1].lower()
            #Remove special characters
            re_special_line = re.sub("[\u0021-\u002F\u003A-\u0040\u005B-\u0060\u007B-\u007E]", "", str(line))
            #Tokenize the text into words
            tokenized_line = list(map(str,re_special_line.split()))

            #Remove stop words
            re_stop_words_line = [w for w in tokenized_line if w not in stop_words]
            #Count num of word
            for w in re_stop_words_line:
                word_num_dict[w] +=1

            re_stop_words_line = list(set(re_stop_words_line))
            for w in re_stop_words_line:
                if row[0] == '5':
                    rating_five_word_num_dict[w] +=1
                else:
                    rating_one_word_num_dict[w] +=1

            #Counting Stars '5'
            if row[0] == '5':
                num_of_five +=1
            elif row[0] == '1':
                num_of_one +=1
            line_num += 1

    feature_list = sorted(word_num_dict.items(), key=lambda x: -x[1])
    feature_list = feature_list[0:1000]
    print("NBC with %d percent training set" %(t_percent))
    for i in range(19,50):
        print(feature_list[i][0])
    print()

    #Laplace Smoothing
    for i in range(len(feature_list)-1):
        feature_list[i] = list(feature_list[i])
        feature_list[i].append((rating_five_word_num_dict[feature_list[i][0]] + 1)/(num_of_five+2))
        feature_list[i].append((num_of_five+2 - rating_five_word_num_dict[feature_list[i][0]] - 1)/(num_of_five+2))
        feature_list[i].append((rating_one_word_num_dict[feature_list[i][0]] + 1) / (num_of_one + 2))
        feature_list[i].append((num_of_one + 2 - rating_one_word_num_dict[feature_list[i][0]] - 1) / (num_of_one + 2))

    probability_five = num_of_five / (line_num-1)
    probability_one = num_of_one /(line_num-1)


    true_positive = 0
    true_negative = 0
    false_positive = 0
    false_negative = 0
    with open('test.csv', newline='') as t:
        reader = csv.reader(t)
        test_line_num = 0

        for row in reader:
            if test_line_num == 0:
                test_line_num += 1
                continue
            #probability
            p5 = probability_five
            p1 = probability_one

            # Convert all text to lowercase
            line = row[1].lower()
            # Remove special characters
            re_special_line = re.sub("[\u0021-\u002F\u003A-\u0040\u005B-\u0060\u007B-\u007E]", "", str(line))
            # Tokenize the text into words
            tokenized_line = list(map(str, re_special_line.split()))
            # Remove stop words
            re_stop_words_line = [w for w in tokenized_line if w not in stop_words]

            for i in range(len(feature_list) - 1):
                if feature_list[i][0] in re_stop_words_line:
                    p5 *= feature_list[i][2]
                    p1 *= feature_list[i][4]
                else:
                    p5 *= feature_list[i][3]
                    p1 *= feature_list[i][5]

            if p5 >= p1:
                if row[0] == '5':
                    true_positive +=1
                else:
                    false_positive +=1
            elif p5 < p1:
                if row[0] == '5':
                    false_negative += 1
                else:
                    true_negative +=1

    print(true_positive)
    print(true_negative)
    print(false_positive)
    print(false_negative)
    accuracy = (true_negative+true_positive) / (true_negative+true_positive+false_negative+false_positive)
    return accuracy


def Draw_Learning_Curve(x_axis, y_axis):
    title = "Learning Curve"
    plt.figure()
    plt.title(title)
    plt.xlabel("Training Data(%)")
    plt.ylabel("Accuracy")
    plt.plot(x_axis, y_axis, 'bo--', label = "test set")
    plt.axis([0, 120, 0, 1])
    plt.legend()
    plt.show()



if __name__ == '__main__':
    max_train_line = 4000
    stop_words = list()
    for i in range(733):
        stop_words.append(input())

    result = list()
    percent_list = [10, 30, 50, 70, 100]

    for per in percent_list:
        result.append(NBC(per))
    Draw_Learning_Curve(percent_list, result)





