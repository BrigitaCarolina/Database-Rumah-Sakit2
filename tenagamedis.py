import random

def create_tenagamedis(connection):
    create_table_query = """
    CREATE TABLE IF NOT EXISTS TenagaMedis (
        id              int, 
        nomor_lisensi   varchar(25),
        id_departemen   int
        PRIMARY KEY (id),
        FOREIGN KEY (id) REFERENCES Orang(id),
        FOREIGN KEY (id_departemen) REFERENCES Departemen(id)      
    );
    """
    with connection.cursor() as cursor:
        cursor.execute(create_table_query)


def input_data_tenaga_medis(x, connection):
    connection.cursor().execute("SELECT id FROM orang")
    connection.cursor().execute("SELECT id FROM orang")
    dataId = connection.cursor().fetchall()
    random.shuffle(dataId)
    connection.cursor().execute("SELECT id FROM Departemen")
    dataIdDept = connection.cursor().fetchall()
    random.shuffle(dataIdDept)
    for i in range(x):
        id = dataId[i]['id']
        nomorlisensi = i+101
        idDept = dataIdDept[i]['id']
        with connection.cursor() as cursor:
            cursor.execute(f"INSERT INTO TenagaMedis (id, nomor_lisensi, id_departemen) VALUES ({id}, '{nomorlisensi}', {idDept})")