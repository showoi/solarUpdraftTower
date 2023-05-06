import json

# Load the existing translations from the file
with open('languages.json', 'r') as f:
    translations = json.load(f)

# Prompt the user to add translations until they choose to stop
while True:
    # Prompt the user for the English sentence to translate
    en_sentence = input('Enter the English sentence to translate (or enter "q" to quit): ')
    if en_sentence == 'q':
        break

    # Prompt the user for the Turkish translation of the sentence
    tr_translation = input('Enter the Turkish translation of the sentence: ')

    # Add the new translation to the dictionary
    translations['en'][en_sentence] = tr_translation

    print('Translation added successfully.')

# Save the updated translations to the file
with open('languages.json', 'w') as f:
    json.dump(translations, f)
