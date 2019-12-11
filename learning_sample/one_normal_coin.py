import numpy as np
import matplotlib.pyplot as plt


class OneCoin():

    def __init__(self,p=0.5):
        self._p = p


    def filp(self):
        rand_value =  np.random.rand()
        return rand_value > self._p


if __name__ == "__main__":
    try_count = 1000
    coin =OneCoin()

    positive_rate = []
    positive_count =0

    for i in range(try_count):
        if coin.filp():
            positive_count +=1
        positive_rate.append(positive_count/(i+1))

    print(positive_count / try_count)

    plt.plot(range(try_count), positive_rate, ls="-", lw=2, label="positive_rate")

    plt.legend()
    plt.axhline(y=0.5, ls=":", c="red")  # 添加水平直线
    plt.savefig('./figs/tmp/one_normal_coin.jpg')
    plt.show()


