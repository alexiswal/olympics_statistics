# prerequisites import
import pandas as pd

# dataset import
df= pd.read_csv(filepath_or_buffer="/Users/alexiswallon/developpement/dataset/olympics_medals_country_wise.csv", sep=',', header=0)
print(df)

#dataframe cleaning
df = df.rename(columns=lambda column: column.strip())
print(df)
new_names = {"total_participation":"total_participations"}
df = df.rename(columns=new_names)
print(df.columns)

#medals statistics
print(df.columns)

max_medals = df["total_total"].max()#variables instantiation
max_medals_country = []#variables instantiation
min_medals = df["total_total"].min()#variables instantiation
min_medals_country = []#variables instantiation

for index, row in df.iterrows(): #statistics calculation
    if row["total_total"]==max_medals:
        max_medals_country.append(row["countries"])
    if row["total_total"]==min_medals:
        min_medals_country.append(row["countries"])

print("Le(s) pays ayant gagné le plus de médailles aux JO est", max_medals_country) #results display
print("Les pays ayant gagné le moins de médailles aux JO sont", min_medals_country) #results display

#Winter and summer performance comparison
countries_stronger_in_summer = [] #variables instantiation
countries_stronger_in_winter = [] #variables instantiation
df["winter_total"]= df["winter_total"].astype(str).str.replace(",","").astype(int) #data cleaning
df["summer_total"]= df["summer_total"].astype(str).str.replace(",","").astype(int) #data cleaning

for index, row in df.iterrows(): #comparison
    if row["winter_total"]>row["summer_total"]:
            countries_stronger_in_winter.append(row["countries"])
    else:
        countries_stronger_in_summer.append(row["countries"])

print("Le(s) pays ayant remporté davantages de médailles en hiver qu'en été sont", countries_stronger_in_winter) #results display

#winter olympics efficiency
df["winter_ratio"]= df["winter_total"]/df["winter_participations"]
for index, row in df.iterrows():
     if row["countries"] in countries_stronger_in_winter:
          print("Leur ratio est précisément de :",row["countries"],":",row["winter_ratio"])

print("Au total, les pays ayant le meilleur ratio aux jeux d'hiver sont:", df.sort_values(by="winter_ratio", ascending=False).head(5)["countries"])

#total less efficiency
