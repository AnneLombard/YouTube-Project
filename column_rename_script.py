import pandas as pd

# Assurez-vous que le chemin du fichier est correct et inclut l'extension .csv
df = pd.read_csv('stockes_twins')

# Afficher les premières lignes pour vérifier le chargement
df
df.columns = df.columns.str.replace(" ", "_").str.lower()
#remplacer les espace par '_'
def to_seconds(s) :

  return float(s.split(":")[0]) * 60 + float(s.split(":")[1])


df["video_seconds"] = df["duration"].map(to_seconds)
# creation d'une fonction pour convertir la durée des vidéos en secondes
df.to_csv("stockes_twins_channel.csv", index=False) # CSV Exportation 