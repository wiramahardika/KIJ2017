TUGAS 1 - IMPLEMENTASI ALGORITMA DES DENGAN MENGGUNAKAN METODE CBC

Kelompok F13 :
  I Putu Eka Wira Mahardika (5114100025)
  Wida Dwitiayasa           (5114100155)
  
PENDAHULUAN

Salah satu hal yang penting dalam komunikasi menggunakan computer untuk menjamin kerahasiaan data adalah enkripsi. Enkripsi adalah sebuah proses yang melakukan perubahan sebuah kode dari yang bisa dimengerti menjadi sebuah kode yang tidak bisa dimengerti (tidak terbaca). Enkripsi dapat diartikan sebagai kode atau chiper. Sebuah sistem pengkodean menggunakan suatu table atau kamus yang telah didefinisikan untuk mengganti kata dari informasi atau yang merupakan bagian dari informasi yang dikirim. Sebuah chiper menggunakan suatu algoritma yang dapat mengkodekan semua aliran data (stream) bit dari sebuah pesan menjadi cryptogram yang tidak dimengerti. Karena teknik chiper merupakan suaru sistem yang telah siap untuk di automasi, maka teknik ini digunakan dalam sistem keamanan komputer dan network. 

DASAR TEORI

DES
DES (Data Encryption Standard) adalah algoritma cipher blok yang populer karena dijadikan standard algoritme enkripsi kunci-simetri, meskipun saat ini DES telah dianggap tidak aman lagi. DES termasuk ke dalam sistem kriptografi simetri dan tergolong jenis chiperblok. DES beroperasi pada ukuran blok 64 bit. DES mengenkripsikan 64 bit plaintext menjadi 64 bit ciphertext menggunakan 56 bit kunci internal (internal key) atau subkey. Kunci internal dibangkitkan dari kunci eksternal yang panjangnya 64 bit.

OFB
Mode OFB hampir mirip dengan mode CFB, hanya saja input dari metode enkripsinya adalah input key dan nilai initial vector yang merupakan hasil enkripsi dari proses sebelumnya. 

IMPLEMENTASI

Langkah-langkah dalam implementasi algoritma DES menggunakan metode OFD adalah sebagai berikut:

MODE ENKRIPSI

[!alt tag](https://github.com/wiramahardika/KIJ2017/commit/be9bb69d19a087a829398638e78c434a91b54053)

1. Meminta input plaintext
2. Meminta input key
3. Ubah input plaintext menjadi binary
4. Ubah input key menjadi binary
5. Inisialisasikan nilai initial vector (iv)
6. Melakukan enkripsi menggunakan algoritma DES per block (per 8 bit)
    6.1 Pertama-tama ambil 8 bit pertama dari plain text untuk diproses
    6.2 Kemudian masuk ke dalam fungsi encrypt yang memiliki argumen berupa initial vector dan binary dari input key nya (selanjutnya disebut key_bin)
        6.2.1 Lakukan teknik operasi permutasi antara tabel ip_table dengan binary dari initial vector
        6.2.2 Bagi 2 string biner yang terbentuk dari tahap 6.2.1 [50:50]
        6.2.3 Lakukan juga teknik operasi permutasi antara tabel pc_1_table dengan key_bin
        6.2.4 Bagi 2 string biner yang terbentuk dari tahap 6.2.3 [50:50]
        6.2.5 Lakukan teknik operasi left shift antara tabel left_shift dengan masing-masing hasil string dari tahap 6.2.4
        6.2.6 Gabungkan kembali setiap hasil iterasi dari 6.2.5
        6.2.7 Lakuan teknik operasi permutasi antara tabel pc_2_table dengan masing-masing hasil dari tahap 6.2.6
        6.2.8 Lakukan teknik operasi permutasi kembali antara tabel e_table dengan masing-masing hasil pembagian kedua dari tahap 6.2.2
        6.2.9 Lakukan teknik operasi XOR antara hasil dari 6.2.7 dengan hasil dari tahap 6.2.8
        6.2.10 Lakukan teknik operasi s-box terhadap hasil dari 6.2.9 dengan tabel S1_table
        6.2.11 Kemudian lakukan permutasi kembali antara tabel p_box_table dengan hasil dari tahap 6.2.10
        6.2.12 Lakukan teknik operasi XOR antara hasil dari tahap 6.2.11 dengan masing-masing hasil pembagian pertama dari tahap 6.2.2
        6.2.13 Ubah nilai hasil pembagian pertama pada tahap 6.2.2 menjadi hasil pembagian kedua pada tahap 6.2.2
        6.2.14 Ubah nilai hasil pembagian kedua pada tahap 6.2.2 menjadi hasil dari tahap 6.2.12
        6.2.15 Gabungkan kembali masing-masing hasil tahap 6.2.13 dengan masing-masing hasil tahap 6.2.14 sesuai indeksnya
        6.2.16 Lakukan teknik operasi antara tabel ip_inverse_table dengan hasil dari tahap 6.2.15
        6.2.17 Proses enkripsi pun sudah selesai, lakukan kembali mulai dari tahap 6.2.1 pada 8 bit binary plaintext selanjutnya
        6.2.18 Nilai initial vector diganti dengan hasil dari tahap 6.2.17 
    6.3 Masing-masing hasil dari tahap 6.2 digabungkan kembali dan ubah dari binary menjadi heksadesimal
    6.4 Selesai

RUN PROGRAM

[!alt tag](https://github.com/wiramahardika/KIJ2017/commit/be9bb69d19a087a829398638e78c434a91b54053)
    
MODE DEKRIPSI

[!alt tag](https://github.com/wiramahardika/KIJ2017/commit/be9bb69d19a087a829398638e78c434a91b54053)

1. Meminta input chipertext berupa heksadesimal
2. Meminta input key
3. Ubah input chipertext menjadi binary
4. Ubah input key menjadi binary
5. Initialisasikan nilai vector (iv)
6. Melakukan dekripsi menggunakan algoritma DES per block (per 8 bit)
    6.1 Pertama-tama ambil 8 bit pertama dari chipertext untuk diproses
    6.2 Kemudian masuk ke dalam fungsi encrypt yang memiliki argumen berupa initial vector dan binary dari input key nya (selanjutnya disebut key_bin)
        6.2.1 Lakukan teknik operasi permutasi antara tabel ip_table dengan binary dari initial vector
        6.2.2 Bagi 2 string biner yang terbentuk dari tahap 6.2.1 [50:50]
        6.2.3 Lakukan juga teknik operasi permutasi antara tabel pc_1_table dengan key_bin
        6.2.4 Bagi 2 string biner yang terbentuk dari tahap 6.2.3 [50:50]
        6.2.5 Lakukan teknik operasi left shift antara tabel left_shift dengan masing-masing hasil string dari tahap 6.2.4
        6.2.6 Gabungkan kembali setiap hasil iterasi dari 6.2.5
        6.2.7 Lakuan teknik operasi permutasi antara tabel pc_2_table dengan masing-masing hasil dari tahap 6.2.6
        6.2.8 Lakukan teknik operasi permutasi kembali antara tabel e_table dengan masing-masing hasil pembagian kedua dari tahap 6.2.2
        6.2.9 Lakukan teknik operasi XOR antara hasil dari 6.2.7 dengan hasil dari tahap 6.2.8
        6.2.10 Lakukan teknik operasi s-box terhadap hasil dari 6.2.9 dengan tabel S1_table
        6.2.11 Kemudian lakukan permutasi kembali antara tabel p_box_table dengan hasil dari tahap 6.2.10
        6.2.12 Lakukan teknik operasi XOR antara hasil dari tahap 6.2.11 dengan masing-masing hasil pembagian pertama dari tahap 6.2.2
        6.2.13 Ubah nilai hasil pembagian pertama pada tahap 6.2.2 menjadi hasil pembagian kedua pada tahap 6.2.2
        6.2.14 Ubah nilai hasil pembagian kedua pada tahap 6.2.2 menjadi hasil dari tahap 6.2.12
        6.2.15 Gabungkan kembali masing-masing hasil tahap 6.2.13 dengan masing-masing hasil tahap 6.2.14 sesuai indeksnya
        6.2.16 Lakukan teknik operasi antara tabel ip_inverse_table dengan hasil dari tahap 6.2.15
        6.2.17 Proses enkripsi pun sudah selesai, lakukan kembali mulai dari tahap 6.2.1 pada 8 bit binary chipertext selanjutnya
        6.2.18 Nilai initial vector diganti dengan hasil dari tahap 6.2.17 
    6.3 Masing-masing hasil dari tahap 6.2 digabungkan kembali dan ubah dari binary menjadi char
    6.4 Selesai

RUN PROGRAM

[!alt tag](https://github.com/wiramahardika/KIJ2017/commit/be9bb69d19a087a829398638e78c434a91b54053)


PENJELASAN TEKNIK OPERASI

PERMUTASI
Teknik operasi permutasi adalah teknik merubah urutan input biner menjadi sesuai urutan tabel mutlak/statis yang ditunjuk.
Contoh
    input biner                  1   0   0   1   1
    indeks ke-                  [0] [1] [2] [3] [4]
    urutan indeks tabel statis  [4] [0] [3] [1] [2]
    hasil permutasi              1   0   1   0   0
    
LEFT SHIFT
Teknik operasi left shift adalah teknik pergeseran urutan input biner. Besar/banyak pergeseran ditentukan oleh tabel mutlak/statis yang ditunjuk sesuai iterasinya.
Contoh
    input biner                  1   0   0   1   1
    tabel statis yang ditunjuk  [ 1, 2, 2, 1,..... ]
    hasil iterasi ke-0           0   0   1   1   1      (bergeser 1)
          iterasi ke-1           1   1   1   0   0      (bergeser 2)
          iterasi ke-2           1   0   0   1   1      (bergeser 2)
          dst.
          
XOR
Teknik operasi XOR adalah teknik operasi yang menghasilkan angka biner 0 atau 1. Akan menghasilkan 1 ketika kedua input yang dibandingkan menunjukan angka yang berbeda, berlaku sebaliknya.
Contoh
    input biner                  1   0   0   1   1
    input biner                  1   1   1   0   1
    hasil XOR                    0   1   1   1   0
    
    
S-BOX
Teknik operasi S-BOX adalah teknik operasi yang mengganti nilai input biner menjadi nilai biner pada state yang ditunjuk dari tabel matrix mutlak/statis. Nilai baris yang ditunjuk adalah gabungan biner 1 bit pertama dan 1 bit terakhir input biner. Sisanya menjadi referensi nilai kolom yang akan ditunjuk.
Contoh
    input biner                  1   0   0   1   1  1
    menunjuk baris matriks       1                  1    [11]
    menunjuk kolom matriks           0   0   1   1       [0011]
    matrix[11][0011] = 14 maka input biner = 00001110
    
