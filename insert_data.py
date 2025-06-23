# Oluşturduğum tablolara insert methodu ile verileri girelim.

def insert_data(cursor):
    employees = [
        (1, 'Ali Kaya', 30, 'ali@gmail.com', 'İstanbul', 'Developer'),
        (2, 'Ziya Üstün', 25, 'ziya@gmail.com', 'İstanbul', 'Accounting'),
        (3, 'Zeynep Kuşçu', 29, 'zeynep@gmail.com', 'İzmit', 'Manager'),
        (4, 'Harun Har', 42, 'harun@gmail.com', 'İstanbul', 'Developer'),
        (5, 'Nur Hilal Çok', 22, 'nur@gmail.com', 'Ankara', 'Assistant')
    ]
    #Veri tabanına birden fazla ekelmeyi aynı anda yapıyoruz.
    cursor.executemany("INSERT INTO Employees VALUES (?,?,?,?,?,?)", employees)

    payments = [
        (1, 3, 5000),
        (2, 1, 3000),
        (3, 4, 2500),
        (4, 2, 2000),
        (5, 5, 1000)
    ]
    cursor.executemany("INSERT INTO Payments VALUES (?,?,?)", payments)

    #Veriler eklendiğinde bize bilgi versin
    print("Sample data inserted successfully")