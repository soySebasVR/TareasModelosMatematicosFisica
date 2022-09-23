import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np

def main():
    x = np.linspace(-10, 10, 200)
    y = x**2 + 5*x - 3

    fig, ax = plt.subplots()
    ax.plot(x, y, 'r--', label='x^2 + 5x - 3')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title("Pregunta 1b")
    ax.grid(True)
    ax.legend()
    plt.show()

if __name__ == '__main__':
    main()
