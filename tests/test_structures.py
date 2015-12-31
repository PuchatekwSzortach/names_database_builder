# -*- coding: utf-8 -*-

import names.structures


class TestJapanaseNamesValidator(object):

    def test_legal_name(self):

        validator = names.structures.JapaneseNamesValidator()
        name = names.structures.JapaneseName(kanji=u"強固", hiragana=u"きょうこ", gender=u"男")

        assert True == validator.is_name_valid(name)

    def test_illegal_hiragana(self):

        validator = names.structures.JapaneseNamesValidator()
        name = names.structures.JapaneseName(kanji=u"強固", hiragana=u"KYOKO", gender=u"女")

        assert False == validator.is_name_valid(name)

    def test_illegal_kanji(self):

        validator = names.structures.JapaneseNamesValidator()
        name = names.structures.JapaneseName(kanji=u"KYOKO", hiragana=u"きょうこ", gender=u"女")

        assert False == validator.is_name_valid(name)

    def test_set_two_same_names(self):

        first_name = names.structures.JapaneseName(kanji=u"協子", hiragana=u"きょうこ", gender=u"女")
        second_name = names.structures.JapaneseName(kanji=u"協子", hiragana=u"きょうこ", gender=u"女")

        names_set = {first_name, second_name}
        assert 1 == len(names_set)

        name_from_set = names_set.pop()
        assert name_from_set.kanji == u"協子"
        assert name_from_set.hiragana == u"きょうこ"
        assert name_from_set.gender == u"女"

    def test_different_names(self):

        first_name = names.structures.JapaneseName(kanji=u"枚見", hiragana=u"まいみ", gender=u"女")
        second_name = names.structures.JapaneseName(kanji=u"協子", hiragana=u"きょうこ", gender=u"女")

        names_set = {first_name, second_name}
        assert 2 == len(names_set)

    def test_names_ordering(self):

        first_name = names.structures.JapaneseName(kanji=u"愛見", hiragana=u"あいみ", gender=u"女")
        second_name = names.structures.JapaneseName(kanji=u"協子", hiragana=u"きょうこ", gender=u"女")

        names_list = [second_name, first_name]
        sorted_names = sorted(names_list)

        assert first_name is sorted_names[0]
        assert second_name is sorted_names[1]

    def test_names_ordering_same_hiragana(self):

        first_name = names.structures.JapaneseName(kanji=u"愛", hiragana=u"あいみ", gender=u"女")
        second_name = names.structures.JapaneseName(kanji=u"愛見", hiragana=u"あいみ", gender=u"女")

        names_list = [second_name, first_name]
        sorted_names = sorted(names_list)

        assert first_name is sorted_names[0]
        assert second_name is sorted_names[1]
