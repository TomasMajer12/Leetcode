


import pandas as pd

data = [[1, 1], [1, 2], [1, 3], [2, 1], [2, 4]]
project = pd.DataFrame(data, columns=['project_id', 'employee_id']).astype({'project_id':'Int64', 'employee_id':'Int64'})
data = [[1, 'Khaled', 3], [2, 'Ali', 2], [3, 'John', 1], [4, 'Doe', 2]]
employee = pd.DataFrame(data, columns=['employee_id', 'name', 'experience_years']).astype({'employee_id':'Int64', 'name':'object', 'experience_years':'Int64'})

"""
Write an SQL query that reports the average experience
 years of all the employees for each project, rounded to 2 digits.
"""
def project_employees_i(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(project, employee, how='left')
    return df[['project_id','experience_years']
                    ].groupby('project_id').mean().round(2).reset_index(
                    ).rename(columns = {'experience_years':'average_years'})

print(project_employees_i(project,employee))

