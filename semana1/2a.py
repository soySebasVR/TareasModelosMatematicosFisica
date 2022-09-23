import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

def main():
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    n = 256
    x = np.linspace(-1., 1., n)
    y = np.linspace(-1., 1., n)
    X, Y = np.meshgrid(x, y)

    Z = 1 / (np.sqrt(X**2 + Y**2))

    surf = ax.plot_surface(
        X, Y, Z,
        cmap=cm.coolwarm,
        linewidth=0,
        antialiased=False
    )
    plt.show()

if __name__ == '__main__':
    main()
