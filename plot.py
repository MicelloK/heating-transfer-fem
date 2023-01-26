import matplotlib.pyplot as plt

def show(x, y, n):
    plt.style.use('seaborn-darkgrid')
    ax = plt.subplot()
    ax.set(title='heating transfer FEM', xlabel='n = ' + str(n))
    ax.plot(x, y, color='red')

    plt.show()
