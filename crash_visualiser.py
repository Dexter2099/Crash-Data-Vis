# 📂 File: crash_visualiser.py
# 🚦 Australian Crash Data Visualiser
# 🧠 Tools: pandas, matplotlib
# 🧑‍💻 Created by: Dexter

import os
import sys
import pandas as pd
import matplotlib.pyplot as plt

# 🔧 Config
DATA_DIR = "data"
CHARTS_DIR = "charts"
DATA_FILE = "crash_data.csv"  # Ensure this exists in /data

# 🚨 Ensure required directories exist
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(CHARTS_DIR, exist_ok=True)

def load_data():
    """Loads the crash data CSV into a pandas DataFrame"""
    path = os.path.join(DATA_DIR, DATA_FILE)
    if not os.path.exists(path):
        print(f"❌ Data file not found at {path}")
        sys.exit(1)

    print("📥 Loading data...")
    df = pd.read_csv(path)
    print(f"✅ Data loaded: {len(df)} rows")
    return df

def show_menu():
    """Displays the CLI menu and returns user choice"""
    print("\n📊 What would you like to visualise?")
    print("1. Crashes by Year")
    print("2. Crashes by State")
    print("3. Crashes by Road Condition")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")
    return choice.strip()

def plot_and_save(title, x, y, kind="bar", xlabel="", ylabel="Crashes"):
    """Generic plot function using matplotlib"""
    plt.figure(figsize=(10, 6))
    if kind == "pie":
        plt.pie(y, labels=x, autopct="%1.1f%%", startangle=90)
        plt.axis("equal")
    else:
        getattr(plt, kind)(x, y)

    plt.title(title)
    if kind != "pie":
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.xticks(rotation=45)

    # Save chart
    filename = f"{CHARTS_DIR}/{title.replace(' ', '_').lower()}.png"
    plt.tight_layout()
    plt.savefig(filename)
    plt.show()
    print(f"✅ Chart saved to {filename}")

def visualise_crashes_by_year(df):
    """Groups and plots crash counts by year"""
    if "Crash_Year" not in df.columns:
        print("❌ 'Crash_Year' column not found in dataset.")
        return
    grouped = df["Crash_Year"].value_counts().sort_index()
    plot_and_save("Crashes by Year", grouped.index.astype(str), grouped.values, kind="bar", xlabel="Year")

def visualise_crashes_by_state(df):
    """Groups and plots crash counts by state"""
    if "State" not in df.columns:
        print("❌ 'State' column not found in dataset.")
        return
    grouped = df["State"].value_counts()
    plot_and_save("Crashes by State", grouped.index, grouped.values, kind="bar", xlabel="State")

def visualise_crashes_by_road_condition(df):
    """Groups and plots crash counts by road condition"""
    col = "Road_Condition"
    if col not in df.columns:
        print(f"❌ '{col}' column not found in dataset.")
        return
    grouped = df[col].value_counts()
    plot_and_save("Crashes by Road Condition", grouped.index, grouped.values, kind="pie")

def main():
    df = load_data()

    while True:
        choice = show_menu()
        if choice == "1":
            visualise_crashes_by_year(df)
        elif choice == "2":
            visualise_crashes_by_state(df)
        elif choice == "3":
            visualise_crashes_by_road_condition(df)
        elif choice == "4":
            print("👋 Exiting.")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
