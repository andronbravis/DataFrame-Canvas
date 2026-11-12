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

result = inspect_namespace(globals().copy())

test_df = pd.DataFrame()

def scope_test():
    test_df2 = pd.DataFrame()

    # should print all dataframes apart from test_df2 which is local to the scope_test function
    print(inspect_namespace(globals().copy()))

    # should print only test_df2 which is the only local variable inside the function its called from
    print(inspect_namespace(locals().copy()))

scope_test()