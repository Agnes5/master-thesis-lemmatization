def main():
    with open('output.out') as file:
        form_words = []
        lemmitized_words = []
        result_words = []

        for line in file.readlines():
            if line.startswith('S-'):
                form_words.append(' '.join(line.split()[1:-1]))
            elif line.startswith('T-'):
                lemmitized_words.append(' '.join(line.split()[1:-1]))
            elif line.startswith('H-'):
                result_words.append(' '.join(line.split()[2:-1]))

        goods = 0
        bads = 0
        almost_bads = 0

        for form, lemmitized, result in zip(form_words, lemmitized_words, result_words):
            if lemmitized == result:
                goods += 1
            elif lemmitized.lower() == result.lower():
                almost_bads += 1
                print(form, ' ', lemmitized, ' ', result)
            else:
                bads += 1
                print(form, ' ', lemmitized, ' ', result)
        print('Poprawnie bez uwzgledniania wielkości liter: ', goods + almost_bads, '/', goods + bads + almost_bads)
        print('Poprawnie: ', goods, '/', goods + bads + almost_bads)


if __name__ == '__main__':
    main()
