import random

def create_departemen(connection):
    create_table_query = """
    CREATE TABLE Departemen (
        id                  int auto_increment, 
        nama_departemen     varchar(255) NOT NULL,
        kepala_departemen   varchar(255) NOT NULL,
        PRIMARY KEY (id) 
    );
    """
    with connection.cursor() as cursor:
        cursor.execute(create_table_query)

def input_departemen(connection, fake):
    nama_departemen = ["Dermatologi", "Patologi Klinik", "Orthopedi dan Traumatologi", "Medik Gigi dan Mulut", "Kebidanan dan Kandungan", "THT", "Penyakit Dalam", "Urologi", "Penyakit Saraf", "Bedah Saraf", "Bedah", "Kesehatan Anak", "Forensik dan Medikolegal", "Kesehatan Jiwa", "Anestesiologi", "Mikrobiologi Klinik", "Ilmu Gizi Klinik", "Farmakologi Klinik"]
    for i in range(len(nama_departemen)):
        kepala_departemen = fake.name()
        departemen = nama_departemen[random.randint(0, len(nama_departemen)-1)]  
        with connection.cursor() as cursor:
            cursor.execute(f"INSERT INTO Departemen (nama_departemen, kepala_departemen) VALUES ('{departemen}', '{kepala_departemen}')")
