# Deps: python3.9, tqdm(pip), aria2c

mkdir -p data
aria2c -i json.list -d data
python dump.py

echo "Total lines of data"
wc -l "VA-2020-precincts.csv"
