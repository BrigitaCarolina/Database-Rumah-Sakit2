import random
def create_teslab(connection):
    # connection.cursor().execute("DROP TABLE TesLab")
    create_table_query = """
    CREATE TABLE TesLab (
        id int auto_increment, 
        id_medical_records int,
        tanggal_tes date,
        hasil varchar(255),
        tempat varchar(100),
        PRIMARY KEY (id),
        FOREIGN KEY(id_medical_records) REFERENCES MedicalRecord(id)
    );
    """
    with connection.cursor() as cursor:
        cursor.execute(create_table_query)

def input_data_teslab(x, connection, fake):
    connection.cursor().execute("SELECT id_medical_records FROM MedicalRecord")
    data = connection.cursor().fetchall()
    laboratorium = ["Lab Klinik" , "Lab Patologi Klinik", "Lab Mikrobiologi", "Lab Kimia Klinik", "Lab Imunologi", "Lab Hematologi", ""]
    for i in range(x):
        id_medical_records = data[i]['id']
        tanggal_tes = fake.date_between(start_date='-22y', end_date='today').strftime('%Y-%m-%d')
        hasil = fake.sentence()
        tempat = laboratorium[random.choice() % len(laboratorium) - 1]
        with connection.cursor() as cursor:
            cursor.execute(f"INSERT INTO TesLab (id_medical_records, tanggal_tes, hasil, tempat) VALUES ('{id_medical_records}', '{tanggal_tes}', '{hasil}', '{tempat}')")