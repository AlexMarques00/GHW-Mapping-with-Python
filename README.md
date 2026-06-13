# World Capitals Tracker 🌍
> **My Take on The Program:** I built my own version of this mapping project using a different database. Instead of tracking disasters, I extracted all world cities and mapped out exclusively national capitals. I also ported the entire project into a native desktop application using **PyQt5** to provide a cleaner, standalone visualization tool. It’s a simple app, but I learned a lot about data engineering and GUI integration making it. 
> 
> Thank you, **MLH Global Hack Week**!

---

## 🚀 How to Run (My Desktop Version)
You don't need to manually configure your environment or install dependencies via terminal. 

1. Ensure you have Python installed.
2. Download the project files.
3. Simply double-click the **[start.bat](start.bat)** file. 

The batch script will automatically handle the setup (`requirements.txt`), download the dataset via `kagglehub`, and launch the desktop map app window instantly.

### 🛠️ Built With (Desktop App)
* **Python** & **Pandas** (Data cleaning & filtering)
* **Folium / Leaflet** & **Esri Tiles** (Geospatial visualization & infinite horizontal scroll)
* **PyQt5** & **PyQtWebEngine** (Desktop GUI & Chromium rendering engine)

---

# Mapping with Python (Original Workshop Context)

A 1-hour workshop for **MLH Global Hack Week** — taking a real, messy government dataset and turning it into an interactive map of climate-related natural disasters using pandas and Folium.

## What you'll learn

- Cleaning and filtering a real-world dataset with pandas (47 columns, 16,000+ rows, lots of missing data)
- Thinking critically about data quality and bias (only ~17% of records have coordinates — what does that mean for our map?)
- Building interactive maps with [Folium](https://python-visualization.github.io/folium/)
- Encoding multiple dimensions of data visually (colour = disaster type, size = severity)

## Getting started (Workshop Version)

1. **Get the dataset** — go to [public.emdat.be/data](https://public.emdat.be/data), create a free account, and download disaster data. Filter settings used for this workshop:
   - Time period: 2000–2026
   - Classification / Countries: left blank (global, all types)
   - Historical (pre-2000) toggle: off
   - Export as `.xlsx`

2. Place the downloaded file in the `data/` folder.

3. Install dependencies:
   ```bash
   pip install pandas folium openpyxl jupyter