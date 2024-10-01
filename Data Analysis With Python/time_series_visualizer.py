import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", index_col="date")

# Clean data
# Clean data by removing anything smaller than 2.5% quantile or greater than 97.5% quantile
df = df[(df["value"] > df["value"].quantile(0.025)) & (df["value"] < df["value"].quantile(0.975))]
df.index = pd.to_datetime(df.index) #  Change index to datetime format


def draw_line_plot():
    # Draw line plot
    fig, ax= plt.subplots(figsize=(15,5))
    fig.suptitle("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")
    ax.locator_params(axis="x", nbins=5, tight=True)
    ax.plot(df,"r")

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.resample("M").mean()
    df_bar["Months"] = df_bar.index.strftime("%B")
    df_bar["year"] = df_bar.index.year.astype(int)
    df_bar = df_bar.rename(columns={"value":"Average Page Views"})
    df_bar.index = df_bar.index.strftime("%Y-%m")

    # Insert missing data in 2016, the first four months
    missing_data = {
        "year": [2016, 2016, 2016, 2016],
        "Months": ['January', 'February', 'March', 'April'],
        "Average Page Views": [0, 0, 0, 0]
    }

    df_bar = pd.concat([pd.DataFrame(missing_data), df_bar])

    # Draw bar plot
    fig, ax = plt.subplots(figsize=(7,7))
    ax = sns.barplot(data=df_bar, 
                     x="year", 
                     y="Average Page Views", 
                     hue="Months", 
                     palette="tab10")
    plt.tight_layout()


    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

        # Draw box plots (using Seaborn)
    fig,ax = plt.subplots(1,2,figsize=(15,5))

    # First plot
    ax[0].title.set_text("Year-wise Box Plot (Trend)")
    ax[0].set_xlabel("Year")
    ax[0].set_ylabel("Page Views")
    sns.boxplot(df_box, 
                x="year", 
                y="value", 
                ax=ax[0], 
                hue="year", 
                palette="bright", 
                legend=False, 
                fliersize=1)

    # Second plot
    ax[1].title.set_text("Month-wise Box Plot (Seasonality)")
    ax[1].set_xlabel("Month")
    ax[1].set_ylabel("Page Views")
    sns.boxplot(df_box, x="month", 
                y="value", 
                ax=ax[1], 
                hue="month", 
                order=["Jan", "Feb", "Mar", "Apr", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], 
                palette="Set2", 
                fliersize=1)

    for ax in ax:
        ax.set_ylim([0,200000])
        ax.locator_params(axis="y", nbins=10, tight=True)

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
