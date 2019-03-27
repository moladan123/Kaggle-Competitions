import pandas as pd

ROOT = "/Volumes/Unititled/Jan-Apr-2019/Random/KaggleCompetitions/titanicData/titanic/"

info = pd.read_csv(ROOT + "gender_submission.csv")
test = pd.read_csv(ROOT + "test.csv")
train = pd.read_csv(ROOT + "train.csv")

