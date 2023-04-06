import random

def create_dokter(connection):
    create_table_query = """
    CREATE TABLE IF NOT EXISTS Dokter (
        nomor_lisensi   varchar(25),
        spesialisasi    varchar(255),
        PRIMARY KEY (nomor_lisensi),
        FOREIGN KEY (nomor_lisensi) REFERENCES TenagaMedis(nomor_lisensi)
    );
    """
    with connection.cursor() as cursor:
        cursor.execute(create_table_query)

def input_data_dokter(x, connection):
    spesialisasi = {"Cardiology", "Dermatology", "Endocrinology", "Gastroenterology", " Hematology", "Infectious Disease", "Nephrology", "Neurology", "Oncology", "Ophthalmology", "Orthopedics", "Pulmonology", "Rheumatology", "Urology"}
    connection.cursor().execute("SELECT nomor_lisensi FROM TenagaMedis")
    lisensiDokter = connection.cursor().fetchall()
    random.shuffle(lisensiDokter)
    for i in range(x):
        lisensiDokterr = lisensiDokter[i]['nomor_lisensi'] 
        spesialisasii = spesialisasi[random.choice % (len(spesialisasi) - 1)]
        with connection.cursor() as cursor:
            cursor.execute(f"INSERT INTO dokter (nomor_lisensi) VALUES ('{lisensiDokterr}', '{spesialisasii}')")
