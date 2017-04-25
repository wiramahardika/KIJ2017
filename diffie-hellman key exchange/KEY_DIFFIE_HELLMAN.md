Kelompok F-13
I Putu Eka Wira Mahardika		5114100025
Wida Dwitiayasa					5114100155

# Pendahuluan #

Dalam perjalanan anda untuk membangun suatu system keamanan jarinagan, salah satu prosesnya adalah menilai resiko keamanan dalam organisasi anda. Akan tetapi terlebih dahulu anda perlu juga memahami berbagai jenis ancaman keamanan jaringan.

Salah satu metode yang umum dipakai untuk melakukan serangan terhadap keamanan infrastruktur jaringan anda adalah metode 'Sniffer'.

Dalam melakukan eksekusi ancaman Sniffer ini, banyak tool yang dapat digunakan yaitu salah satunya adalah aplikasi Wireshark. 

Akan tetapi telah banyak juga metode yang dikembangkan guna melakukan antisipasi ancaman Sniffer seperti menggunakan enkripsi dekripsi dalam setiap proses pengiriman pesan. 

Menurut definisi secara umum, enkripsi adalah proses mengubah pesan yang dapat dibaca dan dimengerti maknanya menjadi bentuk pesan yang tersandi dan tidak dapat dimengerti maknanya oleh pihak lain. Sedangkan dekripsi adalah proses mengembalikan pesan terssandi menjadi pesan yang dimengerti maknanya oleh pihak penerima informasi (Rindaldi Munir, 2004).

Penjelasan metode enkripsi-dekripsi menggunakan DES-OFD telah dijelaskan pada dokumentasi sebelumnya yang dapat diakses pada link berikut :
https://github.com/wiramahardika/KIJ2017/blob/master/DES_OFB.md

Kemudian, penjelasan metode enkripsi dekripsi menggunakan DES-OFD yang diimplementasikan dalam algoritma sender-receiver juga telah dijelaskan pada dokumentasi sebelumnya yang dapat diakses pada link berikut :
https://github.com/wiramahardika/KIJ2017/blob/master/encrypted_chat/encrypted_chat.md

Penggunaan enkripsi dekripsi dalam seni komunikasi telah digunakan oleh Bangsa Sparta sejak 400 SM (Thomas Kelly, 1998) dan hingga saat ini, penggunaan enkripsi dekripsi sudah mengalami perkembangan yang cukup pesat dan digunakan di berbagai macam aspek kehidupan kita sehari-hari seperti transaksi internet banking dan verifikasi akun email (Scheiner, 2007)

Berdasarkan kunci/key, metode enkripsi dekripsi dalam kriptografi dibagi menjadi dua tipe yaitu metode dengan kunci simetris dan metode dengan kunci asimetris. Pada metode dengan kunci simetris menggunakan satu kunci rahasia yang sama-sama digunakan untuk proses enkripsi dan dekripsi. Sedangkan metode dengan kunci asimetris menggunakan kunci yang berbeda yaitu satu public key yang digunakan oleh pengirim untuk melakukan enkripsi dan satu private key yang digunakan untuk melakukan dekripsi (William Stallings, 2005).

![alt tag](https://raw.githubusercontent.com/wiramahardika/KIJ2017/0202991bba7405026d7d00847504694781bfe0fd/diffie-hellman%20key%20exchange/img/2.png)

![alt tag](https://raw.githubusercontent.com/wiramahardika/KIJ2017/0202991bba7405026d7d00847504694781bfe0fd/diffie-hellman%20key%20exchange/img/3.png)

Jika pada dokumentasi sebelumnya penulis menggunakan kunci simetris, pada kesempatan kali ini penulis akan menggunakan kunci asimetris dalam penerapan enkripsi dekripsi menggunakan metode DES-OFD dengan algoritma sender-receiver seperti yang telah disebutkan sebelumnya. Karena pada penerapannya, penulis menemukan kelemahan dalam penggunaan kunci simetris yaitu kunci yang digunakan tidak bersifat dinamis sehingga memerlukan proses hard-code dalam menentukan key yang digunakan. 

Terdapat beberapa contoh proses enkripsi dekripsi yang menggunakan public key atau kunci asimetris yaitu Diffie-Hellman, ElGamal, Cramer-Shoup, Elliptic Curve dan DSS (William Stallings, 2005). Maka pada dokumentasi ini, akan diterapkan algoritma Diffie-Hellman dalam menentukan nilai key.


# Landasan Teori #

## Sniffer ##

Sniffer merupakan suatu serangan keamanan jaringan dalam bentuk Sniffer (atau dikenal sebagai snooping attack) merupakan kegiatan user perusak yang ingin mendapatkan informasi tentang jaringana atau traffic lewat jaringan tersebut. Suatu Sniffer merupakan program penangkap paket yang dapat menduplikasikan isi paket yang lewat melalui media jaringan kedalam file. Serangan Sniffer sering difokuskan pada koneksi awal antara client dan server untuk mendapatkan login credensial, kunci rahasia, password dan lainnya.

## Wireshark ##

Network Protocol Analyzer Wireshark adalah salah satu dari sekian banyak tool Network Analyzer yang banyak digunakan oleh Network administrator untuk menganalisa kinerja jaringannya. Wireshark banyak disukai karena interfacenya yang menggunakan Graphical User Interface (GUI) atau tampilan grafis.

Seperti namanya, Wireshark mampu menangkap paket-paket data/informasi yang melintas di jaringan yang kita "intip". Semua jenis paket informasi dalam berbagai format protokol pun akan dengan mudah ditangkap dan dianalisa. Karenanya tak jarang tool ini juga dapat dipakai sniffing (seperti yang dijelaskan diatas) dengan menangkap paket-paket yang melintas di dalam jaringan dan menganalisanya.

Untuk menggunakan tool ini pun cukup mudah. Kita cukup memasukkan perintah untuk mendapatkan informasi yang ingin kita capture (yang ingin diperoleh) dari jaringan kita.

## Kriptografi ##

Kriptografi adalah ilmu yang mempelajari tentang kerahasiaan pesan. (Schneier, 2007). Dalam kriptografi, enkripsi adalah suatu proses transformasi pesan/informasi (plaintext) dengan menggunakan suatu kunci, agar tidak dapat terbaca oleh siapapun kecuali mereka yang memiliki kunci tersebut. Pesan yang sudah dienkripsi ini disebut juga ciphertext, sedangkan dekripsi adalah proses mengembalikan chipertext menjadi plaintext awal (Rinaldi Munir, 2004)

![alt tag](https://raw.githubusercontent.com/wiramahardika/KIJ2017/0202991bba7405026d7d00847504694781bfe0fd/diffie-hellman%20key%20exchange/img/1.png)

## Algoritma Diffie-Hellman ##

Algoritma Diffie-Hellman adalah algoritma yang menggunakan public-key dalam proses pembentukkan kunci rahasia. Untuk mendapatkan kunci rahasia harus melalui beberapa tahap yang di dalamnya terjadi kesepakatan kunci yang dikenal dengan kespakatan kunci Diffie-Hellman. Nama algoritma ini diambil dari Martin E. Hellman dan Bailey W. Diffie yang merupakan penemu dari algoritma Diffie-Hellman pada tahun 1976. Tujuan dari algoritma ini adalah supaya kedua pihak dapat melakukan kesepakatan kunci yang hasilnya nanti dapat digunakan dalam proses enkripsi / dekripsi pesan yang dikirim maupun diterima. (William Stallings, 2005)


# Implementasi #

Misalkan terdapat dua orang yang berkomunikasi sebut saja user1 (Alice) dan user2 (Bob)

![alt tag](https://raw.githubusercontent.com/wiramahardika/KIJ2017/0202991bba7405026d7d00847504694781bfe0fd/diffie-hellman%20key%20exchange/img/4.png)

1. Mula-mula user1 dan user2 menyepakati bilangan prima yang besar dan didefinisikan sebagai variabel 'n' dan bilangan prima kecil sebagai variabel 'g', demikian sehingga didapatkan bahwa g<n. Bilangan n dan g tidak perlu rahasia

![alt tag](https://raw.githubusercontent.com/wiramahardika/KIJ2017/0202991bba7405026d7d00847504694781bfe0fd/diffie-hellman%20key%20exchange/img/5.png)

![alt tag](https://raw.githubusercontent.com/wiramahardika/KIJ2017/0202991bba7405026d7d00847504694781bfe0fd/diffie-hellman%20key%20exchange/img/6.png)

![alt tag](https://raw.githubusercontent.com/wiramahardika/KIJ2017/0202991bba7405026d7d00847504694781bfe0fd/diffie-hellman%20key%20exchange/img/7.png)

2. User1 membangkitkan bilangan bulat acak yang besar sebagai variabel random_prime dan mengirim hasil perhitungan berikut kepada user2 sebagai public_key:

![alt tag](https://raw.githubusercontent.com/wiramahardika/KIJ2017/0202991bba7405026d7d00847504694781bfe0fd/diffie-hellman%20key%20exchange/img/8.png)

![alt tag](https://raw.githubusercontent.com/wiramahardika/KIJ2017/0202991bba7405026d7d00847504694781bfe0fd/diffie-hellman%20key%20exchange/img/9.png)

![alt tag](https://raw.githubusercontent.com/wiramahardika/KIJ2017/0202991bba7405026d7d00847504694781bfe0fd/diffie-hellman%20key%20exchange/img/10.png)

3. User2 membangkitkan bilangan bulat acak yang besar random_prime dan mengirim hasil perhitungan berikut kepada user1 sebagai public_key :

![alt tag](https://raw.githubusercontent.com/wiramahardika/KIJ2017/0202991bba7405026d7d00847504694781bfe0fd/diffie-hellman%20key%20exchange/img/13.png)

![alt tag](https://raw.githubusercontent.com/wiramahardika/KIJ2017/0202991bba7405026d7d00847504694781bfe0fd/diffie-hellman%20key%20exchange/img/14.png)

![alt tag](https://raw.githubusercontent.com/wiramahardika/KIJ2017/0202991bba7405026d7d00847504694781bfe0fd/diffie-hellman%20key%20exchange/img/15.png)

4. User1 menghitung private_key dengan perhitungan sebagai berikut :

![alt tag](https://raw.githubusercontent.com/wiramahardika/KIJ2017/0202991bba7405026d7d00847504694781bfe0fd/diffie-hellman%20key%20exchange/img/11.png)

![alt tag](https://raw.githubusercontent.com/wiramahardika/KIJ2017/0202991bba7405026d7d00847504694781bfe0fd/diffie-hellman%20key%20exchange/img/12.png)

5. User2 menghitung private_key dengan perhitungan sebagai berikut :

![alt tag](https://raw.githubusercontent.com/wiramahardika/KIJ2017/0202991bba7405026d7d00847504694781bfe0fd/diffie-hellman%20key%20exchange/img/16.png)

![alt tag](https://raw.githubusercontent.com/wiramahardika/KIJ2017/0202991bba7405026d7d00847504694781bfe0fd/diffie-hellman%20key%20exchange/img/17.png)

Jika perhitungan dilakukan dengan benar maka seharusnya private key yang dihasilkan user1 dan user2 adalah sama. 
Pihak ketiga (Eve) yang ingin menyadap pembicaraan antara user1 (Alice) dan user2 (Bob) tidak dapat menghitung private key. Ia hanya memiliki informasi n,g, dan public key masing-masing user. Tetapi ia tidak mempunyai informasi random_prime user1 dan user2. Untuk mengetahui nilai random_prime, ia perlu melakukan perhitungan algoritma diskrit yang mana sangat sulit untuk dikerjakan.

![alt tag](https://raw.githubusercontent.com/wiramahardika/KIJ2017/0202991bba7405026d7d00847504694781bfe0fd/diffie-hellman%20key%20exchange/img/18.png)

Keterangan :
x : random_prime user1
y : random_prime user2
X : public key user1
Y : public key user2
K : private key user1
K' : private key user2


# Referensi #

https://www.slideshare.net/KuliahKita/kriptografi-algoritma-diffie-hellman

http://lib.ui.ac.id/file?file=digital/20296251-S1738-Merysa%20Amanda.pdf

https://github.com/wiramahardika/KIJ2017/blob/master/DES_OFB.md

https://github.com/wiramahardika/KIJ2017/blob/master/encrypted_chat/encrypted_chat.md