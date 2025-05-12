# 🚦 Crash Data Visualiser (Australia - QLD)

An interactive Python application that loads, analyzes, and visualizes real crash data from Queensland, Australia using `pandas` and `matplotlib`.

## 📊 Features

- Load real-world CSV crash data (not included in repo)
- Visualize crashes by:
  - Year
  - State
  - Road condition (pie chart)
- Export graph images to `charts/` folder
- Clean command-line menu
- Modular, readable code

## 🧰 Tech Stack

- Python 3.10+
- pandas
- matplotlib
- (Optional) requests

## 📥 Crash Dataset

⚠️ The full dataset (192MB) is **not included** in this repo due to GitHub file size limits.

**To run this project:**
1. Download the dataset manually from the official source:  
   👉 [QLD Gov Crash Data](https://www.data.qld.gov.au/dataset/crash-data-from-queensland-roads/resource/e88943c0-5968-4972-a15f-38e120d72ec0)

2. Rename it to: `crash_data.csv`

3. Place it inside the `/data` directory:


## 🚀 How to Run

1. Clone the repo  
```bash
git clone https://github.com/Dexter2099/Crash-Data-Vis.git
cd Crash-Data-Vis

python -m venv venv
venv\Scripts\activate   # or source venv/bin/activate
pip install -r requirements.txt

#Choose what to visualise from the menu
1. Crashes by Year
2. Crashes by State
3. Crashes by Road Condition
