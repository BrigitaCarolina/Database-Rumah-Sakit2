

def create_perawat(connection):
    create_table_query = """
    CREATE TABLE IF NOT EXISTS Perawat (
        id   int,
        PRIMARY KEY (id),
        FOREIGN KEY (id) REFERENCES LisensiTenagaMedis(id)
    );
    """
    with connection.cursor() as cursor:
        cursor.execute(create_table_query)


def input_data_perawat(x, connection, fake):
    cursor = connection.cursor()
    cursor.execute("SELECT id FROM dokter")
    lisensiDokter = cursor.fetchall()
    cursor.execute("SELECT id FROM LisensiTenagaMedis")
    lisensiTenagaMedis = cursor.fetchall()
    new_list = [x for x in lisensiTenagaMedis if x not in lisensiDokter]
    print(new_list)
    for i in range(x):
        nomor_lisensi = new_list[i]['id']
        with connection.cursor() as cursor:
            cursor.execute(f"INSERT INTO Perawat (id) VALUES ({nomor_lisensi})")