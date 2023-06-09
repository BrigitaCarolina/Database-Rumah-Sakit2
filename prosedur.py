import random
def create_prosedur(connection):
    create_table_query = """
    CREATE TABLE IF NOT EXISTS Prosedur (
        id int auto_increment,
        id_medical_records int NOT NULL,
        nama_pengobatan varchar(255) NOT NULL,
        dosis varchar(255) NOT NULL,
        tanggal_mulai date NOT NULL,
        tanggal_selesai date NOT NULL,
        biaya int NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY (id_medical_records) REFERENCES MedicalRecord(id)
    );
    """
    with connection.cursor() as cursor:
        cursor.execute(create_table_query)

def input_data_prosedur(x, connection, fake):
    #take id_medical_records from MedicalRecord
    with connection.cursor() as cursor:
        cursor.execute("SELECT id FROM MedicalRecord")
        id_medical_records_list = cursor.fetchall()
    
    for i in range(x):
        id = i+1
        id_medical_records = fake.random_choices(elements=id_medical_records_list)[0]['id']
        nama_pengobatan = fake.word()
        dosis = fake.word()
        tanggal_mulai = fake.date()
        tanggal_selesai = fake.date()
        biaya = random.randint(1, 1000)
        query = "INSERT INTO Prosedur (id, id_medical_records, nama_pengobatan, dosis, tanggal_mulai, tanggal_selesai, biaya) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        with connection.cursor() as cursor:
            cursor.execute(query, (id, id_medical_records, nama_pengobatan, dosis, tanggal_mulai, tanggal_selesai, biaya))
        connection.commit()