import pandas as pd
import sqlite3

df = pd.read_csv("all_job_post.csv")

conn = sqlite3.connect("jobs.db")
df.to_sql("jobs", conn, if_exists="replace", index=False)

query = """
SELECT category, COUNT(*) as total_jobs
FROM jobs
GROUP BY category
ORDER BY total_jobs DESC
"""
result = pd.read_sql(query, conn)
print(result)

# Skills analysis - SQL + Python combo
import ast
from collections import Counter

df['skills_list'] = df['job_skill_set'].apply(
    lambda x: [s.strip().lower() for s in ast.literal_eval(x)]
)

query2 = """
SELECT category, job_title
FROM jobs
WHERE category = 'INFORMATION-TECHNOLOGY'
LIMIT 5
"""
it_jobs = pd.read_sql(query2, conn)
print("\nSample IT job titles:\n", it_jobs)