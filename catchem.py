import pandas as pd
from nltk.tag import pos_tag
from fuzzywuzzy import fuzz


def extract_NNPs(text):
    tagged = pos_tag(text.split())
    NNPs = [word for word, pos in tagged if pos == 'NNP']

    return NNPs

def get_matches(list1, list2):
    return [x for x in list1 if x in list2]


def get_fuzzy_match(list1, list2, treshold):

    matches = []

    for i1 in list1:
        for i2 in list2:
            ratio = fuzz.token_set_ratio(i1, i2)
            if ratio >= treshold:
                matches.append([i1, ratio])

    return matches


def write_list_to_file(filename, list):
    f = open(filename, "w")

    for item in list:
        f.write("{}\n".format(item))



if __name__ == "__main__":
    # Broken, fix read_csv arguments (http://stackoverflow.com/questions/24251219/pandas-read-csv-low-memory-and-dtype-options)
    # Also, download the panamapapers: https://offshoreleaks.icij.org/pages/database
    # Download "archive of all files" (.csv files)

    panama_df = pd.read_csv('panamapapers/Entities.csv')
    organizations = panama_df.name


    # fiscel-2016.csv downoaded from http://open.canada.ca/data/en/dataset/53753f06-8b28-42d7-89f7-04cd014323b0
    canada_df = pd.read_csv('fiscal-2016.csv')
    contractors = canada_df['supplier-standardized-name']

    matches = get_fuzzy_match(contractors, organizations, 0)



    # test1 = ["Lorem ipsum", "Lörem aspum", "IPSUM LOREM", "lo rem ip sum", "Iprem losum"];
    # test2 = ["Lorem ipsum"]
    #
    #
    # matches = get_fuzzy_match(test1, test2, 75)

    write_list_to_file("matches.txt", matches)
