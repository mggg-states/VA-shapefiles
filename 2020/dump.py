import glob
import json
import copy
import tqdm
import pandas as pd

"""
Dumps fetched json data to a csv file
"""

data = []
json_files = glob.glob("data/*.json")

for each_file in tqdm.tqdm(json_files):
    with open(each_file) as f:
        json_data = json.load(f)

        if "ElectionName" not in json_data or "Precincts" not in json_data:
            continue

        json_data["LocalityName"] = json_data["Locality"]["LocalityName"]
        json_data["LocalityCode"] = json_data["Locality"]["LocalityCode"]
        del json_data["Locality"]

        try:
            precincts = json_data["Precincts"]
            del json_data["Precincts"]
        except KeyError:
            print(json_data)

        # Sanity check, should be flat
        for k, v in json_data.items():
            assert not isinstance(v, list)
            assert not isinstance(v, dict)

        for each_precinct in precincts:
            for each_candidate in each_precinct["Candidates"]:
                row = copy.deepcopy(json_data)
                row["PrecinctName"] = each_precinct["PrecinctName"]
                data.append(row | each_candidate)

df = pd.DataFrame.from_records(data)
df.to_csv("VA-2020-precincts.csv")
