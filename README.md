# names_database_builder
Japanese names database builder

This code builds a sqlite3 database of Japanese names for my Android app Akachanmei.
Input comes from file raw_names.txt.
While raw_names.txt file included with this source has only a few positions, the original I use for real development contains nearly 200,000 names.
Some of these are duplicates, some are illegal names (e.g. contain romaji), and most importantly names are listed in no particular order.

This code removes duplicates and illegal names, and then sorts the result, before building sqlite3 database file.
The most interesting part is use of `functools.total_ordering`, `__hash__` and `__eq__` functions to enable efficient sets and sort computations.