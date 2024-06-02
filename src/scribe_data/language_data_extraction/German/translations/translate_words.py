"""
Translates the German words queried from Wikidata to all other Scribe languages.

Example
-------
    python3 src/scribe_data/wikidata/languages/German/translations/translate_words.py
"""

import json
import os
import sys

from scribe_data.translation.translation_utils import (
    translate_to_other_languages,
)

SRC_LANG = "German"
translate_script_dir = os.path.dirname(os.path.abspath(__file__))
words_to_translate_path = os.path.join(translate_script_dir, "words_to_translate.json")

with open(words_to_translate_path, "r", encoding="utf-8") as file:
    json_data = json.load(file)

word_list = [item["word"] for item in json_data]

translations = {}
translated_words_path = os.path.join(
    translate_script_dir,
    f"{os.path.dirname(sys.path[0]).split('scribe_data')[0]}/../language_data_export/{SRC_LANG}/translated_words.json",
)
if os.path.exists(translated_words_path):
    with open(translated_words_path, "r", encoding="utf-8") as file:
        translations = json.load(file)

translate_to_other_languages(
    source_language=SRC_LANG,
    word_list=word_list,
    translations=translations,
    batch_size=100,
)
