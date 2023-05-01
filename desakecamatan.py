import random

def create_desakecamatan(connection):
    print("Something")
    create_table_query = """
    CREATE TABLE IF NOT EXISTS DesaKecamatan (
        desa_kelurahan  varchar(255) NOT NULL,
        kecamatan       varchar(255) NOT NULL,
        PRIMARY KEY (desa_kelurahan)     
    );
    """
    with connection.cursor() as cursor:
        cursor.execute(create_table_query)
    print("Something")

def input_data_orang(x, connection, fake):
    for i in range(x):
        desa = fake.city()
        kecamatan = fake.city()
        print(f"INSERT INTO DesaKecamatan (desa/kelurahan, kecamatan) VALUES ('{desa}', '{kecamatan}')")
        with connection.cursor() as cursor:
            cursor.execute(f"INSERT INTO DesaKecamatan (desa_kelurahan, kecamatan) VALUES ('{desa}', '{kecamatan}')")
