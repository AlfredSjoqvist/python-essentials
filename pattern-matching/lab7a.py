from match import match
from books import db


def search(seq, database):
    """
    Returns all the sequences in given database
    which match the given pattern(seq).
    """

    matches = []

    for element in database:
        if match(element, seq):
            matches.append(element)
    return matches


test_sequences = [[['forfattare', ['&', 'zelle']], ['titel', ['--', 'python', '--']], ['ar', '&']],
                  ["--", ['titel', ["&", "&"]], "--"],
                  [['titel', ["&", "&"]], "--"],
                  ["&", ['titel', ["&", "&"]], "&"],
                  [["forfattare", ["--"]], ['titel', ["&", "&"]], ["ar", "&"]],
                  ["&", ['titel', ["&", "&"]], ["ar", "&"], "--"],
                  ["&", ['titel', ["&", "&"]], ["ar", "&"], "&"],
                  []]


for seq in test_sequences:

    match_list = search(seq, db)

    print(f"Matches for {seq}:")

    for match_element in match_list:

        print(match_element)

    print("")
