# -*- coding: utf-8 -*-

import names.structures


class TestJapanaseNamesValidator(object):

    def test_legal_name(self):

        validator = names.structures.JapaneseNamesValidator()
        name = names.structures.JapaneseName(kanji=u"強固", hiragana=u"きょうこ", gender=u"男")

        assert True == validator.is_name_valid(name)

    def test_illegal_hiragana(self):

        validator = names.structures.JapaneseNamesValidator()
        name = names.structures.JapaneseName(kanji=u"強固", hiragana=u"KYOKO", gender=u"男")

        assert False == validator.is_name_valid(name)

    def test_illegal_kanji(self):

        validator = names.structures.JapaneseNamesValidator()
        name = names.structures.JapaneseName(kanji=u"きょう子", hiragana=u"きょうこ", gender=u"男")

        assert False == validator.is_name_valid(name)
