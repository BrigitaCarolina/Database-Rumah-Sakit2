import random

def create_orang(connection):
    print("Something")
    create_table_query = """
    CREATE TABLE IF NOT EXISTS Orang (
        id              int auto_increment,
        nama_depan      varchar(255) NOT NULL,
        nama_belakang   varchar(255) NOT NULL,
        tanggal_lahir   date NOT NULL,
        jenis_kelamin   varchar(255) NOT NULL,
        nomor_telepon   varchar(100) NOT NULL,
        jalan           varchar(255) NOT NULL,
        desa_kelurahan  varchar(255) NOT NULL,
        kecamatan       varchar(255) NOT NULL,
        kabupaten_kota  varchar(255) NOT NULL,
        provinsi        varchar(255) NOT NULL,
        email           varchar(255) NOT NULL,
        PRIMARY KEY (id)     
    );
    """
    with connection.cursor() as cursor:
        cursor.execute(create_table_query)
    print("Something")

def input_data_orang(x, connection, fake):
    gender = ["laki-laki", "perempuan"]
    for i in range(x):
        namaDepan = fake.name()
        namaBelakang = fake.name()
        tanggalLahir  = fake.date()
        jenisKelamin = gender[random.randint(0, 1)]  
        nomor_telepon = "08" + "".join([str(random.randint(0,9)) for i in range(10)])
        email = fake.email()
        jalan = fake.street_address()
        desa = fake.city()
        kecamatan = fake.city()
        kabupaten = fake.city() 
        provinsi = fake.state()
        print(f"INSERT INTO Orang (nama_depan, nama_belakang, tanggal_lahir, jenis_kelamin, nomor_telepon, jalan, desa/kelurahan, kecamatan, kabupaten/kota, provinsi, email) VALUES ('{namaDepan}', '{namaBelakang}', '{tanggalLahir}', '{jenisKelamin}','{nomor_telepon}', '{jalan}', '{desa}', '{kecamatan}', '{kabupaten}', '{provinsi}', '{email}')")
        with connection.cursor() as cursor:
            cursor.execute(f"INSERT INTO Orang (nama_depan, nama_belakang, tanggal_lahir, jenis_kelamin, nomor_telepon, jalan, desa_kelurahan, kecamatan, kabupaten_kota, provinsi, email) VALUES ('{namaDepan}', '{namaBelakang}', '{tanggalLahir}', '{jenisKelamin}','{nomor_telepon}', '{jalan}', '{desa}', '{kecamatan}', '{kabupaten}', '{provinsi}', '{email}')")
