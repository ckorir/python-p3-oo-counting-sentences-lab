#!/usr/bin/env python3

class MyString:
  pass
  def __init__(self, value=""):
    self._value = value

  @property
  def get_value(self):
    return self._value

  def set_value(self, new_value):
    if isinstance(new_value, str):
      self._value = new_value
    else:
      print("The value must be a string.")

  def is_sentence(self):
    return self._value.endswith(".")

  def is_question(self):
    return self._value.endswith("?")

  def is_exclamation(self):
    return self._value.endswith("!")

  def count_sentences(self):
    odered_sentence = self._value.replace('!', '.').replace('?', '.')
    # Split the text into sentences based on the '.' character
    sentences = [s for s in odered_sentence.split('.') if s]
    return len(sentences)
  
  value = property(get_value, set_value)
  