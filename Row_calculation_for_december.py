import pandas as pd

df = pd.read_csv("/content/TOP 5 earning.csv")

df["date"] = pd.to_datetime(df["date"])

# create df without Mr_beast
df_filt = df[df["youtuber"] != "Mr_Beast"]

df_filt.groupby("youtuber")["estimation_earning_numeric"].mean()

# create a dictionary with new rows to be added later

d = {
    'date' : ['2024-12-01', '2024-12-01', '2024-12-01', '2024-12-01'],
    'estimation_earning' : ['504K', '2M', '531K', '1.3M'],
    'estimation_earning_numeric' : [504136, 2004000, 531863, 1295182],
    'youtuber' : ['A4', 'KIMPRO', 'Stokes_Twins', 'alan_chikin_chow']

}

df_new = pd.DataFrame(d)

# concatenate both dataframes
df_full = pd.concat([df, df_new], axis = 0)

# make sure that date is in format date

df_full['date'] = pd.to_datetime(df_full["date"])

# download the full df
df_full.to_csv("df_full.csv", index = False)