import random

def create_dokter(connection):
    create_table_query = """
    CREATE TABLE IF NOT EXISTS Dokter (
        id   int,
        spesialisasi    varchar(255) NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY (id) REFERENCES TenagaMedis(id)
    );
    """
    with connection.cursor() as cursor:
        cursor.execute(create_table_query)

def input_data_dokter(x, connection, fake):
    spesialisasi = ["Cardiology", "Dermatology", "Endocrinology", "Gastroenterology", " Hematology", "Infectious Disease", "Nephrology", "Neurology", "Oncology", "Ophthalmology", "Orthopedics", "Pulmonology", "Rheumatology", "Urology"]
    cursor = connection.cursor()
    cursor.execute("SELECT id FROM TenagaMedis")
    lisensiDokter = cursor.fetchall()
    random.shuffle(lisensiDokter)
    for i in range(x):
        lisensiDokterr = lisensiDokter[i]['id'] 
        spesialisasii = spesialisasi[random.randint(0, len(spesialisasi) - 1)]
        with connection.cursor() as cursor:
            cursor.execute(f"INSERT INTO dokter (id, spesialisasi) VALUES ({lisensiDokterr}, '{spesialisasii}')")
