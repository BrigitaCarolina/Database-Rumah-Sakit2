import random;

def create_kepala_departemen(connection):
    create_table_query = """
    CREATE TABLE KepalaDepartemen (
        nama_departemen     varchar(255) NOT NULL,
        kepala_departemen   varchar(255) NOT NULL,
        PRIMARY KEY (nama_departemen)
    );
    """
    with connection.cursor() as cursor:
        cursor.execute(create_table_query)

def input_kepala_departemen(connection, fake):
    nama_departemen = ["Dermatologi", "Patologi Klinik", "Orthopedi dan Traumatologi", "Medik Gigi dan Mulut", "Kebidanan dan Kandungan", "THT", "Penyakit Dalam", "Urologi", "Penyakit Saraf", "Bedah Saraf", "Bedah", "Kesehatan Anak", "Forensik dan Medikolegal", "Kesehatan Jiwa", "Anestesiologi", "Mikrobiologi Klinik", "Ilmu Gizi Klinik", "Farmakologi Klinik"]
    for i in range(len(nama_departemen)):
        kepala_departemen = fake.unique.name()
        departemen = nama_departemen[i]  
        with connection.cursor() as cursor:
            cursor.execute(f"INSERT INTO KepalaDepartemen (nama_departemen, kepala_departemen) VALUES ('{departemen}', '{kepala_departemen}')")
