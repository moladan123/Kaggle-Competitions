import pandas as pd

ROOT = "/Volumes/Unititled/Jan-Apr-2019/Random/KaggleCompetitions/titanicData/titanic/"

sample_prediction = pd.read_csv(ROOT + "gender_submission.csv")

test = pd.read_csv(ROOT + "test.csv")
train = pd.read_csv(ROOT + "train.csv")

print(train)
train = train.loc['Survived']
print(train)


inputs = []
for i in range(test.shape[0]):
    new_person = train.iloc[i, :]


    inputs.append(new_person)
print(inputs)

