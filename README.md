# Exoplanet Mini Project 🌌

A quick analysis of **confirmed exoplanets** using NASA Exoplanet Archive data.

## Libraries Used
- `pandas` – data loading and cleaning
- `numpy` – numerical operations (log scaling, filtering)
- `matplotlib` – dark-themed scientific visualizations

## What This Does
1. Downloads the latest confirmed planet data directly from NASA's TAP service.
2. Cleans the dataset (keeps planets with both radius and orbital period).
3. Produces a 4-panel dashboard:
   - Top discovery methods
   - Radius vs orbital period (log-log)
   - Discoveries per year
   - Planet radius distribution (shows the "radius valley")
4. Filters a rough "habitable-zone candidate" set.

## How to Run
```bash
pip install pandas numpy matplotlib
python exoplanet_analysis.py
