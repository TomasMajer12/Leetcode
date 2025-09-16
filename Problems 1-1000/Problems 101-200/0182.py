

import pandas as pd
data = [[1, 'a@b.com'], [2, 'c@d.com'], [3, 'a@b.com']]
person = pd.DataFrame(data, columns=['id', 'email']).astype({'id':'Int64', 'email':'object'})

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    dups = person[person.duplicated(subset='email', keep=False)].sort_values(by='email').reset_index(drop=True)
    return pd.DataFrame(dups["email"].unique(), columns=["Email"])

print(duplicate_emails(person))