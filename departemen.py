import random

def create_departemen(connection):
    create_table_query = """
    CREATE TABLE Departemen (
        id                  int auto_increment, 
        nama_departemen     varchar(255) NOT NULL,
        PRIMARY KEY (id) 
        FOREIGN KEY (nama_departemen) REFERENCES KepalaDepartemen(nama_departemen)
    );
    """
    with connection.cursor() as cursor:
        cursor.execute(create_table_query)


def input_departemen(connection, fake):
    cursor = connection.cursor()
    cursor.execute("SELECT nama_departemen FROM KepalaDepartemen")
    namaDepartemen = cursor.fetchall()
    for i in range(x):
        namaDepartemen = namaDepartemen[i]['nama_departemen']
        with connection.cursor() as cursor:
            cursor.execute(f"INSERT INTO departemen (nama_departemen) VALUES ('{namaDepartemen}')")
