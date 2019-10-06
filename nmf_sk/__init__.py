from sklearn.decomposition import NMF
import numpy as np
import matplotlib.pyplot as plt


def nmf_sklearn_to_file(n,file_addr,outW_addr,outH_addr):
    model = NMF(n_components=n)
    mat = np.loadtxt(file_addr,delimiter=",")
    W=model.fit_transform(mat)
    H=model.components_
    np.savetxt(outW_addr,W,delimiter=',')
    np.savetxt(outH_addr,H,delimiter=',')


def nmf_sklearn(n,mat):
    model = NMF(n_components=n)
    W=model.fit_transform(mat)
    H=model.components_
    return W,H


if __name__=='__main__':
    model = NMF(n_components=3)
    mat=np.loadtxt("/Users/liuyupeng/Desktop/data/traffic_csv/total.csv",delimiter=',')
    W=model.fit_transform(mat)
    H=model.components_
    np.savetxt("/Users/liuyupeng/Desktop/data/traffic_csv/totalW.csv",W,delimiter=',')
    np.savetxt("/Users/liuyupeng/Desktop/data/traffic_csv/totalH.csv", H, delimiter=',')

    x = []
    y1 = []
    y2 = []
    y3 = []

    for i in range(24):
        x.append(i)
        y1.append(H[0, i])
        y2.append(H[1, i])
        y3.append(H[2, i])

    plt.plot(x, y1)
    plt.plot(x, y2)
    plt.plot(x, y3)
    plt.plot()
    plt.show()