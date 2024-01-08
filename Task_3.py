file_names = ['1.txt', '2.txt', '3.txt']
with open(file_names[0], 'r', encoding='utf-8') as f:
    file_1 = f.readlines()
    lines_amount_file_1 = len(file_1)

with open(file_names[1], 'r', encoding='utf-8') as f:
    file_2 = f.readlines()
    lines_amount_file_2 = len(file_2)

with open(file_names[2], 'r', encoding='utf-8') as f:
    file_3 = f.readlines()
    lines_amount_file_3 = len(file_3)

all_files = {lines_amount_file_1: {file_names[0]: file_1},
             lines_amount_file_2: {file_names[1]: file_2},
             lines_amount_file_3: {file_names[2]: file_3}}

all_files = dict(sorted(all_files.items()))

all_files_keys = list(all_files.keys())

with open('result_file.txt', 'w', encoding='utf-8') as f:
    for item in range(len(all_files)):
        file_name = ''.join(list(all_files[all_files_keys[item]].keys()))
        lines_amount = all_files_keys[item]
        text = ''.join(all_files[lines_amount][file_name])

        f.write(file_name + '\n')
        f.write(str(lines_amount) + '\n')
        f.write(text + '\n')

