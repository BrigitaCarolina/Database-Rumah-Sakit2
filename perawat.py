

def create_perawat(connection):
    create_table_query = """
    CREATE TABLE IF NOT EXISTS Perawat (
        nomor_lisensi   varchar(25),
        PRIMARY KEY (nomor_lisensi),
        FOREIGN KEY (nomor_lisensi) REFERENCES TenagaMedis(nomor_lisensi)
    );
    """
    with connection.cursor() as cursor:
        cursor.execute(create_table_query)


def input_data_perawat(x, connection):
    connection.cursor().execute("SELECT nomor_lisensi FROM dokter")
    lisensiDokter = connection.cursor().fetchall()
    connection.cursor().execute("SELECT nomor_lisensi FROM TenagaMedis")
    lisensiTenagaMedis = connection.cursor().fetchall()
    new_list = [x for x in lisensiTenagaMedis if x not in lisensiDokter]
    print(new_list)
    for i in range(x):
        nomor_lisensi = new_list[i]
        with connection.cursor() as cursor:
            cursor.execute(f"INSERT INTO Perawat (nomor_lisensi) VALUES ('{nomor_lisensi}')")