#Veri okuma
#Oluşturduğumuz veri tabanına bağlanarak çeşitli okuma işlemleri yapacağız.
import sqlite3

#Veri tabanına bağlan.
conn = sqlite3.connect('database.db')

#Bütün veriyi getirelim
def read_data():
    #Cursor (imleç) oluşturuyorum.
    cursor = conn.cursor()
    print("----------Select All----------")
    #Okuma
    cursor.execute("SELECT * FROM Employees")
    records = cursor.fetchall()
    for row in records:
        print(f"ID: {row[0]}, İSİM: {row[1]}, YAŞ: {row[2]}, EMAIL: {row[3]}, Şehir: {row[4]}, Departman: {row[5]}")

def read_data2():
    #Belirlenen Kolonları okuma
    cursor = conn.cursor()
    print("----------Select Columns----------")
    cursor.execute("SELECT name,department FROM Employees")
    records = cursor.fetchall()
    for row in records:
        print(f"İsim: {row[0]}, Departman: {row[1]}")

    #Where, filtreleme ile okuma
    print("----------Where City = İstanbul ----------")
    cursor.execute("SELECT * FROM Employees WHERE city = 'İstanbul'")
    records = cursor.fetchall()
    for row in records:
        print(row)

    #Order by, yaşa göre sıralama yapalım.
    print("----------Order by age ----------")
    cursor.execute("SELECT * FROM Employees ORDER BY age")
    records = cursor.fetchall()
    for row in records:
        print(row)

    #Limit, belirli bir limit ile veri çekme
    print("----------Limit by 3 ----------")
    cursor.execute("SELECT * FROM Employees LIMIT 3")
    records = cursor.fetchall()
    for row in records:
        print(row)

    #Average, maaş ortalamalarını alalaım
    print("----------Aggregate Monthly Payment----------")
    cursor.execute("SELECT AVG(monthly_payment) FROM Payments")
    records = cursor.fetchall()
    print(records[0])

    #Group by, Hangi şehirde kaç çalışan var onu görelim
    print("----------Aggregate Functions Group by----------")
    cursor.execute("SELECT city, COUNT(*) FROM Employees GROUP BY city")
    result = cursor.fetchall()
    print(result)

    #Son olarak iki tablodan verilerle kimin maaşı ne kadar onu görelim.
    print("----------Monthly Payments----------")
    cursor.execute("SELECT name,monthly_payment FROM Employees e INNER JOIN Payments p ON e.id = p.employee_id ")
    records = cursor.fetchall()
    for row in records:
        print(f"İsim: {row[0]}, Maaş: {row[1]}")


# Veri ekleme güncelleme ve silme yöntemlerini görelim

# Tek veri ekleme
def insert_data():
    cursor = conn.cursor()
    print("----------Data Added----------")
    cursor.execute("INSERT INTO Employees VALUES (6, 'Tümer Kazık', 36, 'tumer@gmail.cum', 'Yozgat', 'Developer')")
    conn.commit()


# Veri güncelleme
def update_data():
    cursor = conn.cursor()
    print("----------Data Updated----------")
    cursor.execute("UPDATE Employees SET age = 38 WHERE name = 'Tümer Kazık'")
    conn.commit()


# Veri silme
def delete_data():
    cursor = conn.cursor()
    print("----------Data Deleted----------")
    cursor.execute("DELETE FROM Employees WHERE id = 4"),
    conn.commit()
    #verinin son halini görelim
    read_data()

if __name__ == '__main__':
    read_data()
    read_data2()
    insert_data()
    update_data()
    delete_data()

