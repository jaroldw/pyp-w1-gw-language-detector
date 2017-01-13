# -*- coding: utf-8 -*-

"""This is the entry point of the program."""

def detect_language(text, languages):
    """Returns the detected language of given text."""

    results = {}
    
    for lang in languages:
        results[lang['name']] = len([word for word in text.split()
                                    if word in lang['common_words']])
    
    return max(results, key=results.get)