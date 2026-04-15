import pandas as pd
import numpy as np

np.random.seed(42)

n = 200

data = pd.DataFrame({
    'Age_Group': np.random.choice(['18-24','25-34','35-44'], n),
    'Gender': np.random.choice(['Male','Female'], n),
    'Preferred_Tool': np.random.choice(['Python','R','Excel'], n),
    'Satisfaction': np.random.randint(1,6,n),
    'Feedback': np.random.choice(['Good','Average','Excellent','Poor'], n)
})

data.to_csv("data/poll_data.csv", index=False)
print("Poll data created!")