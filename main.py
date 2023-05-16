import re
import csv

with open('phonebook_raw.csv', encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

    for i, row in enumerate(contacts_list):
        fio = ' '.join(row[0:3]).split()
        fio.append('') if len(fio) < 3 else 0
        for k in range(3):
            contacts_list[i][k] = fio[k]

    dic = {}
    for st in contacts_list:
        keys = ' '.join(st[0:2])
        values = st[2::]
        if dic.get(keys, False) is False:
            dic[keys] = values
        else:
            for va in range(5):
                # pprint(dic[keys][va])
                if dic[keys][va] == '':
                    dic[keys][va] = values[va]

    pattern = r"(8|\+7)?\s*[\(]?(\d{3})[\)-]?\s*(\d{3})[-\s]*(\d{2})[-\s]*(\d{2})\s*[\(]?(\w+\.)?\s*(\d+)?[\)]?"
    subst = r"+7(\2)\3-\4-\5 \6\7"
    data_dict = []
    for k, v in dic.items():
        x = k.split(' ', 2)
        data_dict.append({'lastname': x[0],
                          'first_name': x[1],
                          'surname': v[0],
                          'organization': v[1],
                          'position': v[2],
                          'phone': re.sub(pattern, subst, v[3]),
                          'email': v[4],
                          })

    if __name__ == '__main__':
        with open("phonebook1.csv", "w", encoding='utf-8', newline='') as f:
            datawriter = csv.writer(f, delimiter=';')
            for item in data_dict:
                datawriter.writerow(
                    [item['lastname'], item['first_name'], item['surname'], item['organization'], item['position'],
                     item['phone'], item['email']])