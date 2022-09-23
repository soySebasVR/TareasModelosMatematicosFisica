import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np

def main():
    x = np.linspace(0, 2 * np.pi, 100)
    fx = np.sin(x)
    gx = x**2 + 3*x

    fig, ax = plt.subplots()
    ax.plot(x, fx, label='f(x) = sin(x)')
    ax.plot(x, gx, label='g(x) = x^2 + 3x')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title("Pregunta 1a")
    ax.legend()
    plt.show()

if __name__ == '__main__':
    main()
