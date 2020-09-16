import pandas as pd

def main():
    data = pd.read_csv("municipality.csv")
    latlong = pd.read_csv("citylatlong.csv")

    datalength = len(data.code)
    for i in range(datalength):
        code = data.code[i]
        city = latlong[latlong.code == code]
        if city.empty :
            continue

        idxlat = 3
        idxlon = 4
        data.iloc[i,idxlat] = city.latitude.values[0]
        data.iloc[i,idxlon] = city.longitude.values[0]
    data.to_csv("cleaned.csv",index=False)

if __name__ == "__main__":
    main()