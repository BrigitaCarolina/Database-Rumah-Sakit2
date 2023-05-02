import random
def create_kecamatankabupatenkota(connection):
    print("Something")
    create_table_query = """
    CREATE TABLE IF NOT EXISTS KecamatanKabupatenKota (
        kecamatan       varchar(255) NOT NULL,
        kabupaten_kota  varchar(255) NOT NULL,
        PRIMARY KEY (kecamatan),
        FOREIGN KEY (kabupaten_kota) REFERENCES KabupatenProvinsi(kabupaten_kota)     
    );
    """
    with connection.cursor() as cursor:
        cursor.execute(create_table_query)
    print("Something")

def input_data_kecamatankabupatenkota(x, connection, fake):
    #take kabupaten_kota from KabupatenProvinsi
    with connection.cursor() as cursor:
        cursor.execute("SELECT kabupaten_kota FROM KabupatenProvinsi")
        kabupaten_kota_list = cursor.fetchall()

    for i in range(x):
        kecamatan = fake.unique.city()
        kabupaten = fake.random_choices(elements=kabupaten_kota_list)[0]['kabupaten_kota'] 
        print(f"INSERT INTO KecamatanKabupatenKota (kecamatan, kabupaten/kota) VALUES ('{kecamatan}', '{kabupaten}')")
        with connection.cursor() as cursor:
            cursor.execute(f"INSERT INTO KecamatanKabupatenKota (kecamatan, kabupaten_kota) VALUES ('{kecamatan}', '{kabupaten}')")
