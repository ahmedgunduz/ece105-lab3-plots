"""Generate publication-quality sensor data visualizations.

This script creates synthetic temperature sensor data using NumPy
and produces scatter, histogram, and box plot visualizations saved
as PNG files.

Usage
-----
    python generate_plots.py
"""
# Create a function generate_data(seed) that returns sensor_a, sensor_b,
# and timestamps arrays with the same parameters as in the notebook.
# Use NumPy-style docstring with Parameters and Returns sections.
def generate_data(seed):
    """
    Generate synthetic temperature sensor readings.

    Parameters
    ----------
    seed : int
        Random number generator seed for reproducibility.

    Returns
    -------
    sensor_a : numpy.ndarray
        Temperature readings from sensor A in Celsius, shape (200,).
    sensor_b : numpy.ndarray
        Temperature readings from sensor B in Celsius, shape (200,).
    timestamps : numpy.ndarray
        Measurement timestamps in seconds, shape (200,).
    """
    rng = np.random.default_rng(seed=seed)

    timestamps = rng.uniform(0.0, 10.0, 200)
    sensor_a = rng.normal(25.0, 3.0, 200)
    sensor_b = rng.normal(27.0, 4.5, 200)

    return sensor_a, sensor_b, timestamps

import numpy as np

def generate_data(seed):
    """
    Generate simulated temperature readings from two sensors with timestamps.

    This function creates synthetic sensor data for analysis and visualization,
    simulating temperature measurements from two sensors over a 10-second period.

    Parameters
    ----------
    seed : int
        The seed for the random number generator to ensure reproducible results.
        Should be the last 4 digits of the user's Drexel ID.

    Returns
    -------
    timestamps : ndarray of shape (200,)
        Uniformly distributed timestamps from 0 to 10 seconds.
    sensor_a : ndarray of shape (200,)
        Temperature readings for Sensor A, normally distributed with mean 25°C and std 3°C.
    sensor_b : ndarray of shape (200,)
        Temperature readings for Sensor B, normally distributed with mean 27°C and std 4.5°C.
    """
    rng = np.random.default_rng(seed=seed)
    timestamps = rng.uniform(0, 10, 200)
    sensor_a = rng.normal(25, 3, 200)
    sensor_b = rng.normal(27, 4.5, 200)
    return timestamps, sensor_a, sensor_b

# Create plot_scatter(sensor_a, sensor_b, timestamps, ax) that draws
# the scatter plot from the notebook onto the given Axes object.
# NumPy-style docstring. Modifies ax in place, returns None.

def plot_scatter(sensor_a, sensor_b, timestamps, ax):
    """
    Create a scatter plot of sensor readings over time on the given Axes.

    Plots temperature readings from two sensors against their timestamps,
    using blue for Sensor A and orange for Sensor B.

    Parameters
    ----------
    sensor_a : array-like
        Temperature readings for Sensor A.
    sensor_b : array-like
        Temperature readings for Sensor B.
    timestamps : array-like
        Time values corresponding to the readings.
    ax : matplotlib.axes.Axes
        The Axes object on which to draw the scatter plot.

    Returns
    -------
    None
        Modifies the input Axes object in place.
    """
    ax.scatter(timestamps, sensor_a, color='blue', label='Sensor A', alpha=0.7)
    ax.scatter(timestamps, sensor_b, color='orange', label='Sensor B', alpha=0.7)
    ax.set_xlabel('Timestamp (seconds)')
    ax.set_ylabel('Sensor Reading (°C)')
    ax.set_title('Sensor Readings vs Time')
    ax.legend()
    ax.grid(True, alpha=0.3)

# Create plot_histogram(sensor_a, sensor_b, ax) that draws
# the overlaid histogram from the notebook onto the given Axes object.
# NumPy-style docstring. Modifies ax in place, returns None.

def plot_histogram(sensor_a, sensor_b, ax):
    """
    Create an overlaid histogram of sensor temperature distributions on the given Axes.

    Plots histograms for both sensors with 30 bins, transparency, and mean lines.

    Parameters
    ----------
    sensor_a : array-like
        Temperature readings for Sensor A.
    sensor_b : array-like
        Temperature readings for Sensor B.
    ax : matplotlib.axes.Axes
        The Axes object on which to draw the histogram.

    Returns
    -------
    None
        Modifies the input Axes object in place.
    """
    ax.hist(sensor_a, bins=30, alpha=0.5, label='Sensor A', color='blue')
    ax.hist(sensor_b, bins=30, alpha=0.5, label='Sensor B', color='orange')
    ax.axvline(np.mean(sensor_a), color='blue', linestyle='--', linewidth=2, label='Mean Sensor A')
    ax.axvline(np.mean(sensor_b), color='orange', linestyle='--', linewidth=2, label='Mean Sensor B')
    ax.set_xlabel('Temperature (°C)')
    ax.set_ylabel('Frequency')
    ax.set_title('Overlaid Histograms of Sensor Temperature Distributions')
    ax.legend()