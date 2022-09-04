import re
from pprint import pprint
import csv

with open("phonebook_raw.csv") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

# помещаем Ф И О на свои места:
for contact in contacts_list:
    lastname_firstname_surname = []
    # если обнаружила, что ФИО не наместе, то делю найденное по пробелам и записываю
    # в созданный чуть выше список
    if len(contact[0].split()) > 1 or len(contact[1].split()) > 1:
      for i in range(0, 2):
        for word in contact[i].split():
          lastname_firstname_surname.append(word)
      for i in range(0, len(lastname_firstname_surname)):
        contact[i] = lastname_firstname_surname[i]

# объединяем дублирующиеся записи:
for n in range(1, len(contacts_list)):
  for_del = []
  for i in range(n + 1, len(contacts_list)):
    if contacts_list[n][0] == contacts_list[i][0] and contacts_list[n][1] == contacts_list[i][1]:
      for_del.append(i)
      for m in range(2, len(contacts_list[n])):
        if len(contacts_list[n][m]) == 0:
          contacts_list[n][m] = contacts_list[i][m]
  # и удадляем дубли:
  if len(for_del) >= 1:
    for el in reversed(for_del):
      contacts_list.pop(el)

# приводим телефоны к виду +7(999)999-99-99 доб.9999:
for el in contacts_list:
  pattern = r"(\+7|8)\s?\(?(\d\d\d)\)?(\s|[-])?(\d\d\d)(\s|[-])?(\d\d)(\s|[-])?(\d\d)\s?\(?([д][о][б]\.\s(\d*))?\)?"
  result = (re.sub(pattern, r"+7(\2)\4-\6-\8 \9", el[5])).strip()
  el[5] = result

pprint(contacts_list)

with open("phonebook.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(contacts_list)
