"""
Utilising a custom Countem class the find_most_repeated function finds the 
most repeated elements in a list and the number of times they repeat
"""

from typing import List, Dict
from . import Countem

def find_most_repeated(elems: List) -> Dict:
    """
    Return the most repeated elements in a list and the number of times they repeat
    
    Args:
        elems (List): A list of elements to search for repeats
    Returns:
        Dict: A dictionary containing the elements that repeat the most and 
        the number of times they repeat

        e.g.
        print(find_most_repeated(['a', 'b', 'b', 3, 'c', 3, 'c', 3, 'b']))
        {'elements': ['b', 3], 'repeats': 3}
    """
    counts = Countem(elems)
    maxcount = counts.max()

    if not maxcount or maxcount < 2:
        return { 'elements': [], 'repeats': None }

    return { 'elements': list(counts.multi_mode()), 'repeats': maxcount }
