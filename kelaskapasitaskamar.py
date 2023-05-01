import random
def create_penempatan_kamar(connection):
    create_table_query = """
    CREATE TABLE IF NOT EXISTS PenempatanKamar (
        nomor              int,
        lantai             int,
        kelas              varchar(10) NOT NULL,
        kapasitas          int NOT NULL
        PRIMARY KEY (nomor, lantai)
    );
    """
    with connection.cursor() as cursor:
        cursor.execute(create_table_query)

def input_data_kamar(connection, fake):
    kelas = ['A', 'B', 'C']
    for i in range(len(id)):
        nomor = (lantai * 100) + random.randint(1, 3)
        lantai = random.randint(1, 20)
        kelaskamar = kelas[random.randint(0, 2)]
        kapasitas = random.randint(2, 4)
        with connection.cursor() as cursor:
            cursor.execute(f"INSERT INTO PenempatanKamar (nomor, lantai, kelas, kapasitas) VALUES ({nomor}, {lantai}, '{kelaskamar}', {kapasitas})")
            