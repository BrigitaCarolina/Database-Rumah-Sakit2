import random
def create_kelas_kapasitas_kamar(connection):
    create_table_query = """
    CREATE TABLE IF NOT EXISTS KelasKapasitasKamar (
        nomor              int,
        lantai             int,
        kelas              varchar(10) NOT NULL,
        kapasitas          int NOT NULL,
        PRIMARY KEY (nomor, lantai)
    );
    """
    with connection.cursor() as cursor:
        cursor.execute(create_table_query)

def input_data_kelas_kapasitas_kamar(connection, fake):
    kelas = ['A', 'B', 'C']
    for i in range(50):
        lantai = random.randint(1, 5)
        nomor = i+1
        kelaskamar = kelas[random.randint(0, 2)]
        kapasitas = random.randint(2, 4)
        with connection.cursor() as cursor:
            cursor.execute(f"INSERT INTO KelasKapasitasKamar (nomor, lantai, kelas, kapasitas) VALUES ({nomor}, {lantai}, '{kelaskamar}', {kapasitas})")
            