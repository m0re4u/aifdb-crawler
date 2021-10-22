from aifdb_crawler import get_stats, read_dataset, read_arg_file

if __name__ == "__main__":
    map7 = read_arg_file('data/araucaria/map8.json')

    print("== Araucaria == ")
    araucaria = read_dataset('data/araucaria/*.json')
    labels_araucaria = get_stats(araucaria)

    print("== US2016 == ")
    US2016 = read_dataset('data/US2016G1tvWALTON/*.json')
    label_US2016 = get_stats(US2016)

    both = label_US2016.intersection(labels_araucaria)
    print(f"{len(both)} labels overlap")