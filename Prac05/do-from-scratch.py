def main():
    sentence = "this is a collection of words of nice words this is a fun thing it is"

    WORD_DICT = {}

    split_sentence = sentence.split()

    for word in split_sentence:
        if word in WORD_DICT:
            WORD_DICT[word] += 1
        else:
            WORD_DICT[word] = 1

    print("Text:", sentence)

    longest_word_len = int(max(len(word) for word in WORD_DICT))

    sorted_list = sorted(WORD_DICT.items())

    for word, count in sorted_list:
        print("{:{}} : {}".format(word, longest_word_len, count))

main()