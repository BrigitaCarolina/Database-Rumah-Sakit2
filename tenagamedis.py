import random

def create_tenagamedis(connection):
    create_table_query = """
    CREATE TABLE IF NOT EXISTS TenagaMedis (
        id              int PRIMARY KEY, 
        nomor_lisensi   varchar(25),
        id_departemen   int,
        FOREIGN KEY (id) REFERENCES Orang(id),
        FOREIGN KEY (id_departemen) REFERENCES Departemen(id)      
    );
    """
    with connection.cursor() as cursor:
        cursor.execute(create_table_query)


def input_data_tenaga_medis(x, connection, fake):
    with connection.cursor() as cursor:
        cursor.execute("SELECT id FROM Orang")
        dataId = cursor.fetchall()
        random.shuffle(dataId)
        cursor.execute("SELECT id FROM Departemen")
        dataIdDept = cursor.fetchall()
        random.shuffle(dataIdDept)
    for i in range(len(dataIdDept)):
        id = dataId[i]['id']
        nomorlisensi = i+101
        idDept = dataIdDept[i]['id']
        with connection.cursor() as cursor:
            cursor.execute(f"INSERT INTO TenagaMedis (id, nomor_lisensi, id_departemen) VALUES ({id}, '{nomorlisensi}', {idDept})")

    indexDataId = len(dataIdDept)
    for i in range(x-len(dataIdDept)):
        id = dataId[indexDataId]['id']
        nomorlisensi = i+101
        idDept = dataIdDept[random.randint(0, len(dataIdDept) - 1)]['id']
        with connection.cursor() as cursor:
            cursor.execute(f"INSERT INTO TenagaMedis (id, nomor_lisensi, id_departemen) VALUES ({id}, '{nomorlisensi}', {idDept})")
        indexDataId += 1