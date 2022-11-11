### synonyms task
given  
```python

def solution(dictionary, test):
    pass

pairs_of_words = [
    ["big", "large"],
    ["large", "huge"],
    ["great", "huge"],
    ["small", "little"],
    ["apple", "banana"],
]

test_words = [
    ["same", "same"],
    ["big", "huge"],
    ["huge", "big"],
    ["apple", "peach"],
    ["big", "tall"],
    ["peach", "PEACH"],
]

result = solution(pairs_of_words, test_words)
expected_result = [True, True, True, False, False, True]
assert result, expected_result

```
