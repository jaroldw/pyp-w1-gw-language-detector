# -*- coding: utf-8 -*-

"""This is the entry point of the program."""

def detect_language(text, languages):
    """Returns the detected language of given text."""

    results = {}        
    
    for lang in languages:
        word_count = 0
        
        for word in text.split(' '):
            if word in lang['common_words']:
                word_count += 1
                
        results[lang['name']] = word_count
    
    max_count = max(results.values())
    
    for lang, count in results.items():
        if count == max_count:
            return lang