def create_lisensi_tenaga_medis(connection):
    create_table_query = """
    CREATE TABLE IF NOT EXISTS LisensiTenagaMedis (
        id                  INT AUTO_INCREMENT PRIMARY KEY,
        nomor_lisensi       VARCHAR(25) NOT NULL,
        FOREIGN KEY (id) REFERENCES Orang(id),
    );
    """

    with connection.cursor() as cursor:
        cursor.execute(create_table_query)