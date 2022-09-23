import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np

def main():
    n = 10
    x, y = np.meshgrid(np.linspace(-5,5,10),np.linspace(-5,5,10))
    u = (np.sqrt(x**2+y**2)*x)/(x**2+y**2)
    v = (np.sqrt(x**2+y**2)*y)/(x**2+y**2)

    fig, ax = plt.subplots()
    ax.quiver(x,y,u,v)
    ax.set_title("Pregunta 3j")
    plt.show()

if __name__ == '__main__':
    main()
