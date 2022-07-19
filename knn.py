from calendar import c
from http import client
import math

#calculate euclidean distance
def Euclidean_distance(train_data,test_data):
    n = 0
    ans = 0
    test_len = len(test_data)
    while n < test_len:
        if n == test_len - 1:
            break
        a = float(test_data[n])
        b = float(train_data[n])
        temp = pow(a-b,2)
        ans = ans + temp
        n+=1
    return math.sqrt(ans)

def classify_nn(training_filename, testing_filename, k):
    # train = np.genfromtxt(training_filename, delimiter=',', names=None, autostrip=True)
    # test = np.genfromtxt(testing_filename, delimiter=',', names=None, autostrip=True)
    train = [] #ls of train
    test = [] #ls of test

    #result_train = [[0.084,0.192,0.569,0.274,0.105,0.179,0.090,0.284,yes]]
    #type(elements in result): str
    f_train = open(training_filename,'r')
    for l in f_train:
        line = l.strip("\n").split(",")
        train.append(line)

    #result_test = [[0.588,0.628,0.574,0.263,0.136,0.463,0.054,0.333]]
    #type(elements in result): str
    f_test = open(testing_filename,'r')
    for l in f_test:
        line = l.strip("\n").split(",")
        test.append(line)


    ans = []
    i = 0
    while i < len(test):
        k_class = []
        k_dist = []
        n = 0
        while n < k: #（把前k个distance和class放到分别的ls里面去）

            temp_d = Euclidean_distance(train[n],test[i]) #取一个testdata 前k个training data
            k_dist.append(temp_d)
            last = len(train[n])-1
            temp_class = train[n][last] #yes/no

            k_class.append(temp_class)
            n+=1
        j = 0
        while j < len(train):
            d = Euclidean_distance(train[j],test[i]) #取一个testdata 所有training data
            max_d = max(k_dist)#有最大的替换最大的

            if d <= max_d:
                max_position = k_dist.index(max_d)
                k_dist[max_position] = d
                last_class = len(train[j]) - 1
                max_class = train[j][last_class] #替换最大的label

                k_class[max_position] = max_class
            j+=1
        count_n = 0
        count_y = 0
        g = 0
        while g < len(k_class):
            if k_class[g] == "no":
                count_n+=1
            elif k_class[g] == "yes":
                count_y+=1
            g+=1
        if count_n > count_y:
            ans.append("no")
        else:
            ans.append("yes")
        

        i+=1
        
    f_train.close()
    f_test.close()
    return ans


def accuracy(training_filename, testing_filename, k):
    predict = classify_nn(training_filename,testing_filename,k)
    actual = [] 
    f_test = open(testing_filename,'r')
    for l in f_test:
        line = l.strip("\n").split(",")
        actual.append(line[len(line) - 1])
    check = 0
    for i in range(len(actual)):
        if i >= len(predict):
            break
        if actual[i] == predict[i]:
            check+=1
    acc = check/len(actual)
    return acc

def main():
    # a = accuracy("knn1_1train.csv", "knn1_1test.csv",5)
    # a2 = accuracy("knn1_2train.csv", "knn1_2test.csv",5)
    # a3 = accuracy("knn1_3train.csv", "knn1_3test.csv",5)
    # a4 = accuracy("knn1_4train.csv", "knn1_4test.csv",5)
    # a5 = accuracy("knn1_5train.csv", "knn1_5test.csv",5)
    # a6 = accuracy("knn1_6train.csv", "knn1_6test.csv",5)
    # a7 = accuracy("knn1_7train.csv", "knn1_7test.csv",5)
    # a8 = accuracy("knn1_8train.csv", "knn1_8test.csv",5)
    # a9 = accuracy("knn1_9train.csv", "knn1_9test.csv",5)
    # a10 = accuracy("knn1_10train.csv", "knn1_10test.csv",5)
    a = accuracy("cfstrain1.csv", "cfstest1.csv",1)
    a2 = accuracy("cfstrain2.csv", "cfstest2.csv",1)
    a3 = accuracy("cfstrain3.csv", "cfstest3.csv",1)
    a4 = accuracy("cfstrain4.csv", "cfstest4.csv",1)
    a5 = accuracy("cfstrain5.csv", "cfstest5.csv",1)
    a6 = accuracy("cfstrain6.csv", "cfstest6.csv",1)
    a7 = accuracy("cfstrain7.csv", "cfstest7.csv",1)
    a8 = accuracy("cfstrain8.csv", "cfstest8.csv",1)
    a9 = accuracy("cfstrain9.csv", "cfstest9.csv",1)
    a10 = accuracy("cfstrain10.csv", "cfstest10.csv",1)
    avg = (a + a2 + a3+a4+a5+a6+a7+a8+a9+a10)/10

    print(avg)

main()
#no feature selection
#k=1, 0.679630895420369
#k=5, 0.7473855092276145

#feature selection
#k=1,0.68996003996004
#k=5,0.7506327006327007



