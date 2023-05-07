import matplotlib.pyplot as plt
import pandas

def plot_insertion_sort():
    data = pandas.read_csv("sorting_algorithms.csv")

    # Call plot three times to make three different lines
    plt.plot(data["Array Size"], data["Insertion (Ascending)"])
    plt.plot(data["Array Size"], data["Insertion (Descending)"])
    plt.plot(data["Array Size"], data["Insertion (Random)"])

    # Set the titles, as usual
    plt.xlabel("Size of Array")
    plt.ylabel("Average Number of Steps")
    plt.title("Insertion Sort Complexity by Array Size")

    # Add a legend to the graph by giving it a list of labels.
    # There are more sophisticated ways to do this, but they go beyond our Python
    # knowledge by a lot.
    plt.legend(["Ascending Order", "Descending Order", "Random Order"])
    
    # And show it!
    plt.savefig("insertion_labels.png")


def plot_merge_sort():
    data = pandas.read_csv("sorting_algorithms.csv")

    # Call plot three times to make three different lines
    plt.plot(data["Array Size"], data["Merge (Ascending)"])
    plt.plot(data["Array Size"], data["Merge (Descending)"])
    plt.plot(data["Array Size"], data["Merge (Random)"])

    # Set the titles, as usual
    plt.xlabel("Size of Array")
    plt.ylabel("Average Number of Steps")
    plt.title("Insertion Sort Complexity by Array Size")

    # Add a legend to the graph by giving it a list of labels.
    # There are more sophisticated ways to do this, but they go beyond our Python
    # knowledge by a lot.
    plt.legend(["Ascending Order", "Descending Order", "Random Order"])
    
    # And show it!
    plt.show()

def plot_sort_comparison():
    pass

if __name__ == "__main__":
    plot_insertion_sort()
