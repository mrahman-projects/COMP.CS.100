"""
This program formats text in a fully justified typesetting

Project No.Name: 6.14_Fully Justified Text
Name: Mijanur Rahman (mijanur.m.rahman@tuni.fi)
Student ID: 151762776
"""


def input_text():
    """
    This function takes input from a user, and returns when an empty
    row is given as input
    :return: 'list', user given input in a list form
    """
    print("Enter text rows. Quit by entering an empty row.")
    total_input = []
    while True:
        user_input = input()
        if user_input != "":
            total_input += user_input.split()
        else:
            break
    return total_input


def add_space_char(word):
    """
    This function appends additional space with a word
    :param word: 'given' word
    :return:
    """
    return word + " "


def justify_text(text_list, length_of_line):
    """
    This function justifies a given text at a given length
    :param length_of_line: `int`, the given length of justified line
    :param text_list: `list`, the given text as a list
    :return: `str`, the justified text
    """
    justified_text = ''
    words_in_a_line = []
    chars_count_in_a_line = 0
    total_words_justified = 0
    last_line_flag = False
    # print(text_list)    # remove

    for word_from_text in range(len(text_list)):
        # print("*" * 80)     #  remove
        # print(f"Iteration number: {word_from_text}, the word is: {text_list[word_from_text]}")     #: remove
        # print(f"Total number of words in the list {len(text_list)}")    # : remove
        # print(f"Out of that already justified: {total_words_justified}, left: {len(text_list) - total_words_justified}")    # : remove

        # Last line check
        chars_remain_from_text = 0
        # print("Last Line Check")    #: remove
        # print("     Last line check loop range: ", word_from_text, '-', len(text_list))     # : to remove later
        for word_pointer in range(word_from_text, len(text_list)):
            chars_remain_from_text += len(text_list[word_pointer]) + 1  # length of a space character is 1
            # print(f"    Iterate number {word_pointer}, Adding length of {text_list[word_pointer]}, char remain from text: {chars_remain_from_text}")
        chars_remain_from_text = chars_remain_from_text - 1     # removing the last space of the last word
        # print("     Char left from the current word: ", chars_remain_from_text)   # : to remove later

        # if last line has identified, append the last line with adding default spaces

        if chars_remain_from_text <= length_of_line and last_line_flag is True:
            # print("     On The Last Line!")     # : to remove later
            if word_from_text != len(text_list)-1:
                words_in_a_line.append(text_list[word_from_text] + " ")
            else:
                words_in_a_line.append(text_list[word_from_text])
                # print("     Added last words of the body, the words now:")    # : to remove later
                # print(words_in_a_line)  # : to remove later
                for join_word in words_in_a_line:
                    justified_text += "".join(join_word)

        else:   # if not the words of the last line
            # print("     Not in the last line yet!")     # : remove
            count_total = len(text_list[word_from_text]) + chars_count_in_a_line + len(words_in_a_line)
            # print(f"Length of new word '{text_list[word_from_text]}' and existing words in the list is: {count_total}")     # : to remove later
            if count_total <= length_of_line:
                words_in_a_line.append(text_list[word_from_text])
                # print(f"Adding word in the temp list: {text_list[word_from_text]} ")  # : to remove later
                # print(f"Total temp list now: {words_in_a_line}")    # : to remove later
                chars_count_in_a_line += len(text_list[word_from_text])
                last_line_flag = False
                # print(f"Length of all chars in the temp list now {count_total}")   # : to remove later
                if chars_count_in_a_line + len(text_list[word_from_text+1]) + len(words_in_a_line) > length_of_line:
                    # print(f"Total chars have exceeded the length of lines ({length_of_line}).")     # : remove
                    spaces_to_add = length_of_line - chars_count_in_a_line - (len(words_in_a_line) - 1)
                    spaces_left = spaces_to_add
                    # print(f"Additional {spaces_to_add} spaces needs to be added apart from the default spaces")     # : remove
                    count = 0
                    while spaces_left != 0:
                        if len(words_in_a_line) != 1:   # if not a single word line
                            if count <= len(words_in_a_line)-2:
                                words_in_a_line[count] = add_space_char(words_in_a_line[count])
                                count += 1
                                spaces_left -= 1
                            else:
                                count = 0
                        else:   # it's a single word line
                            # print("Its a one word line!")   #: remove
                            words_in_a_line[0] = add_space_char(words_in_a_line[0])
                            spaces_left -= 1
                    # print(f"Words in a line WITHOUT default spaces: {words_in_a_line} ")    #: remove

                    for j in range(len(words_in_a_line)-1):
                        words_in_a_line[j] = add_space_char(words_in_a_line[j])
                    # print(f"Words in a line WITH default spaces: {words_in_a_line}")        # : remove

                    for join_word in words_in_a_line:
                        justified_text += "".join(join_word)
                    justified_text += "\n"
                    # print(f"Justified text till now: {justified_text}")     # : remove

                    total_words_justified += len(words_in_a_line)
                    words_in_a_line.clear()
                    chars_count_in_a_line = 0
                    last_line_flag = True
                # words_in_a_line.append(word)
                # chars_count_in_a_line = len(word)

    return justified_text


def main():

    given_texts = input_text()
    # print(given_texts)
    justified_length = int(input("Enter the number of characters per line: "))
    print(justify_text(given_texts, justified_length))


if __name__ == "__main__":
    main()
