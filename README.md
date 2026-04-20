# ECE105 Lab 3 Sensor Plots

A Python script that generates synthetic temperature sensor data and creates publication-quality visualizations including scatter plots, histograms, and box plots.

## Installation

1. Activate the `ece105` conda environment:
   ```
   conda activate ece105
   ```

2. Install required dependencies:
   ```
   conda install numpy matplotlib
   ```
   or
   ```
   mamba install numpy matplotlib
   ```

## Usage

Run the script from the command line:
```
python generate_plots.py
```

The script will generate synthetic sensor data and save a combined plot figure.

## Example Output

The script produces a single PNG file `sensor_analysis.png` containing three side-by-side plots:

- **Scatter Plot**: Temperature readings from two sensors plotted against time, showing the temporal distribution of measurements.
- **Histogram**: Overlaid histograms of temperature distributions for both sensors, with vertical lines marking the mean values.
- **Box Plot**: Side-by-side box plots comparing the statistical distributions of both sensors, including an overall mean reference line.

All plots use consistent color coding (blue for Sensor A, orange for Sensor B) and are optimized for 150 DPI publication quality.

## AI Tools Used and Disclosure

[Placeholder: Describe any AI tools used in development and provide appropriate disclosure.]