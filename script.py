### Для работы скрипта необходимо, чтобы в папке со скриптом находилась необходимая база данных

import pandas as pd
#даем имена колоннам для лучшего ориентирования
col_names = ["id","price","data","postcode","property_type","old/new","duration","paon","saon","street","lokality","town/city","district","country","ppd","status"]
#читаем csv файл
csv_file = pd.read_csv('pp-complete.csv', names=col_names)
#удаляем ненужные столбцы
csv_file.pop('id')
csv_file.pop('price')
csv_file.pop('duration')
csv_file.pop('property_type')
csv_file.pop('ppd')
csv_file.pop('status')
csv_file.pop('data')
csv_file.pop('postcode')
csv_file.pop('old/new')
#считаем повторяющиеся адреса
counter = csv_file.value_counts(subset=["country","town/city","district","lokality","street","paon","saon"],dropna=False)
#считаем количество полученных строк
i = 0
for row in counter:
    if row > 1:
        i += 1
#записываем Serial в CSV
grp = counter.head(i)
grp.to_csv('pp-group.csv')