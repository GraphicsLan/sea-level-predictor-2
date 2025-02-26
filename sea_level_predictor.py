import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
   df= pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
   plt.scatter(data=df, x='Year', y='CSIRO Adjusted Sea Level', color='blue' ,marker='^', s=100 ,alpha=0.7)
   plt.title('Rise in Sea Level')
   plt.xlabel('Year')
   plt.ylabel('Sea Level (inches)')
   plt.legend()

    # Create first line of best fit
   slope1, intercept1, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level']) 
   years1 = list(range(df['Year'].min(), 2051))
   predicted_sea_levels1 = [slope1 * year + intercept1 for year in years1] 
   plt.plot(years1, predicted_sea_levels1, 'r', label="Best Fit (All Data)")

    # Create second line of best fit
   df_recent = df[df['Year'] >= 2000]
   slope2, intercept2, _, _, _ = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
   years2 = list(range(2000, 2051))
   predicted_sea_levels2 = [slope2 * year + intercept2 for year in years2]
   plt.plot(years2, predicted_sea_levels2, 'g', label="Best Fit (2000-Present)")


    # Add labels and title
   plt.xlabel("Year")
   plt.ylabel("Sea Level (inches)")
   plt.title("Rise in Sea Level")
   plt.legend()
   plt.grid(True)
    
    # Save plot and return data for testing (DO NOT MODIFY)
   plt.savefig('sea_level_plot.png')
   return plt.gca()