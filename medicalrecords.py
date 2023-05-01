import random

def create_medical_records(connection):
    create_table_query = """
    CREATE TABLE IF NOT EXISTS MedicalRecord (
        id                  int auto_increment,
        id_pasien           int NOT NULL,
        id_kerja_sama       int NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY (id_pasien) REFERENCES Pasien(id),
        FOREIGN KEY (id_kerja_sama) REFERENCES SatuanTugas(id_kerja_sama),
    );
    """
    with connection.cursor() as cursor:
        cursor.execute(create_table_query)

def input_data_medical_records(connection, fake):
    cursor = connection.cursor()
    cursor.execute("SELECT id FROM Pasien")
    PasienID = cursor.fetchall()
    x = len(PasienID)
    cursor.execute("SELECT id_kerja_sama FROM SatuanTugas")
    SatuanTugasID = cursor.fetchall()
    y = len(SatuanTugasID)

    for i in range(x):
        id_pasien = PasienID[temp]['id']
        id_kerja_sama = SatuanTugasID[random.randint(0, y-1)]['id_kerja_sama']
        with connection.cursor() as cursor:
            cursor.execute(f"INSERT INTO MedicalRecord (id_pasien, id_kerja_sama) VALUES ('{id_pasien}', '{id_kerja_sama}')")
    
    cursor.execute("SELECT id, id_pasien, id_kerja_sama FROM MedicalRecord")
    current = cursor.fetchall()
    
    for i in range(50):
        id_pasien = PasienID[random.randint(0, x-1)]['id']
        
        # make the id_kerja_sama to be different as previous
        current_id_kerjasama = set()
        for j in range(len(current)):
            if current[j]['id_pasien'] == id_pasien:
                current_id_kerjasama.add(current[j]['id_kerja_sama'])
        id_kerja_sama = SatuanTugasID[random.randint(0, y-1)]['id_kerja_sama']
        while id_kerja_sama in current_id_kerjasama:
            id_kerja_sama = SatuanTugasID[random.randint(0, y-1)]['id_kerja_sama']
        
        with connection.cursor() as cursor:
            cursor.execute(f"INSERT INTO MedicalRecord (id_pasien, id_kerja_sama) VALUES ('{id_pasien}', '{id_kerja_sama}')")