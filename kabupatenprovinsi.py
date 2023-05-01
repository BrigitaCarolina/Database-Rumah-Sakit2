def create_kabupatenprovinsi(connection):
    print("Something")
    create_table_query = """
    CREATE TABLE IF NOT EXISTS KabupatenProvinsi (
        kabupaten_kota  varchar(255) NOT NULL,
        provinsi        varchar(255) NOT NULL,
        PRIMARY KEY (kabupaten_kota)     
    );
    """
    with connection.cursor() as cursor:
        cursor.execute(create_table_query)
    print("Something")

def input_data_kabupatenprovinsi(x, connection, fake):
    for i in range(x):
        kabupaten = fake.city() 
        provinsi = fake.state()
        print(f"INSERT INTO KabupatenProvinsi (kabupaten_kota, provinsi) VALUES ('{kabupaten}', '{provinsi}')")
        with connection.cursor() as cursor:
            cursor.execute(f"INSERT INTO KabupatenProvinsi (kabupaten_kota, provinsi) VALUES ('{kabupaten}', '{provinsi}')")
