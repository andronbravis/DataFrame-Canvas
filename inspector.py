import pandas as pd

def inspect_namespace(namespace: dict) -> list:
    res = dict()

    for name, value in namespace.items():
        if isinstance(value, pd.DataFrame):
            key = id(value)
            if key not in res.keys():
                res[key] = {'names': [], 'shape' : value.shape, 'columns' : [], 'preview' : [], 'index' : []}   
                for column, dtype in value.dtypes.items():
                    res[key]['columns'].append((column, str(dtype)))
                for row in value.iloc[:10].itertuples(index=False):
                    res[key]['preview'].append(list(row))
                res[key]['index'] = value.iloc[:10].index.tolist()
            res[key]['names'].append(name)

    return list(res.values())
