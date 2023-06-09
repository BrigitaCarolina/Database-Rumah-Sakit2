import random
from datetime import datetime, timedelta

def create_detail_records(connection):
    create_table_query = """
    CREATE TABLE IF NOT EXISTS DetailRecords (
        id_pasien           int NOT NULL,
        id_kerja_sama       int NOT NULL,
        tanggal_masuk       date NOT NULL,
        tanggal_keluar      date NOT NULL,
        diagnosis           varchar(255) NOT NULL,
        biaya               int NOT NULL,
        PRIMARY KEY (id_pasien, id_kerja_sama),
        FOREIGN KEY (id_pasien) REFERENCES Pasien(id),
        FOREIGN KEY (id_kerja_sama) REFERENCES SatuanTugas(id_kerja_sama)
    );
    """
    with connection.cursor() as cursor:
        cursor.execute(create_table_query)

def input_data_detail_records(connection, fake):
    cursor = connection.cursor()
    cursor.execute("SELECT id, id_pasien, id_kerja_sama from MedicalRecord w")
    PK = cursor.fetchall()
    x = len(PK)

    min_checkin_date = datetime.strptime('2023-05-01', '%Y-%m-%d')
    max_checkin_date = datetime.strptime('2023-12-31', '%Y-%m-%d')
    min_length_of_stay = 1
    max_length_of_stay = 14

    for i in range(x): # harusnya sama dengan banyaknya data di MedicalRecord (semoga)
        id_pasien     = PK[i]['id_pasien']
        id_kerja_sama = PK[i]['id_kerja_sama']
        checkin_date = fake.date_between(min_checkin_date, max_checkin_date)
        length_of_stay = random.randint(min_length_of_stay, max_length_of_stay)
        checkout_date = checkin_date + timedelta(days=length_of_stay)
        diagnosis = fake.sentence()
        
        # sum biaya from resep, teslab, and prosedur with the same id_medical_records
        biaya = 0
        cursor.execute(f"SELECT id from medicalrecord where id_pasien = {id_pasien} and id_kerja_sama = {id_kerja_sama}")
        id_medical_records = cursor.fetchone()['id']
        cursor.execute(f"SELECT biaya FROM Resep WHERE id_medical_records = {id_medical_records}")
        biaya += sum([row['biaya'] for row in cursor.fetchall()])
        cursor.execute(f"SELECT biaya FROM TesLab WHERE id_medical_records = {id_medical_records}")
        biaya += sum([row['biaya'] for row in cursor.fetchall()])
        cursor.execute(f"SELECT biaya FROM Prosedur WHERE id_medical_records = {id_medical_records}")
        biaya += sum([row['biaya'] for row in cursor.fetchall()])

        cursor.execute(f"INSERT INTO DetailRecords (id_pasien, id_kerja_sama, tanggal_masuk, tanggal_keluar, diagnosis, biaya) VALUES ('{id_pasien}', '{id_kerja_sama}', '{checkin_date}', '{checkout_date}', '{diagnosis}', {biaya})")
        connection.commit()
