import json
import urllib.request
import requests
import re
from pathlib import Path

ARAUCARIA_URL = "http://corpora.aifdb.org/araucaria"
JSON_URL_TEMPLATE = "http://www.aifdb.org/json/{}"


def collect_araucaria(outdir: Path):
    """Collect individual json files from AIFdb."""
    fp = urllib.request.urlopen(ARAUCARIA_URL)
    mybytes = fp.read()

    doc = mybytes.decode("utf8")
    fp.close()
    finds = re.findall(r'nsIDs = .*]', doc)
    assert len(finds) == 1
    map_ids = [int(x) for x in finds[0].strip('nsIDS = [').strip(']').split(',')]

    outdir.mkdir(parents=True, exist_ok=True)

    for i, map_id in enumerate(map_ids):
        print(f"{i}/{len(map_ids)}")
        map_url = JSON_URL_TEMPLATE.format(map_id)
        r = requests.get(map_url)
        out_file = outdir / f'map{map_id}.json'
        with open(out_file, 'w') as f:
            json.dump(r.json(), f)