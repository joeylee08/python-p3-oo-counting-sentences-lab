#!/usr/bin/env python3

class MyString:
    def __init__(self, value=''):
        self.value = value
    
    def get_value(self):
        return self._value
    
    def set_value(self, value):
        if type(value) != str:
            print("The value must be a string.")
        else:
            self._value = value

    value = property(get_value, set_value)
    
    def is_sentence(self):
        return True if self._value[-1] == "." else False

    def is_question(self):
        return True if self._value[-1] == "?" else False

    def is_exclamation(self):
        return True if self._value[-1] == "!" else False

    def count_sentences(self):
        split = self._value.replace(".", "&")
        split = split.replace("!", "&")
        split = split.replace("?", "&")
        split = split.split("&")
        sentences = [substring for substring in split if substring != ""]
        return len(sentences)

# python lib/count_sentences.py