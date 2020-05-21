"""
Given a dictionary of words, find words that are compound words
made from other words in the dictionary
"""

words = ['hi', 'hello', 'hihello', 'bye', 'america', 'plural', 'thigh', 'pluralamericathigh', 'byeamerica', 'youtube', 'byeamericayoutube', 'arm', 'helloarm']
answer = ['hihello', 'pluralamericathigh', 'byeamerica', 'byeamericayoutube', 'helloarm']

def check_prefix(word, candidate):
    if word[:len(candidate)] == candidate:
        return True, word[:len(candidate)]
    else:
        return False, None
