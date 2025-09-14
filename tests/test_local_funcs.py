"""Tests for local_funcs package."""

from local_funcs import hello, example_data_processing_function


def test_hello():
    """Test the hello function."""
    result = hello()
    assert isinstance(result, str)
    assert "Hello from local_funcs!" in result


def test_example_data_processing_function():
    """Test the example data processing function."""
    input_data = [1, 2, 3, 4, 5]
    expected = [2, 4, 6, 8, 10]

    result = example_data_processing_function(input_data)

    assert result == expected
    assert len(result) == len(input_data)


def test_example_data_processing_function_empty():
    """Test processing function with empty input."""
    result = example_data_processing_function([])
    assert result == []


def test_example_data_processing_function_negative():
    """Test processing function with negative numbers."""
    input_data = [-1, -2, -3]
    expected = [-2, -4, -6]

    result = example_data_processing_function(input_data)
    assert result == expected
