import random
from datetime import datetime, timedelta

def create_medical_records(connection):
    create_table_query = """
    CREATE TABLE IF NOT EXISTS MedicalRecord (
        id                  int auto_increment,
        id_pasien           int NOT NULL,
        id_kerja_sama       int NOT NULL,
        tanggal_masuk       date NOT NULL,
        tanggal_keluar      date NOT NULL,
        diagnosis           varchar(255) NOT NULL,
        biaya               int NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY (id_pasien) REFERENCES Orang(id)
    );
    """
    with connection.cursor() as cursor:
        cursor.execute(create_table_query)

def input_data_medical_records(connection, fake):
    cursor = connection.cursor()
    cursor.execute("SELECT id FROM Pasien")
    PasienID = cursor.fetchall()
    x = len(PasienID)

    min_checkin_date = datetime.strptime('2023-05-01', '%Y-%m-%d')
    max_checkin_date = datetime.strptime('2023-12-31', '%Y-%m-%d')
    min_length_of_stay = 1
    max_length_of_stay = 14
    
    for i in range(x):
        id_pasien = PasienID[i]['id']
        id_kerja_sama = i+1
        # tanggal_masuk = fake.date_between(start_date='-22y', end_date='today').strftime('%Y-%m-%d') # date masih salah karena tanggal keluar harus > tanggal masuk 
        # tanggal_keluar = fake.date_between(start_date='-22y', end_date='today').strftime('%Y-%m-%d')
        
        # Generate a random check-in date
        checkin_date = fake.date_between(min_checkin_date, max_checkin_date)
        # Generate a random length of stay
        length_of_stay = random.randint(min_length_of_stay, max_length_of_stay)
        # Calculate the check-out date
        checkout_date = checkin_date + timedelta(days=length_of_stay)
        diagnosis = fake.sentence()
        biaya = fake.pydecimal(left_digits=3, right_digits=2, positive=True, min_value=10)
        with connection.cursor() as cursor:
            cursor.execute(f"INSERT INTO MedicalRecord (id_pasien, id_kerja_sama, tanggal_masuk, tanggal_keluar, diagnosis, biaya) VALUES ('{id_pasien}', '{id_kerja_sama}', '{checkin_date}', '{checkout_date}', '{diagnosis}', {biaya})")

    for i in range(50):
        # Generate a random check-in date
        checkin_date = fake.date_between(min_checkin_date, max_checkin_date)
        # Generate a random length of stay
        length_of_stay = random.randint(min_length_of_stay, max_length_of_stay)
        # Calculate the check-out date
        checkout_date = checkin_date + timedelta(days=length_of_stay)
        id_pasien = PasienID[random.randint(0, len(PasienID) -1)]['id']
        id_kerja_sama = x+i+1
        diagnosis = fake.sentence()
        biaya = fake.pydecimal(left_digits=3, right_digits=2, positive=True, min_value=10)
        with connection.cursor() as cursor:
            cursor.execute(f"INSERT INTO MedicalRecord (id_pasien, id_kerja_sama, tanggal_masuk, tanggal_keluar, diagnosis, biaya) VALUES ('{id_pasien}', '{id_kerja_sama}', '{checkin_date}', '{checkout_date}', '{diagnosis}', {biaya})")


