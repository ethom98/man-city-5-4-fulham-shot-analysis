# ⚽ Man City 5–4 Fulham — Shot Analysis (Python + Matplotlib)

This project is a short, data-driven look at Manchester City’s 5–4 win over Fulham.  
All visualizations were created in Python (pandas + matplotlib) and exported in dark-mode for use on LinkedIn.

---

## 📊 Included Visuals  
- Half-pitch shot map  
- Team-separated shot outcome pies  
- Distance brackets (0–6m, 7–18m, 19m+)  
- Distance histograms  
- Average shot distance per outcome  
- Average xG per distance bracket  

---

## 🧪 Data Source  
Shot event data was manually collected from FBref:

🔗 https://fbref.com/en/matches/83f0391d/Fulham-Manchester-City-December-2-2025-Premier-League

Dataset fields include:
- Minute  
- Player  
- Squad  
- xG / PSxG  
- Outcome  
- Distance  

The cleaned dataset (`shots.csv`) is included in this repo for reproducibility.

---

## 🧵 Python Scripts (`/code`)
- **shot_outcomes_pies.py**  
  Generates the Manchester City + Fulham shot outcome pie charts (dark mode + transparent PNGs).

---

## 📄 Report  
The full PDF match analysis can be found in:  
`/report/ManCity_Fulham_ShotAnalysis.pdf`


