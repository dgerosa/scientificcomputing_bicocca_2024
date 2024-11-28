"""
Q2: Consistent plotting
author: Sara Gamba
"""
import matplotlib.pyplot as plt

def sarasplot(function):
    def wrapper(*args, **kwargs):
        # set default plot style
        plt.rcParams.update({
            'font.size': 10,          # font size
            'axes.titlesize': 14,     # title size
            'lines.markersize': 8,     # marker size
            'axes.labelsize': 12,     # axis labels size
            'xtick.labelsize': 10,    # x-axis label size
            'ytick.labelsize': 10,    # y-axis label size
            'figure.figsize': (10, 8), # figure size
            'lines.linewidth': 1,     # sine
            'axes.grid': False,        # show grid
            'lines.marker': 'o',      # marker shape
        })
        
        # call the plot function
        figure = function(*args, **kwargs)
        
        # save
        figure.savefig(f"{function.__name__}.pdf", format="pdf")
        print(f"Plot saved as {function.__name__}.pdf")
        
        return figure
    return wrapper

# example
@sarasplot
def example_plot():
    figure, ax = plt.subplots()
    ax.plot([0, 1, 2], [0, 1, 4], label="Example")
    ax.set_title("Example Plot")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend()
    return figure

# call decorated function
if __name__ == "__main__":
    example_plot()