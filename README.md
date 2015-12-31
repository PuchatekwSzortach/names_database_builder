# names_database_builder

[![Build Status](https://travis-ci.org/PuchatekwSzortach/names_database_builder.png?branch=master)](https://travis-ci.org/PuchatekwSzortach/names_database_builder)
[![Coverage Status](https://codecov.io/github/PuchatekwSzortach/names_database_builder/coverage.png?branch=master)](https://codecov.io/github/PuchatekwSzortach/names_database_builder)

Japanese names database builder

This code builds an sqlite3 database of Japanese names for my Android app Akachanmei.
Input comes from file raw_names.txt.
While raw_names.txt file included with this source has only a few positions, the original I use for real development contains nearly 200,000 names.
Some of these are duplicates, some are illegal names (e.g. contain romaji).Most importantly names are listed in no particular order.

This code removes duplicates and illegal names, and then sorts the result by hiragana, kanji and gender, before building an sqlite3 database file.
All in all it's a rather simple project. The nifty part is its use of `functools.total_ordering`, `__hash__` and `__eq__` functions to enable efficient sets and sort computations for my custom `JapaneseName` class.
