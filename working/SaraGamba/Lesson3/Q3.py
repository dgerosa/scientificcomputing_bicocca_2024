"""
Q3: A perfect circle
author: Sara Gamba
"""
import numpy as np 
import matplotlib.pyplot as plt
import argparse


def draw_circles(R,x0,y0,color):
    """
    draw_circles
    param: Radius, circle center points, fill color 
    return: pdf of the circle created
    """
    angle=np.linspace(0, 2*np.pi, num=1000)
    x=R*np.cos(angle)+x0
    y=R*np.sin(angle)+y0

    fig = plt.figure()
    ax = plt.axes()
    ax.plot(x,y,color=color)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.fill(x, y, color=color)
    plt.savefig("./working/SaraGamba/Lesson3/cicle.pdf")
    print("./working/SaraGamba/Lesson3/circle.pdf correctly saved.")

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Circle program')
    parser.add_argument('--Radius', type=float, help='Radius')
    parser.add_argument('--y0', type=float, help='y0')
    parser.add_argument('--x0', type=float, help='x0')
    parser.add_argument('--color', type=str, help='fill color')

    args = parser.parse_args()

    if(args.Radius is None or args.x0 is None or args.y0 is None or args.color is None):
        print('Cannot start the program: missing the arguments!')
    else:
        draw_circles(args.Radius,args.x0,args.y0,args.color)
