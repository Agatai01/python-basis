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
def search_contact(value):
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        SELECT * FROM contacts 
        WHERE name LIKE %s OR phone LIKE %s
    """, ('%' + value + '%', '%' + value + '%'))

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    conn.close()

# UPDATE
def update_contact():
    conn = connect()
    cur = conn.cursor()

    value = input("Enter name or phone to find contact: ")

    # 🔍 алдымен тексереміз
    cur.execute("SELECT * FROM contacts WHERE name=%s OR phone=%s", (value, value))
    row = cur.fetchone()

    if not row:
        print("Contact not found!")
        cur.close()
        conn.close()
        return

    print("1. Update name")
    print("2. Update phone")
    choice = input("Choose: ")

    if choice == "1":
        new_name = input("Enter new name: ")
        cur.execute("""
            UPDATE contacts 
            SET name=%s 
            WHERE name=%s OR phone=%s
        """, (new_name, value, value))

    elif choice == "2":
        new_phone = input("Enter new phone: ")
        cur.execute("""
            UPDATE contacts 
            SET phone=%s 
            WHERE name=%s OR phone=%s
        """, (new_phone, value, value))

    else:
        print("Invalid choice")
        cur.close()
        conn.close()
        return

    conn.commit()

    cur.close()
    conn.close()

    print("Updated successfully!")

# DELETE
def delete_contact(value):
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        DELETE FROM contacts 
        WHERE name=%s OR phone=%s
    """, (value, value))

    conn.commit()
    cur.close()
    conn.close()

# FILTER
def filter_by_prefix(prefix):
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        SELECT * FROM contacts 
        WHERE phone LIKE %s
    """, (prefix + '%',))

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    conn.close()