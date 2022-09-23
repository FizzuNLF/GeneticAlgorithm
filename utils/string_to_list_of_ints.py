def string_to_list_of_ints(string_):
    list_ = []
    list_[:0] = string_
    return list(map(int, list_))