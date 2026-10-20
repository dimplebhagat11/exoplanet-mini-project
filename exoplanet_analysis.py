"""
Exoplanet Mini Project - NASA Exoplanet Archive Analysis
Author: Dimple Bhagat UID: 26MCD10002
Libraries: pandas, numpy, matplotlib
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ---------- 1. Load data ----------
# Direct download URL (CSV format, Planetary Systems Composite Parameters table)
url = ("https://exoplanetarchive.ipac.caltech.edu/TAP/sync?"
       "query=select+pl_name,disc_year,discoverymethod,pl_rade,pl_orbper,pl_bmasse,st_teff"
       "+from+pscomppars&format=csv")

print("Downloading data from NASA Exoplanet Archive...")
df = pd.read_csv(url, comment='#')  # skip comment lines
print(f"Loaded {len(df)} confirmed planets.")

# ---------- 2. Clean data ----------
# Keep only rows with radius and orbital period
df_clean = df.dropna(subset=['pl_rade', 'pl_orbper']).copy()

# Habitable zone candidate filter (approx: radius 0.8-1.5 Earth, period 200-500 days)
habitable = df_clean[
    (df_clean['pl_rade'] >= 0.8) & (df_clean['pl_rade'] <= 1.5) &
    (df_clean['pl_orbper'] >= 200) & (df_clean['pl_orbper'] <= 500)
]
print(f"Habitable-zone candidates (rough filter): {len(habitable)}")

# ---------- 3. Plot with dark astronomy style ----------
plt.style.use('dark_background')  # built-in style [citation:3]

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('NASA Exoplanet Archive: Confirmed Planets',
             fontsize=16, y=0.98)

# --- Plot 1: Top 6 discovery methods ---
ax1 = axes[0, 0]
method_counts = df_clean['discoverymethod'].value_counts().head(6)
colors = plt.cm.plasma(np.linspace(0.2, 0.9, len(method_counts)))
bars = ax1.barh(method_counts.index, method_counts.values, color=colors)
ax1.set_xlabel('Number of Planets')
ax1.set_title('Top Discovery Methods')
ax1.invert_yaxis()
# Add value labels
for bar in bars:
    width = bar.get_width()
    ax1.text(width + 20, bar.get_y() + bar.get_height()/2,
             f'{int(width)}', va='center', fontsize=9, color='white')

# --- Plot 2: Radius vs Orbital Period (log-log) ---
ax2 = axes[0, 1]
scatter = ax2.scatter(df_clean['pl_orbper'], df_clean['pl_rade'],
                      c=np.log10(df_clean['pl_rade'] + 1),  # color by radius
                      cmap='plasma', s=8, alpha=0.6, edgecolors='none')
ax2.set_xscale('log')
ax2.set_yscale('log')
ax2.set_xlabel('Orbital Period (days)')
ax2.set_ylabel('Planet Radius (Earth radii)')
ax2.set_title('Radius vs Orbital Period')
ax2.axvline(365, color='cyan', linestyle='--', linewidth=0.8, alpha=0.5)
ax2.text(400, 0.5, '1 year', color='cyan', fontsize=8)
cbar = plt.colorbar(scatter, ax=ax2, label='log10(Radius+1)')
cbar.ax.yaxis.label.set_color('white')
cbar.ax.tick_params(colors='white')

# --- Plot 3: Discoveries per year ---
ax3 = axes[1, 0]
year_counts = df_clean['disc_year'].value_counts().sort_index()
ax3.plot(year_counts.index, year_counts.values,
         color='cyan', linewidth=2, marker='o', markersize=3)
ax3.fill_between(year_counts.index, year_counts.values,
                 alpha=0.3, color='cyan')
ax3.set_xlabel('Discovery Year')
ax3.set_ylabel('Planets Discovered')
ax3.set_title('Discovery Timeline')
ax3.grid(True, alpha=0.2, linestyle='--')

# --- Plot 4: Radius distribution (shows "radius valley") ---
ax4 = axes[1, 1]
ax4.hist(df_clean['pl_rade'], bins=60, range=(0, 25),
         color='mediumpurple', edgecolor='white', linewidth=0.3, alpha=0.8)
ax4.axvline(1.8, color='orange', linestyle='--', linewidth=1.2,
            label='Radius Valley (~1.8 R⊕)')
ax4.set_xlabel('Planet Radius (Earth radii)')
ax4.set_ylabel('Frequency')
ax4.set_title('Planet Radius Distribution')
ax4.legend(loc='upper right', fontsize=9)

plt.tight_layout()
plt.savefig('exoplanet_dashboard.png', dpi=150, bbox_inches='tight',
            facecolor='black')
print("Saved: exoplanet_dashboard.png")
plt.show()

# ---------- 4. Print a small summary ----------
print("\n--- Summary ---")
print(f"Total planets with radius & period: {len(df_clean)}")
print(f"Most common discovery method: {df_clean['discoverymethod'].mode()[0]}")
print(f"Median planet radius (Earth radii): {df_clean['pl_rade'].median():.2f}")