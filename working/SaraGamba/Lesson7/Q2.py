"""
Q2: Consistent plotting
author: Sara Gamba
"""
import matplotlib.pyplot as plt
import argparse

def sarasplot(function):
    def wrapper(*args, **kwargs):
        """
        wrapper
        param: *args, **kwargs
        return: set default plot style
        """
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
        figure.savefig(f"./working/SaraGamba/Lesson7/{function.__name__}.pdf", format="pdf")
        print(f"Plot saved as ./working/SaraGamba/Lesson7/{function.__name__}.pdf")
        
        return figure
    return wrapper


@sarasplot
def example_plot():
    """
    example_plot
    param:
    return: figure of example
    """
    figure, ax = plt.subplots()
    ax.plot([0, 1, 2], [0, 1, 4], label="Example")
    ax.set_title("Example Plot")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend()
    return figure

# call decorated function
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Consistent plotting. Just run the code!')
    args = parser.parse_args()
    
    example_plot()