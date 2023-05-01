import random
def create_lisensi_tenaga_medis(connection):
    create_table_query = """
    CREATE TABLE IF NOT EXISTS DepartemenTenagaMedis (
        id                  INT AUTO_INCREMENT PRIMARY KEY,
        nomor_lisensi       VARCHAR(25) NOT NULL,
        FOREIGN KEY (id) REFERENCES Orang(id)
    );
    """

    with connection.cursor() as cursor:
        cursor.execute(create_table_query)


def input_data_lisensi_tenaga_medis(x, connection):
    with connection.cursor() as cursor:
        cursor.execute("SELECT id FROM Orang")
        data_id = cursor.fetchall()
        random.shuffle(data_id)

        for i in range(x):
            nomor_lisensi = i+101
            cursor.execute(f"INSERT INTO LisensiTenagaMedis (id, nomor_lisensi) VALUES ({data_id[i]['id']}, '{nomor_lisensi}')")