import random
def create_penempatan_kamar(connection):
    create_table_query = """
    CREATE TABLE IF NOT EXISTS PenempatanKamar (
        id                  int,
        lantai              int NOT NULL,
        nomor               int NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY (id) REFERENCES MedicalRecord(id),
        FOREIGN KEY (nomor, lantai) REFERENCES KelasKapasitasKamar(nomor, lantai)
    );
    """
    with connection.cursor() as cursor:
        cursor.execute(create_table_query)

def input_data_penempatan_kamar(connection, fake):
    cursor = connection.cursor()
    cursor.execute("SELECT id FROM MedicalRecord")
    id = cursor.fetchall()
    cursor.execute("SELECT nomor, lantai FROM KelasKapasitasKamar")
    lantai = cursor.fetchall()
    # cursor.execute("SELECT nomor FROM KelasKapasitasKamar")
    # nomor = cursor.fetchall()
    # random.shuffle(nomor)
    for i in range(len(id)):
        idkamar = id[i]['id']
        j = random.randint(0, 49)
        lantaiKamar = lantai[j]['lantai']
        nomorKamar = lantai[j]['nomor']
        with connection.cursor() as cursor:
            cursor.execute(f"INSERT INTO PenempatanKamar (id, lantai, nomor) VALUES ({idkamar}, {lantaiKamar}, {nomorKamar})")
            