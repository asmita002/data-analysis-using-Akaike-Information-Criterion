def computeAIC(X, Y, k=2):
    n = len(Y)
    model = lm()
    model.fit(X, Y)
    RSS = mean_squared_error(Y, model.predict(X)) * len(Y)
    return n*np.log(RSS/n) + k*X.shape[1]
def stepAIC(X, Y, features = X.columns, AIC = True):
    AIC_list, action_list, feature_list = [], [], []
    best_AIC = np.inf
    best_action = ' '
    n = len(Y)
    if AIC:
        k = 2
    else:
        k = np.log(n)
    AIC = computeAIC(X[features], Y, k)
    while(AIC < best_AIC):
        AIC_list.append(AIC)
        feature_list.append(list(features))
        action_list.append(best_action)
        best_AIC = AIC
        tmp_AIC_list, tmp_action_list, tmp_feature_list = [], [], []
        for p in features:
            tmp_features = features.drop(p)
            tmp_AIC = computeAIC(X[tmp_features], Y, k)
            tmp_AIC_list.append(tmp_AIC)
            tmp_feature_list.append(tmp_features)
            tmp_action_list.append('- ' + p)
        remaining_features = [p for p in X.columns if p not in features]
        for p in remaining_features:
            tmp_features = list(features) + [p]
            tmp_AIC = computeAIC(X[tmp_features], Y, k)
            tmp_AIC_list.append(tmp_AIC)
            tmp_feature_list.append(tmp_features)
            tmp_action_list.append('+ ' + p)
        best_model = np.array(tmp_AIC_list).argmin()
        AIC = tmp_AIC_list[best_model]
        features = tmp_feature_list[best_model]
        best_action = tmp_action_list[best_model]
    return pd.DataFrame({'AIC': AIC_list,
                         'action': action_list,
                       'features': feature_list})
