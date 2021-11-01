import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col="date", parse_dates=True)

# Clean data
df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fig = plt.figure()
    plt.plot(df.index, df.value)
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.title('Daily freeCodeCamp Forum Page Views '+ df.index[0].strftime('%-m/%Y')
                + '-'
                + df.index[-1].strftime('%-m/%Y'))

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['year'] = df.index.year
    df_bar['month_name'] = df.index.strftime('%B')

    df_bar = df_bar.groupby(['year', 'month_name']).agg('mean').reset_index()

    months = pd.date_range('2020-01', '2020-12', freq='MS').strftime('%B').tolist()

    # Draw bar plot
    fig = plt.figure()

    sns.barplot(data=df_bar, x="year",y="value",palette="tab20c",hue="month_name",hue_order=months,ec="grey")

    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title='Months', loc='upper left')

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    months = pd.date_range('2020-01', '2020-12', freq='MS').strftime('%b').tolist()
    # Draw box plots (using Seaborn)

    fig, axes = plt.subplots(1,2)

    ax = axes[0]
    sns.boxplot( data=df_box,x="year", y="value",ax=ax)
    ax.set_title('Year-wise Box Plot (Trend)')
    ax.set_xlabel('Year')
    ax.set_ylabel('Page Views')

    ax = axes[1]
    sns.boxplot(data=df_box,x="month", y="value",order=months,ax=ax)
    ax.set_title('Month-wise Box Plot (Seasonality)')
    ax.set_xlabel('Month')
    ax.set_ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
