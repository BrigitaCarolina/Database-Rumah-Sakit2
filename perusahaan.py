import random

def create_perusahaan(connection):
    create_table_query = """
    CREATE TABLE IF NOT EXISTS PerusahaanAsuransi (
        id int auto_increment,
        nama_perusahaan     varchar(255),
        nama_kontak         varchar(255),
        nomor_telepon       varchar(100),
        PRIMARY KEY (id)   
    );
    """
    with connection.cursor() as cursor:
        cursor.execute(create_table_query)

def input_data_perusahaan(x, connection, fake):
    for i in range (x):
        company = fake.company()
        contact = fake.name()
        pnumber = "08" + "".join([str(random.randint(0,9)) for _ in range(10)])
        print(f"INSERT INTO PerusahaanAsuransi (nama_perusahaan, nama_kontak, nomor_telepon) VALUES ('{company}', '{contact}', '{pnumber}')") 
        with connection.cursor() as cursor:
            cursor.execute(f"INSERT INTO PerusahaanAsuransi (nama_perusahaan, nama_kontak, nomor_telepon) VALUES ('{company}', '{contact}', '{pnumber}')")


