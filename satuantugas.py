import random

def create_satuantugas(connection):
    create_table_query = """
    CREATE TABLE SatuanTugas (
        id_kerja_sama       int,
        nomor_lisensi       varchar(25),
        PRIMARY KEY (id_kerja_sama, nomor_lisensi),
        FOREIGN KEY (nomor_lisensi) REFERENCES TenagaMedis(nomor_lisensi)
    );
    """
    with connection.cursor() as cursor:
        cursor.execute(create_table_query)

def input_data_satuan_tugas(connection):
    with connection.cursor() as cursor:
        cursor.execute("SELECT nomor_lisensi FROM Dokter")
        nomor_lisensi_dokter_list = cursor.fetchall()
        cursor.execute("SELECT nomor_lisensi FROM Perawat")
        nomor_lisensi_perawat_list = cursor.fetchall()
        cursor.execute("SELECT id FROM KerjaSama")
        id_kerja_sama_list = cursor.fetchall()
    x = len(id_kerja_sama_list)
    for i in range(x):
        num_doc = random.randint(1, 3)
        num_nur = random.randint(1, 3)
        doc_list = random.sample(nomor_lisensi_dokter_list, num_doc)
        nur_list = random.sample(nomor_lisensi_perawat_list, num_nur)
        for doc in doc_list:
            with connection.cursor() as cursor:
                sql = "INSERT INTO SatuanTugas VALUES (%s, %s)"
                cursor.execute(sql, (id_kerja_sama_list[i]['id'], doc['nomor_lisensi']))
        for nur in nur_list:
            with connection.cursor() as cursor:
                sql = "INSERT INTO SatuanTugas VALUES (%s, %s)"
                cursor.execute(sql, (id_kerja_sama_list[i]['id'], nur['nomor_lisensi']))
        connection.commit()