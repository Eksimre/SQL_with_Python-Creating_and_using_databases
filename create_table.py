#Veri tabanı için tabloları oluştralım
#Bir şirketin çalışan bilgileri ve maaş bilgileri olmak üzere iki ayrı tablo şeklinde veri yapısını oluşturuyorum.

def create_table(cursor):
    cursor.execute("""
                   CREATE TABLE Employees(
                       id    INTEGER PRIMARY KEY,
                       name  VARCHAR(255) NOT NULL,
                       age   INTEGER,
                       email VARCHAR(50) UNIQUE ,
                       city  VARCHAR(50),
                       department  VARCHAR(50)
                   )
                   """)

    cursor.execute("""
                CREATE TABLE Payments (
                     id INTEGER PRIMARY KEY,
                     employee_id INTEGER,
                     monthly_payment INTEGER,
 
            FOREIGN KEY (employee_id) REFERENCES Employees(id)
        )
    """)

