import random

def create_kontak_darurat(connection):
    create_table_query = """
    CREATE TABLE IF NOT EXISTS KontakDarurat (
        id                  int auto_increment,
        nomor               varchar(100),
        nama                varchar(255),
        PRIMARY KEY (id, nomor, nama),
        FOREIGN KEY (id) REFERENCES Pasien(id)
    )
    """
    with connection.cursor() as cursor:
        cursor.execute(create_table_query)

def insert_kontak_darurat(connection, fake):
    # Take id from Pasien
    with connection.cursor() as cursor:
        cursor.execute("SELECT id FROM Pasien")
        pasien_id = cursor.fetchall()
    
    # Insert KontakDarurat
    for i in range(len(pasien_id)):
        # Take random id from Pasien
        success = False
        while (not success):
            random_id = random.choice(pasien_id)['id']
            if random_id in [d['id'] for d in pasien_id]:
                pasien_id.remove({'id': random_id})
                success = True

        nomor = fake.phone_number()
        nama = fake.name()
        insert_query = f"""
        INSERT INTO KontakDarurat (id, nomor, nama)
        VALUES ({random_id}, '{nomor}', '{nama}')
        """
        with connection.cursor() as cursor:
            cursor.execute(insert_query)