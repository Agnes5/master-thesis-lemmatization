from sklearn.model_selection import train_test_split

input_data_filename = 'result_not_same.tsv'
input_data_filename2 = 'result_same.tsv'
# train 60%, valid 20%, test 20%


def main():
    X_phrases = []
    y_phrases = []

    def parse_text_from_file_to_lists(file_name, how_many=-1):
        lines_number = 0
        with open(file_name) as input_data:
            for line in input_data:
                X_phrases.append(line.split('\t')[0] + '.')
                y_phrases.append(line.split('\t')[1].replace('\n', '.'))
                lines_number += 1
                if how_many != -1 and lines_number > how_many:
                    return lines_number
            return lines_number

    lines_number = parse_text_from_file_to_lists(input_data_filename)
    tmp = parse_text_from_file_to_lists(input_data_filename2, int(0.2 * lines_number))
    print(lines_number, tmp)


    X_train, X_test_valid, y_train, y_test_valid = train_test_split(X_phrases, y_phrases, test_size=0.4)
    X_test, X_valid, y_test, y_valid = train_test_split(X_test_valid, y_test_valid, test_size=0.5)
    output_list = [X_train, y_train, X_test, y_test, X_valid, y_valid]
    print(len(X_train), len(y_train), len(X_test), len(y_test), len(X_valid), len(y_valid))
    output_files = ['train.after', 'train.before',
                    'test.after', 'test.before',
                    'valid.after', 'valid.before']
    for output_file, output in zip(output_files, output_list):
        with open(output_file, 'w') as file:
            file.write('\n'.join(output))


if __name__ == '__main__':
    main()
