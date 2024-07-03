import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('ggplot')
pd.set_option(
    "display.max_columns", None
)
# Load data
df = pd.read_csv("/Users/jsc/Downloads/nba_games.csv")
# data preperation
df = df.sort_values("date")
df = df.reset_index(drop=True)

del df["mp.1"]
del df["mp_opp.1"]
del df["index_opp"]
del df[df.columns[0]]

def add_target(team):
    team["target"] = team["won"].shift(-1)
    return team
df = df.groupby("team", group_keys=False).apply(add_target)
