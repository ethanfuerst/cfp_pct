import pandas as pd

# implied winning percentages for each team
UT_wp = 0.82
UW_wp = 0.3
UGA_wp = 0.6
FSU_wp = 0.6
UM_wp = 0.98

lookup_dict = {
    "UT": UT_wp,
    "UW": UW_wp,
    "UGA": UGA_wp,
    "FSU": FSU_wp,
    "UM": UM_wp,
    "OKST": 1 - UT_wp,
    "ORE": 1 - UW_wp,
    "ALA": 1 - UGA_wp,
    "LOU": 1 - FSU_wp,
    "UI": 1 - UM_wp,
    "OSU": 0,
}

df = pd.read_csv("scenarios.csv")
df["PAC12_wp"] = df["PAC12"].map(lookup_dict)
df["BIG12_wp"] = df["BIG12"].map(lookup_dict)
df["SEC_wp"] = df["SEC"].map(lookup_dict)
df["ACC_wp"] = df["ACC"].map(lookup_dict)
df["BIG10_wp"] = df["BIG10"].map(lookup_dict)

# multiply them together to get pct of each outcome
df["wp"] = (
    df["PAC12_wp"] * df["BIG12_wp"] * df["SEC_wp"] * df["ACC_wp"] * df["BIG10_wp"]
)

# add them together for a team and boom that is the playoff pct
for key in lookup_dict:
    playoff_pct = (
        df[
            (df["r1"] == key)
            | (df["r2"] == key)
            | (df["r3"] == key)
            | (df["r4"] == key)
        ]["wp"].sum()
    ) * 100
    if playoff_pct > 0:
        print(f"{key}'s playoff percentage is {playoff_pct:.2f}%")
