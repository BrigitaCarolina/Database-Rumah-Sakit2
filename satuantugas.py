import random

def create_satuantugas(connection):
    create_table_query = """
    CREATE TABLE SatuanTugas (
        id_kerja_sama       int,
        id       int,
        PRIMARY KEY (id_kerja_sama, id),
        FOREIGN KEY (id) REFERENCES LisensiTenagaMedis(id)
    );
    """
    with connection.cursor() as cursor:
        cursor.execute(create_table_query)

def input_data_satuan_tugas(x, connection, fake):
    with connection.cursor() as cursor:
        cursor.execute("SELECT id FROM Dokter")
        nomor_lisensi_dokter_list = cursor.fetchall()
        cursor.execute("SELECT id FROM Perawat")
        nomor_lisensi_perawat_list = cursor.fetchall()
        id_kerja_sama_list = []
        j = 1
        for i in range(1, 371):
            if (j > 6):
                j %= 6
            id_kerja_sama_list.append(j)
            j += 1
    x = 70
    for i in range(x):
        num_doc = random.randint(1, 3)
        num_nur = random.randint(1, 3)
        doc_list = random.sample(nomor_lisensi_dokter_list, num_doc)
        nur_list = random.sample(nomor_lisensi_perawat_list, num_nur)
        
        for doc in doc_list:
            with connection.cursor() as cursor:
                sql = "INSERT INTO SatuanTugas VALUES (%s, %s)"
                cursor.execute(sql, (i, doc['id']))
        for nur in nur_list:
            with connection.cursor() as cursor:
                sql = "INSERT INTO SatuanTugas VALUES (%s, %s)"
                cursor.execute(sql, (i, nur['id']))