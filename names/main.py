# -*- coding: utf-8 -*-

import logging
import sys

import sqlalchemy.orm
import database
import structures


def get_names_from_file(path):

    with open(path) as file:
        data_lines = file.read().decode('utf-8').splitlines()

    names = []

    for name_line in data_lines:

        fields = name_line.split(",")
        japanese_name = structures.JapaneseName(
             kanji=fields[0], hiragana=fields[1], gender=fields[2])

        names.append(japanese_name)

    return names


if __name__ == "__main__":

    logger = logging.getLogger('names')
    logger.setLevel(logging.INFO)
    logger.addHandler(logging.StreamHandler(sys.stdout))

    logger.info('Reading raw data')
    names = get_names_from_file("./raw_names.txt")

    logger.info('Filtering out duplicates')
    unique_names = set(names)

    logger.info('Filtering out invalid names')
    validator = structures.JapaneseNamesValidator()
    valid_names = [name for name in unique_names if validator.is_name_valid(name)]

    logger.info('Sorting names')
    sorted_names = sorted(list(valid_names))

    logger.info('Populating database')

    Session = sqlalchemy.orm.sessionmaker(bind=database.engine)
    session = Session()

    # Define genders
    boy = database.Gender(gender=u'男')
    girl = database.Gender(gender=u'女')

    session.add_all([boy, girl])
    session.commit()

    name_entries = [database.Name(name) for name in sorted_names]
    session.add_all(name_entries)
    session.commit()
