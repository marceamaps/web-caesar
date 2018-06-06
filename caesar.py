
def alphabet_position(letter):

    #this function takes a letter and returns the index within the alphabet
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    new_letter = alphabet.index(letter.lower())

    return new_letter

def rotate_character(char, rotation):

    #this function takes a char index and rotation amount 
    #and returns the new char index and the new letter 
    #from the appropriate alphabet (upper or lowercase)

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    started_as_upper = char.isupper() #True/False

    if not char.isalpha():
        return char

    position = alphabet_position(char) #this calls the alphabet_position function to find the char position
    position += rotation #this takes the position and adds the rotation amount
    if position > 26: 
        position = position % 26
    if started_as_upper:
        return ALPHABET[position]
    return alphabet[position]

def alphabet_pos_vig(letter):

    #this function takes a letter and returns the index within the alphabet
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    letter_ix = alphabet.index(letter.lower())

    return letter_ix

def rotate_char_vig(char, key_char):

    #this function takes a char index and key char index 
    #and returns the encrpyted char index and the new letter 
    #from the appropriate alphabet (upper or lowercase)

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    started_as_upper = char.isupper() #True/False

    if not char.isalpha():
        return char

    char_position = alphabet_pos_vig(char) #this calls the alphabet_position function to find the char position
    key_position = alphabet_pos_vig(key_char) #this calls the alphabet_position function to find the key char position

    new_position = char_position + key_position  #this takes the char position and the key_char position and returns the new position
    if new_position > 26: 
        new_position = new_position % 26
    if started_as_upper:
        return ALPHABET[new_position]
    return alphabet[new_position]

def encrypt(text, key):

    #this function takes a string of text and appends the new text into a string

    new_text = ''
    count = 0

    for char in text:
        
        if not char.isalpha():
            new_text += char
            if char == ' ':
                new_text += ' '
        else:
            new_text += rotate_char_vig(char, key[count])

            if count + 1 < len(key):
                count += 1
            else:
                count = 0
    return new_text


def main():

    user_message = str(input('Type your message!:'))

    user_rotation = str(input('Write your key:'))

    print(encrypt(user_message, user_rotation))


if __name__ == "__main__":
    main()