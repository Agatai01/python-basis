from connect import connect
import csv

# INSERT
def insert_contact(name, phone):
    conn = connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO contacts (name, phone) VALUES (%s, %s)", (name, phone))
    conn.commit()
    cur.close()
    conn.close()

# CSV import
def insert_from_csv(file):
    conn = connect()
    cur = conn.cursor()

    with open(file, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            cur.execute(
                "INSERT INTO contacts (name, phone) VALUES (%s, %s)",
                (row[0], row[1])
            )

    conn.commit()
    cur.close()
    conn.close()

# SELECT
def get_contacts():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM contacts")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()

# SEARCH
def search_by_name(name):
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM contacts WHERE name ILIKE %s", ('%' + name + '%',))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()

# UPDATE
def update_phone(name, new_phone):
    conn = connect()
    cur = conn.cursor()
    cur.execute("UPDATE contacts SET phone=%s WHERE name=%s", (new_phone, name))
    conn.commit()
    cur.close()
    conn.close()

# DELETE
def delete_contact(name):
    conn = connect()
    cur = conn.cursor()
    cur.execute("DELETE FROM contacts WHERE name=%s", (name,))
    conn.commit()
    cur.close()
    conn.close()