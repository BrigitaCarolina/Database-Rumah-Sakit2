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
        FOREIGN KEY (id_pasien) REFERENCES MedicalRecord(id_pasien),
        FOREIGN KEY (id_kerja_sama) REFERENCES MedicalRecord(id_kerja_sama),
    );
    """
    with connection.cursor() as cursor:
        cursor.execute(create_table_query)

def input_data_detail_records(connection, fake):
    cursor = connection.cursor()
    cursor.execute("SELECT id, id_pasien, id_kerja_sama from MedicalRecord")
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
        biaya = random.randint(a, b)(10, 1000)
        with connection.cursor() as cursor:
            cursor.execute(f"INSERT INTO DetailRecords (id_pasien, id_kerja_sama, tanggal_masuk, tanggal_keluar, diagnosis, biaya) VALUES ('{id_pasien}', '{id_kerja_sama}', '{checkin_date}', '{checkout_date}', '{diagnosis}', {biaya})")
