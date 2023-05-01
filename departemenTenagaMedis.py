import random
def create_departemen_tenaga_medis(connection):
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


def input_data_tenaga_medis(x, connection, fake):
    with connection.cursor() as cursor:
        cursor.execute("SELECT ")