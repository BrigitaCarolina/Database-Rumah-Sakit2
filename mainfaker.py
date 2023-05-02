from faker import Faker
import pymysql
import random
from departemen import *
from dokter import *
from klaimasuransi import *
from kontakdarurat import *
from medicalrecords import *
from orang import *
from pasien import *
from perawat import *
from perusahaan import *
from prosedur import *
from resep import *
from satuantugas import *
from tenagamedis import *
from teslab import *
from kamarpasien import *
from penempatankamar import *
from kelaskapasitaskamar import *
from desakecamatan import *
from kabupatenprovinsi import *
from kecamatankabupatenkota import *
from detailrecords import *
from lisensiTenagaMedis import *
from departemenTenagaMedis import *
from departemen import *
from kepalaDepartemen import *


fake = Faker() 

# Connect to the MySQL database
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='bintang8899',
    db='rumahsakit8',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)
fake = Faker()

create_kabupatenprovinsi(connection)
input_data_kabupatenprovinsi(15, connection, fake)
create_kecamatankabupatenkota(connection)
input_data_kecamatankabupatenkota(75, connection, fake)
create_desakecamatan(connection)
input_data_desa_kecamatan(125, connection, fake)
create_orang(connection)
input_data_orang(300, connection, fake)
# create_departemen(connection)
# input_departemen(connection, fake)
create_kepala_departemen(connection)
input_kepala_departemen(connection, fake)
create_departemen(connection)
input_departemen(connection, fake)
create_lisensi_tenaga_medis(connection)
input_data_lisensi_tenaga_medis(200, connection)
create_dept_tenaga_medis(connection)
input_data_dept_tenaga_medis(connection)
# create_tenagamedis(connection)
# input_data_tenaga_medis(200, connection, fake)
create_dokter(connection)
input_data_dokter(100, connection, fake)
create_perawat(connection)
input_data_perawat(100, connection, fake)
create_pasien(connection)
input_data_pasien(100, connection, fake)
create_kontak_darurat(connection)
insert_kontak_darurat(connection, fake)
create_perusahaan(connection)
input_data_perusahaan(10, connection, fake)
create_satuantugas(connection)
input_data_satuan_tugas(370, connection, fake)
create_medical_records(connection)
input_data_medical_records(connection, fake)
create_resep(connection)
input_data_resep(100, connection, fake)
create_teslab(connection)
input_data_teslab(100, connection, fake)
create_prosedur(connection)
input_data_prosedur(100, connection, fake)
create_detail_records(connection)
input_data_detail_records(connection, fake)
create_kelas_kapasitas_kamar(connection)
input_data_kelas_kapasitas_kamar(connection, fake)
create_penempatan_kamar(connection)
input_data_penempatan_kamar(connection, fake)
# create_kamar_pasien(connection)
# input_data_kamar(connection, fake) 
create_klaim_asuransi(connection)
insert_klaim_asuransi(100, connection, fake)


connection.commit()
connection.close()