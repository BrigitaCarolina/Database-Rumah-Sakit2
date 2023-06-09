import random
def create_dept_tenaga_medis(connection):
    create_table_query = """
    CREATE TABLE IF NOT EXISTS DepartemenTenagaMedis (
        nomor_lisensi       VARCHAR(25) NOT NULL,
        id_departemen       INT NOT NULL,
        PRIMARY KEY (nomor_lisensi),
        FOREIGN KEY (nomor_lisensi) REFERENCES LisensiTenagaMedis(nomor_lisensi),
        FOREIGN KEY (id_departemen) REFERENCES Departemen(id)
    );
    """

    with connection.cursor() as cursor:
        cursor.execute(create_table_query)


def input_data_dept_tenaga_medis(connection):
    with connection.cursor() as cursor:
        cursor.execute("SELECT nomor_lisensi FROM LisensiTenagaMedis")
        data_nomor = cursor.fetchall()

        cursor.execute("SELECT id FROM Departemen")
        data_id_dept = cursor.fetchall()

        for i in range(len(data_nomor)):
            cursor.execute(f"INSERT INTO DepartemenTenagaMedis (nomor_lisensi, id_departemen) VALUES ('{data_nomor[i]['nomor_lisensi']}', {data_id_dept[random.randint(0, 17)]['id']})")

