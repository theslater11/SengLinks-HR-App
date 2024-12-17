## Question 1

Take a look at the file labeled `data/data2.txt`. Why might we have missing values or values that state "NO SIGNAL" in this dataset? While we are currently ignoring these values, what might be the risk of filtering these values out?

User Error or Technical malfunction are likely causes. If source of the error is not corrected it can get worse and corrupt the dataset.

## Question 2

While the "averages.png" and "maximums.png" graphs visualize typical values in our time-series data of heart rates and subsequently describe similar trends, the "stdevs.png" graph visualizes the standard deviations, which results in a graph with less apparent trends. In the context of heart rate, what does the standard deviation describe?

The numerical distance of each individual value from a selected value that best represents the center of the dataset. By individually comparing each value to this 'standard', we can chart how much the data varies from point to point. This is what is represented on the chart, rather than the values of the data itself.

## Question 3

Run your `main.py` module and look at the graph labeled "averages.png." Roughly speaking, where do you see the time series experience a significant difference in values along the x-axis? Point out all x-values where you notice a drastic difference in future values.

At 10 heart rate experiances a noticable, sustained increase until 30 is hit. There is a dropoff back to pre-10 levels thereafter.

## Question 4

Do you also notice a corresponding difference in values in the "stdevs.png" graph? If so, do these differences align with the "averages.png" graph? 

The values along the axis' remain unchanged but the charts do not align. There is a similar spike at 10, but seemingly random fluctuations after that the other two charts do not have.
