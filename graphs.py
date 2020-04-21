#! python3
import numpy as np
import pandas as pd


def shaded_alpha_area(p,n, alpha):
    binomial_mean = p * n
    binomial_var = n * p * (1-p)
    normal_approx = stats.norm(binomial_mean, np.sqrt(binomial_var))

    x = np.linspace(0,n,1000)

    fig, ax = plt.subplots(1, figsize=(16, 3))

    ax.plot(x, normal_approx.pdf(x), linewidth=3)
    ax.fill_between(x, normal_approx.pdf(x), 
                where=(x >= normal_approx.ppf(1-alpha)), color="red", alpha=0.5)
    ax.set_title("Significance Region")

def twin_x():
     #Twin X /  Different Y
    fig, ax1 = plt.subplots(figsize=(8,5))

    color = 'blue'
    ax1.set_xlabel('')
    ax1.set_ylabel(')  # we already handled the x-label with ax1
    ax1.plot(x, y, color=color)
    ax1.tick_params(axis='', labelcolor=color)
    ax1.axhline(OD_mean)

    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis


    color = 'red'

    ax2.set_ylabel('')
    ax2.plot(x, y2, color=color)
    ax2.tick_params(axis='', labelcolor=color)
    
def graph():
    return 



def scatterplot(x,y):
    return plt.scatter(x,y)

def scatter():
    return 'This is a scatter plot'

def eddieplot(df):
    df.plotting.scattermatrix()
    return

def beta_distr():
    fig, ax = plt.subplots(figsize=(10,5))
    x = np.linspace(0,1,100)
    for (a,b,s) in [(1,1,"r-"), (2,1,"g-"), (3,1,"b-"), (2,2,"g--"), (3,2,"b--"), (3,3,"b:")]:
            ax.plot(x,
                    stats.beta(a,b).pdf(x),
                    s,
                    label="({0},{1})".format(a,b))
    ax.legend(title=r"($\alpha,\beta$)", loc="upper left")
    ax.set_xlabel("p")
    ax.set_ylabel("pdf")


import matplotlib.pyplot as plt
x=list(range(10))
fig, ax = plt.subplots()
ax.plot(x,x)


def bootstrap_sample_medians(data, n_bootstrap_samples=10000):
    bootstrap_sample_medians = []
    for i in range(n_bootstrap_samples):
        bootstrap_sample = np.random.choice(data, size=len(data), replace=True)
        bootstrap_sample_medians.append(np.median(bootstrap_sample))
    return bootstrap_sample_medians

def choropleth():
    # import plotly as py
    # import plotly.express as px
    # import json
    # from urllib.request import urlopen

    # see https://github.com/tylerjwoods/covid-19/blob/master/choropleth_states.ipynb
    # for implementation

    with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

    fig = px.choropleth(df, geojson=counties, locations='fips', color='3 day',
                           color_continuous_scale=px.colors.sequential.Inferno,
                           range_color=(0, 40),
                           scope="usa",
                           labels={'3 day':'3-Day Percent Change'},
                           title='3-Day Percent Change in Counties',
                           hover_data=[df['county'], df['Prev 3 day']]
                          )

    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    #fig.write_html('county.html')
    fig.show()
    return 0

def residual_plot(ax, x, y, y_hat, n_bins=50):
    residuals = y - y_hat
    ax.axhline(0, color="black", linestyle="--")
    ax.scatter(x, residuals, color="grey", alpha=0.5)
    ax.set_ylabel("Residuals ($y - \hat y$)")
                   

#HI GUYS!!

