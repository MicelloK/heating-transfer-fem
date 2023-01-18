import matplotlib.pyplot as plt

def show(x, y):
    plt.style.use('seaborn-darkgrid')
    ax = plt.subplot()
    ax.set(title='heating transfer FEM', xlabel='x')
    ax.plot(x, y, color='red')

    plt.show()
