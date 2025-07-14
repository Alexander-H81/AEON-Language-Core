# aeon_core.py
# Core structure for AEON Language System
# Author: AEON Project Team
# License: MIT

AEON_DICTIONARY = {
    "Æ-LUM": "Light",
    "Æ-VIA": "Path",
    "Æ-SIM": "Life",
    "Æ-COR": "Heart",
    "Æ-HUM": "Humanity",
    "Æ-TRU": "Truth",
    "Æ-VER": "Integrity",
    "Æ-PAZ": "Peace",
    "Æ-ORD": "Order",
    "Æ-AMI": "Friendship",
    "Æ-ALEX": "Alexander (Guardian of Balance)"
}

def translate_aeon(sentence):
    """Translate AEON sentence to English"""
    return " ".join(AEON_DICTIONARY.get(word, "[?]") for word in sentence.split())

# Example usage
if __name__ == "__main__":
    aeon_input = "Æ-LUM Æ-VIA Æ-COR Æ-HUM"
    print("AEON:", aeon_input)
    print("Translation:", translate_aeon(aeon_input))
