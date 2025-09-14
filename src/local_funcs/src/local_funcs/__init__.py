"""Local utility functions for data science projects."""

__version__ = "0.1.0"


def hello() -> str:
    """Return a greeting message.

    Returns:
        A simple greeting string
    """
    return "Hello from local_funcs!"


def example_data_processing_function(data: list) -> list:
    """Example function for data processing.

    Args:
        data: Input data list to process

    Returns:
        Processed data with each item doubled
    """
    return [item * 2 for item in data]
