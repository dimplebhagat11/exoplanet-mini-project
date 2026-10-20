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

## Findings

- **Transit method dominates** the dataset — the vast majority of confirmed planets were found this way, driven by space telescopes like Kepler and TESS.
- The **radius vs period log-log plot** shows a cluster of "hot Jupiters" at short periods and large radii, separate from the smaller, longer-period population.
- The **radius histogram** shows a visible dip around ~1.8 Earth radii — the "radius valley," a known astrophysical feature.
- A rough habitable-zone filter (radius 0.8–1.5 R⊕, period 200–500 days) returns a small number of Earth-like candidates, printed by the script.

## Limitations

- The habitable-zone filter is a simplified approximation, not the full Kopparapu et al. formula.
- Some planets have missing radius/period data and were dropped before analysis.

## How to Run
```bash
pip install pandas numpy matplotlib
python exoplanet_analysis.py
