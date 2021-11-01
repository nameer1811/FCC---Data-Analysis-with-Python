import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    firstLine = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    xFirst = np.arange(df['Year'].min(),2051)
    yFirst = xFirst*firstLine.slope + firstLine.intercept

    plt.plot(xFirst,yFirst)

    # Create second line of best fit
    df_2000 = df[df['Year'] >= 2000]

    secondLine = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    xSecond = np.arange(2000,2051)
    ySecond = xSecond*secondLine.slope + secondLine.intercept

    plt.plot(xSecond,ySecond)

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
