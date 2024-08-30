import sys

from langchain.tools import tool
import matplotlib.pyplot as plt

@tool('chart_generator', return_direct=False)
def chart_generator(data: list, chart_type: str) -> str:
    """Generates a chart from the provided data and chart type."""
    try:
        if chart_type == 'line':
            plt.plot(data)
            plt.title('Line Chart')
        elif chart_type == 'bar':
            plt.bar(range(len(data)), data)
            plt.title('Bar Chart')
        elif chart_type == 'scatter':
            plt.scatter(range(len(data)), data)
            plt.title('Scatter Plot')
        else:
            return 'Error: Unsupported chart type.'
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.savefig('chart.png')
        plt.close()
        return 'Chart generated successfully and saved as chart.png.'
    except:
        return 'Error: ' + str(sys.exc_info())