# My Take on The Program

I made my own version of mapping with another database: I took all the cities in the world and just marked the capitals. I also made the map open in a desktop application: this way, it's easier to visualize. It's a simple app, but I learned a lot making it. Thank you **MLH Global Hack Week**.

# Mapping with Python

A 1-hour workshop for **MLH Global Hack Week** — taking a real, messy government dataset and turning it into an interactive map of climate-related natural disasters using pandas and Folium.

## What you'll learn

- Cleaning and filtering a real-world dataset with pandas (47 columns, 16,000+ rows, lots of missing data)
- Thinking critically about data quality and bias (only ~17% of records have coordinates — what does that mean for our map?)
- Building interactive maps with [Folium](https://python-visualization.github.io/folium/)
- Encoding multiple dimensions of data visually (colour = disaster type, size = severity)

## Getting started

1. **Get the dataset** — go to [public.emdat.be/data](https://public.emdat.be/data), create a free account, and download disaster data. Filter settings used for this workshop:
   - Time period: 2000–2026
   - Classification / Countries: left blank (global, all types)
   - Historical (pre-2000) toggle: off
   - Export as `.xlsx`

2. Place the downloaded file in the `data/` folder.

3. Install dependencies:
   ```bash
   pip install pandas folium openpyxl jupyter
   ```

4. Open `notebooks/starter.ipynb` and follow along.

## Structure

- `notebooks/starter.ipynb` — follow-along version with `# TODO` prompts
- `notebooks/solution.ipynb` — complete worked solution
- `data/` — place your downloaded EM-DAT export here (not committed to git due to size)

## Data source

[EM-DAT](https://www.emdat.be/) — The International Disaster Database, maintained by CRED (Centre for Research on the Epidemiology of Disasters), UCLouvain.

## Further exploration

- [GDIS dataset](https://www.nature.com/articles/s41597-021-00846-6) — subnational geocoded disaster data
- [Our World in Data](https://ourworldindata.org/) — broader climate datasets
- `folium.plugins` — heatmaps, marker clusters, and time-animated maps
