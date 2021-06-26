val=math.floor(98/100*len(df))-1

train_data=df.iloc[:val, 1:2].values
