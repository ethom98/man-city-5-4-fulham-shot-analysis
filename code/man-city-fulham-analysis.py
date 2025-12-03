import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# -----------------------
# CONFIG
# -----------------------

# Path to your CSV (adjust if needed)
CSV_PATH = Path("../shots.csv")

# Output folder for PNGs
OUTPUT_DIR = Path("../output")
OUTPUT_DIR.mkdir(exist_ok=True)

# Dark mode
plt.style.use("dark_background")

# Outcome colors (your custom mapping)
OUTCOME_COLORS = {
    "Goal": "#2ecc71",       # green
    "Saved": "#3498db",      # blue
    "Blocked": "#f1c40f",    # yellow
    "Off Target": "#e74c3c", # red
    "Woodwork": "#e67e22",   # orange
}

# -----------------------
# LOAD DATA
# -----------------------

df = pd.read_csv(CSV_PATH)

# Clean up any stray spaces
df["Outcome"] = df["Outcome"].str.strip()
df["Squad"]   = df["Squad"].str.strip()

# Just to be safe, print the unique outcomes once
print("Outcomes in data:", df["Outcome"].unique())
print("Teams in data:", df["Squad"].unique())

# -----------------------
# PLOT FUNCTION
# -----------------------

def plot_team_shot_outcomes(team_name: str):
    """
    Create a pie chart of shot outcomes for a single team
    and save it as a transparent PNG.
    """
    team_df = df[df["Squad"] == team_name]

    if team_df.empty:
        print(f"[WARN] No shots found for team: {team_name}")
        return

    counts = team_df["Outcome"].value_counts()

    # Make sure colors align with outcomes present
    colors = [OUTCOME_COLORS[o] for o in counts.index]

    fig, ax = plt.subplots(figsize=(6, 6))  # square for LinkedIn

    wedges, texts, autotexts = ax.pie(
        counts.values,
        labels=counts.index,
        colors=colors,
        autopct="%.1f%%",
        startangle=90,
        wedgeprops={"edgecolor": "black"}
    )

    ax.set_title(f"{team_name} – Shot Outcomes", color="white")

    # Transparent background PNG for overlays
    out_name = f"{team_name.replace(' ', '_').lower()}_shot_outcomes.png"
    out_path = OUTPUT_DIR / out_name

    fig.savefig(out_path, dpi=300, bbox_inches="tight", transparent=True)
    plt.close(fig)

    print(f"[OK] Saved: {out_path}")

# -----------------------
# RUN FOR BOTH TEAMS
# -----------------------

plot_team_shot_outcomes("Manchester City")
plot_team_shot_outcomes("Fulham")
