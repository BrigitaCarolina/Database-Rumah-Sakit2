
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
        email           varchar(255) NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY (desa_kelurahan) REFERENCES DesaKecamatan(desa_kelurahan)
    );
    """
    with connection.cursor() as cursor:
        cursor.execute(create_table_query)
    print("Something")

def input_data_orang(x, connection, fake):
    #take desa_keluarahan from DesaKecamatan
    with connection.cursor() as cursor:
        cursor.execute("SELECT desa_kelurahan FROM DesaKecamatan")
        desa_kelurahan_list = cursor.fetchall()

    gender = ["laki-laki", "perempuan"]
    for i in range(x):
        namaDepan = fake.name()
        namaBelakang = fake.name()
        tanggalLahir  = fake.date()
        jenisKelamin = gender[random.randint(0, 1)]  
        nomor_telepon = "08" + "".join([str(random.randint(0,9)) for i in range(10)])
        desa_kelurahan = fake.random_choices(elements=desa_kelurahan_list)[0]['desa_kelurahan']
        email = fake.email()
        jalan = fake.street_address()
        print(f"INSERT INTO Orang (nama_depan, nama_belakang, tanggal_lahir, jenis_kelamin, nomor_telepon, jalan, desa/kelurahan, email) VALUES ('{namaDepan}', '{namaBelakang}', '{tanggalLahir}', '{jenisKelamin}','{nomor_telepon}', '{jalan}', '{desa_kelurahan}', '{email}')")
        with connection.cursor() as cursor:
            cursor.execute(f"INSERT INTO Orang (nama_depan, nama_belakang, tanggal_lahir, jenis_kelamin, nomor_telepon, jalan, desa_kelurahan, email) VALUES ('{namaDepan}', '{namaBelakang}', '{tanggalLahir}', '{jenisKelamin}','{nomor_telepon}', '{jalan}', '{desa_kelurahan}', '{email}')")