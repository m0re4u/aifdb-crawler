import json
import glob
from typing import List
from pathlib import Path
import numpy as np
import spacy

nlp = spacy.load("en_core_web_sm")


def read_dataset(data_path: Path):
    """Read a dataset of argument maps in AIF format (json style)."""
    maps = []
    for data_file in glob.glob(data_path):
        map_data = read_arg_file(data_file)
        maps.append(map_data)
    return maps

def read_arg_file(filename: Path):
    with open(filename, 'r') as f:
        data = json.load(f)
    return data

def get_stats(dataset: List):
    print(f"Number of maps: {len(dataset)}")
    stats = {'char_lengths': [], 'token_lengths': []}
    scheme_types = []
    schemes = 0
    maps_with_scheme = 0
    for map in dataset:
        found = False
        for node in map['nodes']:
            if 'scheme' in node:
                schemes += 1
                found = True
                scheme_types.append(node['scheme'])
            if node['type'] == "I":
                lt = len(node['text'])
                doc = nlp(node['text'])
                stats['char_lengths'].append(lt)
                stats['token_lengths'].append(len(doc))
        if found:
            maps_with_scheme += 1


    print(f"Number of nodes with scheme annotation: {schemes}")
    print(f"Number of maps with >0 scheme annotations: {maps_with_scheme}")
    print(f"Number of characters: {np.sum(stats['char_lengths'])}")
    print(f"Number of words: {np.sum(stats['token_lengths'])}")
    print(f"Number of unique scheme labels: {len(set(scheme_types))}")
    return set(scheme_types)

