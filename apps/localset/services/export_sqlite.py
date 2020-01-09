#!/usr/bin/env python
import os
import sqlite3
import json

fixture_settings = [
    {'sql': "SELECT id, name, surname, patronymic FROM user",
     'keys': ('pk', 'name', 'surname', 'patronymic',),
     'initial_file': "company/fixtures/employees_initial.json",
     'model': 'company.Employee'},
    {'sql': "SELECT id, name FROM department",
     'keys': ('pk', 'name', ),
     'initial_file': "company/fixtures/depatments_initial.json",
     'model': 'company.Departments'},
]


def conver_data(sql, keys, model, name_write_file):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    conn = sqlite3.connect(os.path.join(BASE_DIR, 'localset/services/database.db'))

    cursor = conn.cursor()
    print(os.path.join(BASE_DIR, name_write_file))
    data = [dict(zip(keys, row)) for row in cursor.execute(sql).fetchall()]
    for row in data:
        row['model'] = model
        row['fields'] = {key: row[key] for key in keys if not key == 'pk'}
        for key in keys:
            if not key == 'pk':
                row.pop(key)

    with open(os.path.join(BASE_DIR, name_write_file), "w") as write_file:
        json.dump(data, write_file, indent=4, ensure_ascii=False)
    print(f' create initial {model}')


def export():
    for item in fixture_settings:
        conver_data(
            item['sql'],
            item['keys'],
            item['model'],
            item['initial_file'])
