import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.use('TkAgg')


def main():
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    n = 256
    x = np.linspace(-10., 10., n)
    y = np.linspace(-10., 10., n)
    X, Y = np.meshgrid(x, y)

    Z = X - Y + 2

    surf = ax.plot_surface(
        X, Y, Z,
        cmap=cm.coolwarm,
        linewidth=0,
        antialiased=False
    )
    plt.show()


if __name__ == '__main__':
    main()
