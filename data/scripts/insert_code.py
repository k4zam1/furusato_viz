
import pandas as pd
import logging as log

def insert(file):
    log.info("opening files...")
    df = pd.read_csv(file)
    codes = pd.read_csv("citys.csv")
    notfounds = set()

    log.info("inserting city codes...")
    for i in range(len(df)):
        cityname = df.city[i]
        if len(codes[codes.city == cityname].code.values) == 0:
            notfounds.add(df.city[i])
            continue
        df.code[i] = codes[codes.city == cityname].code.values[0]
    if(notfounds):
        log.info("not founds city codes :")
        for city in notfounds:
            print(city)
        return
    df.to_csv("withcode.csv",index=False)


if __name__=="__main__":
    log.basicConfig(level=log.INFO)
    insert("gifts.csv")