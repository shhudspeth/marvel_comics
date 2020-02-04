# model_build.py

import pandas as pd
import pickle
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier


# Load Cleaned dataset
df = pd.read_csv('..Notebooks/blue_eyes_data.csv')
target_variable = df['blue_eyes']
df.drop(columns=['blue_eyes'], inplace=True)

feat_X_train, X_test, feat_y_train,y_test = train_test_split(df, \
                                            target_variable, \
                                            test_size=0.33, random_state=42)

feat_y_train = feat_y_train.astype(int)
model = RandomForestClassifier(n_estimators=100, max_depth=3, random_state=0)
model.fit(feat_X_train, feat_y_train)


filename = 'final_model'
pickle.dump(model, open(filename, 'wb'))
