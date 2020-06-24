from regex import regex
from tqdm import tqdm


def main():
    filename = 'links.tsv'
    links_file_size = count_lines(filename)
    print("All of lines with links: ", links_file_size)
    phrase = 0

    with open(filename) as links_file, \
            open('result_same.tsv', 'w') as results_same_file, \
            open('result_not_same.tsv', 'w') as results_not_same_file, \
            open('result_not_same2.tsv', 'w') as results_not_same_file2:

        for line in tqdm(links_file, total=links_file_size):
            line = line.replace('\n', '')

            lemmatized_phrase = line.split('\t')[3]
            form_phrase = line.split('\t')[4]

            if not any(char.isdigit() for char in form_phrase):
                if lemmatized_phrase == form_phrase:
                    results_same_file.write(f'{lemmatized_phrase}\t{form_phrase}\n')

                elif len(lemmatized_phrase.split()) == len(form_phrase.split()):
                    lemmatized_letters = [word[:2].lower() for word in lemmatized_phrase.split()]
                    form_phrase_letters = [word[:2].lower() for word in form_phrase.split()]
                    if lemmatized_letters == form_phrase_letters and not regex.match(r'\p{Lu}\. \p{Lu}', form_phrase):
                        phrase += 1
                        results_not_same_file.write(f'{lemmatized_phrase}\t{form_phrase}\n')
                    else:
                        results_not_same_file2.write(f'{lemmatized_phrase}\t{form_phrase}\n')
# sorted(re.sub(r'\s+', ' ', re.sub(r'[^\w ]', ' ', "'Ala ma kota, i 2 psów'").strip()).lower().split(' '))

    print(phrase)


def count_lines(file_name):
    with open(file_name) as f:
        return sum(1 for line in f)


if __name__ == '__main__':
    main()
