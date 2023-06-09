def create_pasien(connection):
    create_table_query = """
    CREATE TABLE IF NOT EXISTS Pasien (
        id                  int NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY (id) REFERENCES Orang(id)
    );
    """
    with connection.cursor() as cursor:
        cursor.execute(create_table_query)

def input_data_pasien(x, connection, fake):
    cursor = connection.cursor()
    cursor.execute("SELECT id FROM Orang")
    id = cursor.fetchall()
    cursor.execute("SELECT id FROM LisensiTenagaMedis")
    id_tenaga_medis = cursor.fetchall()
    new_list  = [x for x in id if x not in id_tenaga_medis]
    for i in range(x):
        id = new_list[i]['id'] 
        with connection.cursor() as cursor:
            cursor.execute(f"INSERT INTO Pasien (id) VALUES ({id})")


    