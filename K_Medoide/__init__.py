#K-Midoide algorithm
import numpy as np
import random


def load_matrix_C():
    C = np.loadtxt(r'./matrix_C.txt', delimiter = ',')
    return C

def get_start_list(n, k):
    list = random.sample(range(0,n), k)
    return list

def get_euc_dist(c1,c2):
    return np.sqrt(np.sum(np.square(c1-c2)))

def k_mediode(C, k):
    m, r = np.shape(C)
    random_core_list = get_start_list(m, k)    
    last_list = [i for i in random_core_list]
    core_list, set_list = get_new_core_list(C, last_list, k)
    i = 1
    while(not set_cmp(core_list, last_list)):
        last_list = [i for i in core_list]
        core_list, set_list = get_new_core_list(C, last_list, k)
        print('this is the',i,'loop')
        i += 1
    return core_list, set_list

def set_cmp(list1,list2):
    set1 = set(list1)
    set2 = set(list2)
    return len(set1.difference(set2)) == 0

def get_new_core_list(C, core_list, k):
    set_list = [[]for raw in range(k)]
    m, r = np.shape(C)
    core_set = set(core_list)
    for i in range(k):
        set_list[i].append(core_list[i])

    for i in range(m):
        min_dis = -1
        class_id = -1
        for j in range(k):
            if i in core_set:
                continue
            else:
                #calculate the distance of pointi and point start_list[j]
                coo1 = C[i]
                coo2 = C[core_list[j]]

                cur_dis = get_euc_dist(coo1, coo2)

                if min_dis == -1 or cur_dis < min_dis:
                    min_dis = cur_dis
                    class_id = j
        if not i in core_set:
            set_list[class_id].append(i)

        if i % 5000 == 0:
            print(i,'has been finished')
    #finish one classification

    new_core_list = []
    
    for i in range(k):
        cur_list = set_list[i]
        length = len(cur_list)
        min_dis = -1
        index = -1
        for j in range(length):
            cur_dis = 0
            coo1 = C[cur_list[j]]
            for p in range(length):
                if j == p:
                    continue
                else:                   
                    coo2 = C[cur_list[p]]
                    cur_dis += get_euc_dist(coo1, coo2)
            if min_dis == -1 or cur_dis < min_dis:
                min_dis = cur_dis
                index = j
        print('new core',i,'has been choosed')

        new_core_list.append(cur_list[index])

    return new_core_list, set_list

if __name__ == '__main__':
    k = 250
    C = load_matrix_C()

    core_list, set_list = k_mediode(C, k)

    print('core_list:')
    print(core_list)

    print('set_list')
    print(set_list)
    #graph
