X_train = []
y_train = []
for i in range(60, val):
    X_train.append(train_s[i-60:i, 0])
    y_train.append(train_s[i, 0])
X_train, y_train = np.array(X_train), np.array(y_train)

X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))
