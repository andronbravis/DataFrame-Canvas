import pandas as pd
from inspector import inspect_namespace


mock_list = ['john', 'alice', 'fred']
count = 3
random_var = 'abcdefg'

names = pd.DataFrame(mock_list, columns=['Name'])
names_2 = names
names_copy = names.copy()
names.loc[0, 'Name'] = 'GEORGE'
names = names[names['Name'] != 'alice']
names_2.loc[2, 'Name'] = 'BOB'
names_alias = names

duplicate_columns = pd.DataFrame({
    "text": pd.Series(["Alice", "Bob"], dtype="string"),
    "number": pd.Series([10, 20], dtype="int64"),
})
duplicate_columns.columns = ["value", "value"]

preview_test = pd.DataFrame({
    "name": ["Alice", "Bob", "Cara", "Dan", "Eva", "Finn", "Gina", "Hugo", "Iris", "Jack", "Kate", "Leo"],
    "age": [24, 31, 27, 35, 22, 29, 33, 26, 28, 40, 25, 32],
    "score": [85, 72, 91, 64, 88, 79, 95, 81, 76, 90, 83, 87],
})

result = inspect_namespace(globals().copy())

test_df = pd.DataFrame()

def scope_test():
    test_df2 = pd.DataFrame()

    # should print all dataframes apart from test_df2 which is local to the scope_test function
    print(inspect_namespace(globals().copy()))

    # should print only test_df2 which is the only local variable inside the function its called from
    print(inspect_namespace(locals().copy()))

scope_test()