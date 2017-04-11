from __future__ import print_function
from fuzzywuzzy import fuzz
from nltk.metrics import *

import time


def get_matches(list1, list2):
    return [x for x in list1 if x in list2]


def get_fuzzy_match(list1, list2, treshold):

    matches = []

    for i1 in list1:
        for i2 in list2:
            ratio = fuzz.ratio(i1, i2)
            #ratio = fuzz.partial_ratio(i1, i2)
            #ratio = fuzz.token_sort_ratio(i1, i2)
            #ratio = fuzz.token_set_ratio(i1, i2)
            #ratio = edit_distance(i1, i2)
            if ratio >= treshold:
                matches.append([i1, i2, ratio])

    return matches


def write_list_to_file(filename, list):
    f = open(filename, "w")

    for item in list:
        f.write("{}\n".format(item))



if __name__ == "__main__":
    
    # officers.txt, downloaded and formatted from Officers.csv @
    organizations = list(open("panama/entities.txt", "r", encoding="utf-8"))


    # canada_suppliers.txt, downloaded and formatted from: fiscel-2016.csv @ http://open.canada.ca/data/en/dataset/53753f06-8b28-42d7-89f7-04cd014323b0
    contractors = list(open("canada/canada_suppliers.txt", "r", encoding="utf-8"))

    # Start timer for timing the matching function
    time0 = time.time()

    # Matchem and catchem. Remove "[:100]'s" to use full lists.
    matches = get_fuzzy_match(contractors[:100], organizations[:100], 0)

    # Stop timer for timing the matching function
    time1 = time.time()

    # test1 = ["Lorem ipsum", "Lörem aspum", "IPSUM LOREM", "lo rem ip sum", "Iprem losum"];
    # test2 = ["Lorem ipsum"]
    #
    #
    # matches = get_fuzzy_match(test1, test2, 75)

    write_list_to_file("matches.txt", matches)

    print(time1 - time0)
