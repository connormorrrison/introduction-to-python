import matplotlib.pyplot as plt
import numpy as np


# Plot 1: Line chart
def line_chart(x, y):
    x = [1, 2, 3, 4, 5]
    y = [10, 12, 5, 8, 3]

    plt.plot(x, y)
    plt.title('Line Chart')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.show()


# Plot 2: Bar Chart
def bar_chart():
    categories = ['A', 'B', 'C', 'D']
    values = [25, 40, 30, 20]

    plt.bar(categories, values)
    plt.title('Bar Chart')
    plt.xlabel('Categories')
    plt.ylabel('Values')
    plt.show()


# Plot 3: Pie Chart
def pie_chart():
    labels = ['Category A', 'Category B', 'Category C']
    sizes = [30, 45, 25]

    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.title('Pie Chart')
    plt.show()


# Plot 4: Histogram
def histogram():
    data = np.random.randn(1000)

    plt.hist(data, bins=30, edgecolor='black')
    plt.title('Histogram')
    plt.xlabel('Values')
    plt.ylabel('Frequency')
    plt.show()


# Plot 5: Scatter Plot
def scatter_plot():
    x = np.random.rand(50)
    y = 2 * x + 1 + 0.1 * np.random.randn(50)

    plt.scatter(x, y)
    plt.title('Scatter Plot')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.show()


def main():
    line_chart()
    bar_chart()
    pie_chart()
    histogram()
    scatter_plot()


if __name__ == "__main__":
    main()
