import numpy.matlib
import numpy as np
import hydshow as hs

def open_file(path):
    return open(path, 'r')

def close_file(f):
    f.close()

def find_c_p(V, r, loopcount, e):
    m, n = np.shape(V)

    C = np.matlib.rand(m,r)
    P = np.matlib.rand(r,n)

    i = 0
    while(i < loopcount): 
        C, P = iterate(V, C, P)
        i += 1
        print('loop in :', i)
    return C, P

def check(V, C, P, e):
    #using the idea from the website https://www.cnblogs.com/gavanwanggw/p/7337227.html
    m, n = np.shape(V)
    V_tmp = C * P
    E = V - V_tmp

    err = 0
    for i in range(m):
        for j in range(n):
            err += E[i,j] * E[i,j]
    if err < e:
        return True
    else:
        return False

def iterate(V, C, P):

    # we need : V ?= C*P == V_tmp

    m, n = np.shape(V)
    m, r = np.shape(C)

    #update P
    tmp_mat1 = C.T * V
    tmp_mat2 = C.T * C * P
    for i in range(r):
        for j in range(n):
            if tmp_mat2[i,j] != 0:
                P[i,j] = P[i,j] / tmp_mat2[i,j] * tmp_mat1[i,j] 

    #update C
    tmp_mat3 = V * P.T
    tmp_mat4 = C * P * P.T
    for i in range(m):
        for j in range(r):
            if tmp_mat4[i,j] != 0:
                C[i,j] = C[i,j] / tmp_mat4[i,j] * tmp_mat3[i,j]


    return C, P


if __name__ == '__main__':

    file = open_file('./data/20111116.csv')    
    lines = file.readlines()

    m = len(lines)
    n = len(lines[0].split(',')) - 3
    r = 3
    loopcount = 1000 # max count of loop
    e = 1e-5

    V = np.matlib.empty((m,n))


    for i in range(m):
        #read data of every road(m roads)
        road_i_data = lines[i].split(',')
        road_i_data = np.array(road_i_data[3:])
        V[i,:] = road_i_data

    close_file(file)

    C,P = find_c_p(V, r, loopcount, e)

    np.savetxt(r'./matrix_C.txt', C, delimiter = ',')
    np.savetxt(r'./matrix_P.txt', P, delimiter = ',')

    hs.show(P)

