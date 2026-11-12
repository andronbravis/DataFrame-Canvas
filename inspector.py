import pandas as pd

def inspect_namespace(namespace: dict) -> list:
    res = dict()

    for name, value in namespace.items():
        if isinstance(value, pd.DataFrame):
            key = id(value)
            if key not in res.keys():
                res[key] = {'names': [], 'shape' : value.shape}   
            res[key]["names"].append(name)

    return list(res.values())