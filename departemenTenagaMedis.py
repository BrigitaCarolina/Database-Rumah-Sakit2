import random
def create_dept_tenaga_medis(connection):
    create_table_query = """
    CREATE TABLE IF NOT EXISTS DepartemenTenagaMedis (
        nomor_lisensi       VARCHAR(25) NOT NULL PRIMARY KEY,
        id_departemen       INT NOT NULL,
        FOREIGN KEY (nomor_lisensi) REFERENCES LisensiTenagaMedis(nomor_lisensi),
        FOREIGN KEY (id_departemen) REFERENCES Departemen(id)
    );
    """

    with connection.cursor() as cursor:
        cursor.execute(create_table_query)


def input_data_dept_tenaga_medis(x, connection, fake):
    with connection.cursor() as cursor:
        cursor.execute("SELECT nomor_lisensi FROM LisensiTenagaMedis")
        dataLisensi = cursor.fetchall()
        random.shuffle(dataLisensi)
        cursor.execute("SELECT id FROM Departemen")
        dataID = cursor.fetchall()
        random.shuffle(dataID)
    
    for idx, dept in enumerate(dataID):
        id = dept['id']
        nomor_lisensi = idx+101
