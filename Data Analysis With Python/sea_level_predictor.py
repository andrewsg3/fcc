import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    # Create scatter plot
    fig, ax = plt.subplots()
    ax.scatter(x=df["Year"], y=df["CSIRO Adjusted Sea Level"])

    # Create first line of best fit
    r = linregress(x=df["Year"], y=df["CSIRO Adjusted Sea Level"])
    df["regress"] = (df["Year"] * r.slope) + r.intercept 
    df=pd.concat([pd.DataFrame({"Year": [2050], "regress": [(2050*r.slope)+r.intercept]}), df]).sort_values("Year", ascending=True).reset_index().drop("index",axis=1) # Add 2050
    ax.set_xlim([1850,2075])
    ax.plot(df["Year"],df["regress"],'r')


    # Create second line of best fit
    r2 = linregress(x=df[(df["Year"] > 2000) & (df["Year"] < 2050)]["Year"], y=df[(df["Year"] > 2000) & (df["Year"] < 2050)]["CSIRO Adjusted Sea Level"])
    df["regress2"]= (df[(df["Year"] > 2000)]["Year"] * r2.slope) + r2.intercept 
    ax.plot(df["Year"],df["regress2"],'g')

    # Add labels and title
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")
    #ax.locator_params(nbins=7)
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()