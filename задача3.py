import csv
with open('students_new.csv', encoding="utf8") as csvfile:
    reader = list(csv.DictReader(csvfile, delimiter=',', quotechar='"'))
data = sorted(reader, key=lambda x: int(x['titleProject_id']))

id_project = input()
while (id_project != 'СТОП'):
    id_project = int(id_project)
    L = 0
    R = len(data)
    while L < R - 1:
        M = (L + R) // 2
        if int(data[M]['titleProject_id']) > id_project:
            R = M
        else:
            L = M
    print(data[L]['titleProject_id'])
    if int(data[L]['titleProject_id']) == id_project:
        surname, name, patronymic = data[L]["Name"].split()
        print(f"Проект No{id_project} делал: {name[0]}. {surname} он(а) получил(а) оценку - {data[L]['score']}.")
    else:
        print('Ничего не найдено')
    id_project = input()