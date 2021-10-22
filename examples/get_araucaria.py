from aifdb_crawler import collect_araucaria
from pathlib import Path

DATA_FOLDER = 'data/'

def main():
    outpath = Path(f'{DATA_FOLDER}/araucaria')
    collect_araucaria(outpath)

if __name__ == '__main__':
    main()