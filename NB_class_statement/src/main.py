#!/bin/env python3

import pandas as pd
import numpy as np
#nltk.download('punkt_tab')


fp = r"../resources/statement.csv"
dfx = df = pd.read_csv(fp)

df = df.drop("Balance",axis=1)
df = df.drop("Amount", axis=1)
df = df.drop("Date", axis=1)
df = df.dropna()
df['Description'] = df['Description'].str.upper()
# descriptions = df["Description"]
# #df["tokens"]= df.apply(lambda row:
#                        nltk.word_tokenize(row["Description"]), axis=1)

# pancake = df["tokens"].to_numpy().flatten()
# flat_pancake = []
# for sublist in pancake:
#     for item in sublist:
#         flat_pancake.append(item)

# unclean_tokens = pd.DataFrame(pd.DataFrame(flat_pancake)[0].unique())
inclusion_list = ()
inclusion_list = (['BRUCE', 'PNP','FRUIT','TAKEALOT', 'ONLINE', 'CAR','TRAFFIC','ENGEN','WIMPY','KFC','BOUMAT','CSB','INTEREST','MR PRICE','PENS#ION','ROADHOUSE','ELECTRICITY','SPAR','FUNDS','STAND','VEG','YOUTUB','KWEKERY','TAKE','SKIP','APPLE.COM/BILL','SMS','WITHDRAWAL','ATM','CAFE','GOOGLE','BORDER','ADMED'])
inclusion_list

for ii in inclusion_list:
    df['containsExpr'] = df['Description'].str.contains(ii)
    filtered_df = df[df['containsExpr']]
    print(filtered_df)

    # dfx["Description"] = dfx["Description"].str.upper()
# dfx = dfx.dropna()
# #dfx
# #ncluded = dfx[np.isin(dfx["Description"],inclusion_list)]
# #included.head(50)
# newdf = pd.DataFrame({"Description","Category"})

# newdf.head(50)
    #tokens = pd.DataFrame(pancake)
#pancake

#token_list = list(map(set,tokens.values.T))
#pd.Series({c: tokens[c].unique() for c in tokens})
#pd.Series({c: tokens[c].unique() for c in tokens})

#df.head05
