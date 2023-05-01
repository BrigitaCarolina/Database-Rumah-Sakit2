import random

def create_departemen(connection):
    create_table_query = """
    CREATE TABLE Departemen (
        id                  int auto_increment, 
        nama_departemen     varchar(255) NOT NULL,
        PRIMARY KEY (id) 
        FOREIGN KEY (nama_departemen) REFERENCES KepalaDepartemen(namaDepartemen)
    );
    """
    with connection.cursor() as cursor:
        cursor.execute(create_table_query)


def input_departemen(connection, fake):
    cursor = connection.cursor()
    cursor.execute("SELECT nama_departemen FROM KepalaDepartemen")
    namaDepartemen = cursor.fetchall()
    for i in range(x):
        namaDepartemen = namaDepartemen[i]['nama_departemen']
        with connection.cursor() as cursor:
            cursor.execute(f"INSERT INTO departemen (nama_departemen) VALUES ('{namaDepartemen}')")

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
