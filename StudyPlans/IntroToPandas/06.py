import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    customers['email'] = customers['email'].drop_duplicates()
    return customers.dropna()
