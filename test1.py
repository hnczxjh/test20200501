import os
import pandas as pd
import numpy as np

data_file_name = os.path.join(os.path.expanduser('~'), 'PycharmProjects\\test2005\\Data\\Adult')
adult = pd.read_csv(data_file_name, names=names = ["Age", "Work-Class", "fnlwgt",
                                                   "Education", "Education-Num",
                                                   "Marital-Status", "Occupation",
                                                   "Relationship", "Race", "Sex",
                                                   "Capital-gain", "Capital-loss",
                                                   "Hours-per-week", "Native-Country",
                                                   "Earnings-Raw"])

