import math
def PDF(index,train,test_num):
    sum = 0
    for i in range(len(train)):
        data = float(train[i][index])
        sum += data
    num = len(train)
    avg = sum/num
    sd = 0
    for j in range(len(train)):
        data = pow(float(train[j][index])-avg,2)
        sd += data
    num_sd = len(train) - 1
    sd = math.sqrt(sd/num_sd)
    final = (1/sd/math.sqrt(2*math.pi))* math.exp(-math.pow(test_num-avg,2)/(2*math.pow(sd,2)))
    return final

def classify_nb(training_filename, testing_filename):
    train = []
    test = []
    f_train = open(training_filename,'r')
    for l in f_train:
        line = l.strip("\n").split(",")
        train.append(line)
    f_test = open(testing_filename,'r')
    for l in f_test:
        line = l.strip("\n").split(",")
        test.append(line)
    train_y = []
    train_n = []
    count_y = 0
    count_n = 0
    i = 0
    while i < len(train):
        class_index = len(train[i]) - 1
        if train[i][class_index] == "no":
            train_n.append(train[i])
            count_n+=1
        elif train[i][class_index] == "yes":
            train_y.append(train[i])
            count_y+=1
        i+=1
    
    num_train = len(train)
    P_y = count_y/num_train
    P_n = count_n/num_train
    ans = []
    j = 0
    test_len = len(test)
    while j < test_len:
        P_En = 1
        P_Ey = 1
        one_test_len = len(test[j])
        for t in range(one_test_len):
            if t == one_test_len - 1:
                break
            test_num = float(test[j][t])
            y_PDF = PDF(t,train_y,test_num)
            n_PDF = PDF(t,train_n,test_num)
            P_En *= n_PDF
            P_Ey *= y_PDF
        P_y_E =  P_y * P_Ey
        P_n_E = P_n * P_En
        if P_y_E < P_n_E:
            ans.append("no")
        else:
            ans.append("yes")


        j+=1
    f_train.close()
    f_test.close()
    return ans


def accuracy(training_filename, testing_filename):
    predict = classify_nb(training_filename,testing_filename)
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
    # a = accuracy("knn1_1train.csv", "knn1_1test.csv")
    # a2 = accuracy("knn1_2train.csv", "knn1_2test.csv")
    # a3 = accuracy("knn1_3train.csv", "knn1_3test.csv")
    # a4 = accuracy("knn1_4train.csv", "knn1_4test.csv")
    # a5 = accuracy("knn1_5train.csv", "knn1_5test.csv")
    # a6 = accuracy("knn1_6train.csv", "knn1_6test.csv")
    # a7 = accuracy("knn1_7train.csv", "knn1_7test.csv")
    # a8 = accuracy("knn1_8train.csv", "knn1_8test.csv")
    # a9 = accuracy("knn1_9train.csv", "knn1_9test.csv")
    # a10 = accuracy("knn1_10train.csv", "knn1_10test.csv")
    a = accuracy("cfstrain1.csv", "cfstest1.csv")
    a2 = accuracy("cfstrain2.csv", "cfstest2.csv")
    a3 = accuracy("cfstrain3.csv", "cfstest3.csv")
    a4 = accuracy("cfstrain4.csv", "cfstest4.csv")
    a5 = accuracy("cfstrain5.csv", "cfstest5.csv")
    a6 = accuracy("cfstrain6.csv", "cfstest6.csv")
    a7 = accuracy("cfstrain7.csv", "cfstest7.csv")
    a8 = accuracy("cfstrain8.csv", "cfstest8.csv")
    a9 = accuracy("cfstrain9.csv", "cfstest9.csv")
    a10 = accuracy("cfstrain10.csv", "cfstest10.csv")
    avg = (a + a2 + a3+a4+a5+a6+a7+a8+a9+a10)/10

    print(avg)

main()

#no feature selection
#0.7498974709501026

#feature selection
#0.7544455544455543