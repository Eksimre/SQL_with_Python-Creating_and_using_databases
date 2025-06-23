import sqlite3
import os
import create_table
import insert_data

#Creating a database
#Veri tabanı oluşturma

def create_database():
    #Bulunduğumuz klasörün içinde çalışabilmek için
    if os.path.exists("database.db"):
        #Veri tabanını oluştururken olası hataları engellmek için her çalıştırmamda veri setini siliyorum.
        os.remove("database.db")

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    return conn, cursor

def main():
    conn, cursor = create_database()  #Veri tabanını oluşturacak, başlantı ve imleci vericek.

    #Olası hataları görebilmek için
    try:
        create_table.create_table(cursor) #Fonksiyonu çağırıyorum
        insert_data.insert_data(cursor)
        conn.commit() #Cursor'un işlemlerini uygula.
    except sqlite3.OperationalError:
        print(e)
    finally:
        conn.close() #Her çalıştırma sonrası veri tabanı ile olan bağlantıyı kapatır.

if __name__ == "__main__":
    main()