import random
def create_klaim_asuransi(connection):
    create_table_query = """
    CREATE TABLE IF NOT EXISTS KlaimAsuransi (
        id                  int auto_increment,
        tanggalKlaim        date NOT NULL,
        status              varchar(255) NOT NULL,
        id_perusahaan       int NOT NULL,
        id_medical_records  int NOT NULL,
        jumlah              int NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY (id_perusahaan) REFERENCES PerusahaanAsuransi(id),
        FOREIGN KEY (id_medical_records) REFERENCES MedicalRecord(id)
    );
    """
    with connection.cursor() as cursor:
        cursor.execute(create_table_query)

def insert_klaim_asuransi(x, connection, fake):
    #take id_perusahaan and id_medical_records
    with connection.cursor() as cursor:
        cursor.execute("SELECT id FROM PerusahaanAsuransi")
        id_perusahaan_list = cursor.fetchall()
        cursor.execute("SELECT id FROM MedicalRecord")
        id_medical_records_list = cursor.fetchall()
    
    #insert data
    for i in range(x):
        id = i+1
        tanggalKlaim = fake.date_between(start_date='-1y', end_date='today')
        status = fake.random_choices(elements=('Diterima', 'Ditolak'))[0]
        id_perusahaan = fake.random_choices(elements=id_perusahaan_list)[0]['id']
        success = False
        while (not success):
            random_id = random.choice(id_medical_records_list)['id']
            if random_id in [d['id'] for d in id_medical_records_list]:
                id_medical_records_list.remove({'id': random_id})
                success = True
                with connection.cursor() as cursor:
                    cursor.execute("SELECT biaya from detailrecords join medicalrecord on detailrecords.id_pasien = medicalrecord.id_pasien and detailrecords.id_kerja_sama = medicalrecord.id_kerja_sama where medicalrecord.id = %s", (random_id))
                    jumlah = cursor.fetchone()['biaya']
                if jumlah == 0:
                    success = False
        jumlah = random.randint(1, jumlah)
        query = "INSERT INTO KlaimAsuransi VALUES (%s, %s, %s, %s, %s, %s)"
        with connection.cursor() as cursor:
            cursor.execute(query, (id, tanggalKlaim, status, id_perusahaan, random_id, jumlah))
        connection.commit()
