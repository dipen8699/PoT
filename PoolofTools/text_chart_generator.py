import sys

from langchain.tools import tool

@tool('text_chart_generator', return_direct=False)
def text_chart_generator(data: list, chart_type: str) -> str:
    """Generates a text-based chart from the provided data and chart type."""
    try:
        if chart_type == 'bar':
            max_value = max(data)
            chart = ''
            for value in data:
                chart += '*' * (value * 10 // max_value) + '\n'
            return chart
        else:
            return 'Error: Unsupported chart type. Only bar charts are supported.'
    except:
        return 'Error: ' + str(sys.exc_info())