# Ancaman Keamanan Jaringan #

Dalam perjalanan anda untuk membangun suatu system keamanan jarinagan, salah satu prosesnya adalah menilai resiko keamanan dalam organisasi anda. Akan tetapi terlebih dahulu anda perlu juga memahami berbagai jenis ancaman keamanan jaringan.

Salah satu metode yang umum dipakai untuk melakukan serangan terhadap keamanan infrastruktur jaringan anda adalah metode 'Sniffer'.

## Sniffer ##

Suatu serangan keamanan jaringan dalam bentuk Sniffer (atau dikenal sebagai snooping attack) merupakan kegiatan user perusak yang ingin mendapatkan informasi tentang jaringana atau traffic lewat jaringan tersebut. Suatu Sniffer merupakan program penangkap paket yang dapat menduplikasikan isi paket yang lewat melalui media jaringan kedalam file. Serangan Sniffer sering difokuskan pada koneksi awal antara client dan server untuk mendapatkan login credensial, kunci rahasia, password dan lainnya.

# Analisa Jaringan Menggunakan WireShark #

Wireshark - Network Protocol Analyzer Wireshark adalah salah satu dari sekian banyak tool Network Analyzer yang banyak digunakan oleh Network administrator untuk menganalisa kinerja jaringannya. Wireshark banyak disukai karena interfacenya yang menggunakan Graphical User Interface (GUI) atau tampilan grafis.

Seperti namanya, Wireshark mampu menangkap paket-paket data/informasi yang melintas di jaringan yang kita "intip". Semua jenis paket informasi dalam berbagai format protokol pun akan dengan mudah ditangkap dan dianalisa. Karenanya tak jarang tool ini juga dapat dipakai sniffing (seperti yang dijelaskan diatas) dengan menangkap paket-paket yang melintas di dalam jaringan dan menganalisanya.

Untuk menggunakan tool ini pun cukup mudah. Kita cukup memasukkan perintah untuk mendapatkan informasi yang ingin kita capture (yang ingin diperoleh) dari jaringan kita.

# Antisipasi Sniffer Menggunakan Metode DES #

Salah satu langkah yang dilakukan oleh programmer untuk mengantisipasi  serangan seperti Sniffer adalah dengan menggunakan metode enkripsi-dekripsi pada paket-paket data yang akan dikirim melalui perantara jaringan sehingga hanya alamat yang ditunjuk sebagai penerima lah yang mendapatkan informasi dari pengirim.

Penjelasan metode enkripsi-dekripsi menggunakan DES-OFD telah dijelaskan pada dokumentasi sebelumnya yang dapat diakses pada link berikut :
https://github.com/wiramahardika/KIJ2017/blob/master/DES_OFB.md

# Implementasi #
Pada penjelasan kali ini, akan dianalogikan menggunakan algoritma sender-receiver sederhana yaitu keduanya akan saling berkomunikasi dengan kerahasiaan informasi yang terjaga (tidak terbaca oleh tool Network Analyzer seperti Wireshark) dan diharapkan data yang sampai pada receiver dan sender tetap sama.

Langkah-langkah dalam implementasi algoritma sender-receiver :

1. Sender membuat socket yang isinya adalah host (IP) dan port (Berupa angka bebas yang didefinisikan oleh sender, biasanya terdiri dari 4 digit). Yang selanjutnya sender akan memebritahukan socketnya kepada receiver yang ia pilih.

![alt tag](https://github.com/wiramahardika/KIJ2017/blob/master/encrypted_chat/img/1.png?raw=true)

2. Receiver melakukan input socket yang diberikan oleh sender sehingga receiver dapat memiliki kunci untuk masuk kedalam socket sender.

![alt tag](https://github.com/wiramahardika/KIJ2017/blob/master/encrypted_chat/img/2.png?raw=true)

3. Receiver mengirim permintaan untuk terhubung kepada sender.

![alt tag](https://github.com/wiramahardika/KIJ2017/blob/master/encrypted_chat/img/3.png?raw=true)

4. Kali ini sender diatur agar hanya dapat menerima maksimal 5 receiver dalam waktu yang bersamaan. Setelah ia mendapati adanya receiver yang meminta permintaan dan memiliki kunci akses yang tepat, maka sender akan menerima permintaan receiver.

![alt tag](https://github.com/wiramahardika/KIJ2017/blob/master/encrypted_chat/img/4.png?raw=true)

5. Kemudian sender akan mengirimkan informasi (berupa chat) kepada receiver berupa hasil enkripsi dari informasi tersebut (menggunakan metode DES-OFD)

6. Selanjutnya receiver akan menerima kiriman dari sender masih berupa hasil enkripsi informasi yang selanjutnya akan didekripsi oleh receiver menggunakan metode yang sama yaitu DES-OFD.

7. Selesai. Receiver akan menerima informasi yang sama dengan apa yang dikirimkan oleh sender tetapi informasi tersebut tidak dapat terbaca (encypted) menggunakan tools Network Analyzer seperti Wireshark.

# Run Program #

1. Sender 

![alt tag](https://github.com/wiramahardika/KIJ2017/blob/master/encrypted_chat/img/5.png?raw=true)

2. Wireshark

![alt tag](https://github.com/wiramahardika/KIJ2017/blob/master/encrypted_chat/img/6.PNG?raw=true)

3. Receiver

![alt tag](https://github.com/wiramahardika/KIJ2017/blob/master/encrypted_chat/img/7.PNG?raw=true)

# Referensi #

[https://sriherlina9.wordpress.com/2013/04/26/analisis-jaringan-menggunakan-wireshark/]
(https://sriherlina9.wordpress.com/2013/04/26/analisis-jaringan-menggunakan-wireshark/)

[http://www.jaringan-komputer.cv-sysneta.com/ancaman-keamanan-jaringan]
(http://www.jaringan-komputer.cv-sysneta.com/ancaman-keamanan-jaringan)

[https://www.tutorialspoint.com/python/python_networking.html]
(https://www.tutorialspoint.com/python/python_networking.htm)

## Terimakasih, semoga bermanfaat ! ##
