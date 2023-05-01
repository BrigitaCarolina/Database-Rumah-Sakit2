import random
def create_penempatan_kamar(connection):
    create_table_query = """
    CREATE TABLE IF NOT EXISTS KamarPasien (
        id                  int,
        lantai              int,
        nomor               int,
        PRIMARY KEY (id),
        FOREIGN KEY (id) REFERENCES MedicalRecord(id),
        FOREIGN KEY (lantai, nomor) REFERENCES KelasKapasitasKamar(lantai, nomor)
    );
    """
    with connection.cursor() as cursor:
        cursor.execute(create_table_query)

def input_data_kamar(connection, fake):
    cursor = connection.cursor()
    cursor.execute("SELECT id FROM MedicalRecord")
    id = cursor.fetchall()
    cursor.execute("SELECT lantai FROM KelasKapasitasKamar")
    lantai = cursor.fetchall()
    random.shuffle(lantai)
    cursor.execute("SELECT nomor FROM KelasKapasitasKamar")
    nomor = cursor.fetchall()
    random.shuffle(nomor)
    for i in range(len(id)):
        idkamar = id[i]['id']
        lantaiKamar = lantai[i]['lantai']
        nomorKamar = nomor[i]['nomor']
        with connection.cursor() as cursor:
            cursor.execute(f"INSERT INTO KamarPasien (id, lantai, nomor) VALUES ({idkamar}, {lantaiKamar}, {nomorKamar})")
            