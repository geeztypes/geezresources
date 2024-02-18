import json
import io


sentence = r'ተጻብኦታት ኬጋጥመና ኸሎ፡ ኣብ የሆዋን ኣብ ውድቡን ዘሎና ተኣማንነት ኪፍተን ይኽእል እዩ።'

f = open('geez_syllables.json', mode="r", encoding="utf-8")
 
""" 
    "syllable": "ሀ",
    "syllable_decimal": 4608,
    "syllable_hex": "1200",
    "syllable_phonetic": "ETHIOPIC SYLLABLE HA", 
"""
# returns JSON object as 
# a dictionary
data = json.load(f)

sentence_phonetic = ''

for letter in sentence:
    # Iterating through the json
    # list
    for i in data['geez']:
        if i['syllable'] == letter:
            sentence_phonetic += i['syllable_phonetic']
        elif letter.isspace():
            sentence_phonetic += letter



print(sentence_phonetic)

# Closing file
f.close()