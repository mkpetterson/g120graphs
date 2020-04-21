#! python3

# Import Libraries
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import mplcyberpunk
import seaborn as sns


# Cyberpunk Histogram with KDE

"""
Base graph is Seaborn distplot object with Histogram and Kernel Density Estimate Distribution

REQUIRED MODULES (outside of normal DS imports):
- mplcyberpunk
- seaborn
"""

def distplot(ax:object, series:pd.Series, cybertheme:bool=True, dropna:bool=False) -> None:
    """ Plots 2D density plot visualization with histogram 
        
        Parameters
        ----------
        ax: Axes object
        
        series: array-like, pd.Series of a feature 
            data array
        cybertheme: bool, optional
            sets cell plt theme to "cyberpunk"
        dropna: bool, optional
            drops null values in series, will not be included in plot
    """
    # Set Cell Plot Style to cyberpunk
    if cybertheme:
        plt.style.use("cyberpunk")
    # Plot Series
    sns.distplot(
            series, 
            color="red",
            ax=ax,
            kde_kws={
                "color":'white',
                "shade":True,
                "alpha":0.7})



