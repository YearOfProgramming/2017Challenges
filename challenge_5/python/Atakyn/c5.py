# find the added letter

from collections import Counter


def find_difference(s, t):
    """
    :param s: the shorter string
    :param t: the longer string (has the extra characters in it)
    :return: the extra character
    """
    s_chars = Counter(s)
    t_chars = Counter(t)

    for c in t_chars:  # t_chars will have more values than s_chars
        if s_chars[c] < t_chars[c]:
            return c

print(find_difference('asdfrtyjedsdabnetyujdfgsbaertrjsgfaeryejyrok', 'asdfrtyjedsdabnetyujpdfgsbaertrjsgfaeryejyrok'))
