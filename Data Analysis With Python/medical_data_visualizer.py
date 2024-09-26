import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv("medical_examination.csv")

# 2
df['overweight'] = ((df["weight"] / ((df["height"]/100) **2))>25).astype(int) # New column BMI uses np.select to set rows where BMI (weight/height^2) > 25 to 1, and all other cases to 0.

# 3
df["cholesterol"] = np.select([df["cholesterol"]==1, df["cholesterol"]>1], [0,1]) # Set cholesterol to 0 when it is 1, and 1 when it is above 1
df["gluc"] = np.select([df["gluc"]==1, df["gluc"]>1], [0,1]) # Again for glucose

# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df, id_vars="cardio", value_vars=["cholesterol","gluc","smoke","alco","active","overweight"]) # Convert dataset to long format
 
    # 6
    df_cat = df_cat.groupby(["cardio", "variable", "value"]).size().reset_index() # Group variables such that all with cardio=0 first, then by variable, then by value. Then take the number of entries where each variable had cardio=0,variable="variable",value=value. Then reset_index to add a new index.
    df_cat = df_cat.rename(columns={0 : "total"})

    # 7
    graph = sns.catplot(df_cat, x="variable", y="total", col="cardio", kind="bar", hue="value")


    # 8
    fig = graph.fig


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df[(df["ap_lo"] <= df["ap_hi"]) & 
                (df["height"]>=df["height"].quantile(0.025)) & 
                (df["height"]<=df["height"].quantile(0.975)) & 
                (df["weight"]>=df["weight"].quantile(0.025)) &
                (df["weight"]<=df["weight"].quantile(0.975))]

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 14
    fig, ax = plt.subplots()

    # 15
    sns.heatmap(corr, mask=mask, annot=True, fmt="0.1f")


    # 16
    fig.savefig('heatmap.png')
    return fig
