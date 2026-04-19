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