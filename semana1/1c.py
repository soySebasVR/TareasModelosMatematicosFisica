import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np

def main():
    x = np.linspace(0, 6, 100)
    fx = 3*x*np.exp(x)
    gx = np.sin(x + 3)

    fig, ax = plt.subplots()
    ax.plot(x, fx, 'b', label='f(x) = 3x*e^x')
    ax.plot(x, gx, 'r--', label='g(x) = sin(x + 3)')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title("Pregunta 1c")
    ax.legend()
    plt.show()

if __name__ == '__main__':
    main()
