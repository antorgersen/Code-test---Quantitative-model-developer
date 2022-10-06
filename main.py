import pandas as pd
import geopy.distance as dis

df = pd.read_csv("places.csv", sep=";")

n = input("Write the number of places you want to use: ")

if n:
    n = int(n)
    df = df.sample(n=n)

distance_dict = dict()
for i in range(len(df.index)):
    for j in range(len(df.index)):
        if i >= j:
            continue
        coords_1 = (df.iloc[i, 1], df.iloc[i, 2])
        coords_2 = (df.iloc[j, 1], df.iloc[j, 2])
        distance = round(dis.geodesic(coords_1, coords_2).km,1)
        print(df.iloc[i, 0], df.iloc[j, 0], distance, "km")
        distance_dict[distance] = [df.iloc[i, 0], df.iloc[j, 0]]

average = round(sum(distance_dict.keys())/len(distance_dict.keys()))
closest_distance = min(distance_dict, key=lambda x: abs(x-average))

print("Average distance:", average, "km. Closest pair:",  distance_dict[closest_distance][0],
      distance_dict[closest_distance][1], closest_distance, "km.")





