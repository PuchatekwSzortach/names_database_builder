# -*- coding: utf-8 -*-

import functools
import icu
import re


@functools.total_ordering
class JapaneseName(object):
    """
    An extremely simple class for storing hiragana, kanji and gender of a name
    """

    def __init__(self, hiragana, kanji, gender):

        self.hiragana = hiragana
        self.kanji = kanji
        self.gender = gender

        self.combined_fields = ", ".join([self.hiragana, self.kanji, self.gender])

        # For deciding which names is "greater" than the other
        locale = icu.Locale("ja", "JP")
        self.japanese_collator = icu.Collator.createInstance(locale)

    def __repr__(self):
        return self.combined_fields.encode('utf-8')

    def __hash__(self):

        return self.combined_fields.__hash__()

    def __eq__(self, other):

        # If kanji is different, names are different. Else continue comparison
        if self.kanji != other.kanji:
            return False

        # If hiragana is different, names are different. Else continue comparison
        if self.hiragana != other.hiragana:
            return False

        # Kanji and hiragana are the same, so judge on gender
        return self.gender == other.gender

    def __lt__(self, other):

        # First order on hiragana
        if self.hiragana != other.hiragana:
            return self.japanese_collator.greater(other.hiragana, self.hiragana)

        # Then order on kanji
        if self.kanji != other.kanji:
            return self.japanese_collator.greater(other.kanji, self.kanji)

        # Finally, if everything else is the same, order on gender
        return self.japanese_collator.greater(other.gender, self.gender)


class JapaneseNamesValidator(object):

    def __init__(self):
        pass

        self.hiragana_regex = re.compile(u"^[あ-ん]+$", re.U)
        self.kanji_regex = re.compile(u"^[一-龠々]+$", re.U)
        self.gender_regex = re.compile(u"^[男女]$", re.U)

    def is_name_valid(self, japanese_name):

        is_hiragana_legal = self.hiragana_regex.search(japanese_name.hiragana) is not None
        is_kanji_legal = self.kanji_regex.search(japanese_name.kanji) is not None
        is_gender_legal = self.gender_regex.search(japanese_name.gender) is not None

        return is_hiragana_legal and is_kanji_legal and is_gender_legal
