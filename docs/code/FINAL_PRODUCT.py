import pandas as pd
import matplotlib.pyplot as plt

def read_and_plot():
    # Read in the CSV
    data = pd.read_csv("simple_data.csv")

    # Plot the data with the X axis "Year" and the Y axis "Value (fake)"
    plt.plot(data["Year"], data["Ability to be the Future"])

    # Set the labels on the graph to appropriate stuff
    plt.xlabel("Year")
    plt.ylabel("Ability to be the Future")
    plt.title("The Future Comes for Us All...")

    # Put a horizontal line at Y = 0 to represent when the future starts
    plt.axhline(y=0, color='r', linestyle='-')

    # Once we're done with visual changes, show the plot!
    plt.show()

if __name__ == "__main__":
    read_and_plot()
