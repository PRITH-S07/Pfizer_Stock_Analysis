test_data=df.iloc[val:, 1:2].values

inputs = df[len(df) - (len(df)-val) - 60:]['Open'].values
inputs = inputs.reshape(-1,1)
inputs = scaler.transform(inputs)
X_test = []
for i in range(60, (len(df)-val+1)+60):
    X_test.append(inputs[i-60:i, 0])
X_test = np.array(X_test)
X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))
predicted_stock_price = seq.predict(X_test)
predicted_stock_price = scaler.inverse_transform(predicted_stock_price)
