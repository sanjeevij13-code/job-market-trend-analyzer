import pandas as pd
import ast
from collections import Counter

df = pd.read_csv("all_job_post.csv")

# Skills clean pannurom - lowercase + strip pannitu duplicates avoid pannurom
df['skills_list'] = df['job_skill_set'].apply(
    lambda x: [s.strip().lower() for s in ast.literal_eval(x)]
)

# Category wise top 5 skills
for cat in df['category'].unique():
    skills = df[df['category'] == cat]['skills_list'].sum()
    top5 = Counter(skills).most_common(5)
    print(f"\n{cat}: {top5}")

# Overall top 15 skills
all_skills = df['skills_list'].sum()
print("\nTop 15 overall:", Counter(all_skills).most_common(15))

import matplotlib.pyplot as plt

top15 = Counter(all_skills).most_common(15)
skills, counts = zip(*top15)

plt.figure(figsize=(10,6))
plt.barh(skills, counts, color='steelblue')
plt.xlabel("Frequency")
plt.title("Top 15 In-Demand Skills Across Job Postings")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig("top_skills_chart.png")
plt.show()