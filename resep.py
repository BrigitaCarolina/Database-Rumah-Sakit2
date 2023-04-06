def create_resep(connection):
    create_table_query = """
    CREATE TABLE IF NOT EXISTS Resep (
        id int auto_increment,
        id_medical_records int,
        nama_pengobatan varchar(255),
        dosis varchar(255),
        tanggal_mulai date,
        tanggal_selesai date,
        PRIMARY KEY (id),
        FOREIGN KEY (id_medical_records) REFERENCES MedicalRecord(id)
    );
    """
    with connection.cursor() as cursor:
        cursor.execute(create_table_query)

def input_data_resep(x, connection, fake):
    # take id_medical_records from MedicalRecord
    with connection.cursor() as cursor:
        cursor.execute("SELECT id FROM MedicalRecord")
        id_medical_records_list = cursor.fetchall()
    
    # insert data
    for i in range(x):
        id = i + 1
        id_medical_records = fake.random_choices(elements=id_medical_records_list)['id']
        nama_pengobatan = fake.word()
        dosis = fake.word()
        tanggal_mulai = fake.date()
        tanggal_selesai = fake.date()
        query = "INSERT INTO Resep VALUES (%s, %s, %s, %s, %s, %s)"
        with connection.cursor() as cursor:
            cursor.execute(query, (id, id_medical_records, nama_pengobatan, dosis, tanggal_mulai, tanggal_selesai))
        connection.commit()