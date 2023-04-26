import sqlite3
import numpy as np
import constant
# Tao table Iris neu no khong ton tai
def create_table():
    conn = sqlite3.connect('iris.db')
    with conn:
        cursor = conn.cursor()

        cursor.execute("""CREATE TABLE IF NOT EXISTS iris
                          (id INTEGER PRIMARY KEY,
                           bitcode BLOB NOT NULL)""")


# Lay bitcode tu input
def get_bitcode():
    # Simulate getting bitcode from input
    bitcode = input("Enter bitcode: ")
    return bitcode

# Kiem tra xem bitcode co trong database hay khong
def search_iris(bitcode):
    # Search for iris with matching bitcode
    conn = sqlite3.connect('iris.db')
    with conn:
        cursor = conn.cursor()

        cursor.execute("""SELECT * FROM iris""")
        rows = cursor.fetchall()

        #Hamming distance
        #min_daistance de theo doi khoang cach nho nhat cua cac bitcode
        min_distance = np.inf
        matching_rows = [] # luu tru cac bitcode lien quan den bitcode dau vao
        
        #truy suat 
        for row in rows:
            # la gia tri trung binh , the hien ty le khac nhau giua cac bitcode trong db va input
            distance = np.mean([char1 != char2 for char1, char2 in zip(row[1], bitcode)])
            # neu distance nho hon Sai so thi them vao matching_rows
            if distance <= constant.SS:
                #them bit lien quan vaoa matching_rows
                matching_rows.append(row)
                #cap nhat lai min_distance
                min_distance = min(min_distance, distance)

        # Neu khong co bitcode lien quan thi in ra thong bao va nguoc lai
        if len(matching_rows) == 0:
            print("No iris with matching bitcode found.")
        else:
            print("Matching iris found:")
            for row in matching_rows:
                print(row)

def save_iris():
    # lay bit code tu ham get_bitcode
    bitcode = get_bitcode()

    # Save the iris to the database
    conn = sqlite3.connect('iris.db')
    with conn:
        cursor = conn.cursor()

        cursor.execute("""INSERT INTO iris (bitcode) VALUES (?)""", (bitcode,))

        print("Iris saved successfully.")


def show_iris():
    # hien thi cac bit code trong db
    conn = sqlite3.connect('iris.db')
    with conn:
        cursor = conn.cursor()

        cursor.execute("""SELECT bitcode FROM iris""")
        rows = cursor.fetchall()

        if len(rows) == 0:
            print("No iris in the database.")
        else:
            print("Bitcodes in the database:")
            for row in rows:
                print(row[0])

def main():
    create_table()

    while True:
        choice = input("Enter 1 to search iris, 2 to save iris to database,3 to show all iris in database , or 4 to exit: ")
        if choice == '1':
            bitcode = get_bitcode()
            search_iris(bitcode)
        elif choice == '2':
            save_iris()
        elif choice == '3':
            show_iris()
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
