import json, os
import pandas as pd

file_path = os.path.join("E:/Necleotide Codes/archive", "yelp_academic_dataset_checkin.json")
data_file = open(file_path)
data = []
for line in data_file:
    data.append(json.loads(line))
checkin_df = pd.DataFrame(data)
print(checkin_df)
data_file.close()

args = Namespace(
    raw_train_dataset =

)
item.items*()