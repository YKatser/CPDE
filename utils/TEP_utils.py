from sklearn.preprocessing import StandardScaler
import ruptures as rpt


def dynp(model, data, params):
    ttf = []
    for i in data.keys():
        signal = StandardScaler().fit_transform(data[i].values)
        algo = rpt.Dynp(model=model, 
                        params=params, 
                        jump=1).fit(signal)

        my_bkps = algo.predict(n_bkps=1)
        ttf.append(my_bkps[0]-160)
    return pd.DataFrame({(model+' '+str(*params.values())): ttf}).T