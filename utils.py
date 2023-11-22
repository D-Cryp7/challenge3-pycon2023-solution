from collections import Counter
import string
import spacy

nlp = spacy.load("es_core_news_sm")

digits = string.digits
lowercase = string.ascii_letters[:26]
uppercase = string.ascii_letters[26:]
alphabet = ",." + digits + uppercase + lowercase + "ÁÉÍÑÓÚáéíñóú"

# https://stackoverflow.com/questions/11122291/how-to-find-char-in-string-and-get-all-the-indexes
def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

def decrypt_message(enc_message):
    dec_message = ""
    for char in enc_message:
        if char in alphabet:
            index = alphabet.index(char)
            dec_message += alphabet[(index + 1) % len(alphabet)]
        else:
            dec_message += char
    
    # https://stackoverflow.com/questions/71316888/how-to-sort-the-frequency-of-each-letter-in-a-descending-order-python
    ocurr = dict(Counter(dec_message))
    ocurr = sorted(ocurr, key = lambda x: ocurr[x], reverse = True)
    for char in ocurr[:5]:
        dec_message = dec_message.replace(char, "")
    
    for char in ocurr[5:7]:
        dec_message = dec_message.replace(char, " ")
        
    split = dec_message.split()
    dec_message = " ".join(split)
        
    return dec_message

def categorize_words(message):
    pass

def list_info(enc_message):
    pass
