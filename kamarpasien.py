import random
def create_kamar_pasien(connection):
    create_table_query = """
    CREATE TABLE IF NOT EXISTS KamarPasien (
        id                  int,
        lantai              int,
        nomor               int,
        kelas               varchar(10) NOT NULL,
        kapasitas           int NOT NULL,
        PRIMARY KEY (id, lantai, nomor),
        FOREIGN KEY (id) REFERENCES MedicalRecord(id)
    );
    """
    with connection.cursor() as cursor:
        cursor.execute(create_table_query)

def input_data_kamar(connection, fake):
    cursor = connection.cursor()
    cursor.execute("SELECT id FROM MedicalRecord")
    id = cursor.fetchall()
    kelas = ['A', 'B', 'C']
    for i in range(len(id)):
        idkamar = id[i]['id']
        lantai = random.randint(1, 20)
        nomor = (lantai * 100) + random.randint(1, 3)
        kelaskamar = kelas[random.randint(0, 2)]
        kapasitas = random.randint(2, 4)
        with connection.cursor() as cursor:
            cursor.execute(f"INSERT INTO KamarPasien (id, lantai, nomor, kelas, kapasitas) VALUES ({idkamar}, {lantai}, {nomor}, '{kelaskamar}', {kapasitas})")