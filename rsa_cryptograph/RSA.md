Kelompok 13<br />
- I Putu Eka Wira Mahardika		5114100025<br />
- Wida Dwitiayasa				5114100155


# PENDAHULUAN #

Untuk mengamankan data, salah satu cara dapat diterapkan suatu algoritma kriptografi
untuk melakukan enkripsi. Dengan enkripsi data tidak dapat terbaca karena teks asli atau
plaintext telah diubah ke teks yang tak terbaca atau disebut chipertext. Ada banyak algoritma
kriptografi yang dapat digunakan, berdasarkan sifat kuncinya dibagi menjadi dua yaitu simetris
yang hanya memakai satu kunci rahasia dan asimetris (public key algorithm) yang memakai
sepasang kunci publik dan kunci rahasia.

Jika pada dokumentasi sebelumnya penulis menggunakan kunci asimetris dengan algoritma diffie hellman ( https://github.com/wiramahardika/KIJ2017/blob/master/diffie-hellman%20key%20exchange/KEY_DIFFIE_HELLMAN.md ), pada kesempatan kali ini akan digunakan algoritma RSA. 


# Landasan Teori #

## RSA ##

![alt tag](https://github.com/wiramahardika/KIJ2017/blob/7f77db5a1caca3c2b573a8c4a02f770c72c5cabd/rsa_cryptograph/img/rsa.jpg?raw=true)

RSA Cipher atau kriptografi kunci publik merupakan salah satu kriptografi asimetris, dimana kunci untuk melakukan enkripsi dan dekripsi berbeda. Nama RSA diambil dari inisial orang yang menciptakannya yaitu Ron Rivest, Adi Shamir, dan Leonard Adleman, dan dipublikasikan pada jurnal ilmiah Communication of ACM tahun 1977.

Keamanan algoritma RSA terletak pada tingkat kesulitan dalam aktorisasi pada bilangan yang sangat besar. Pada tahun 2005, bilangan faktorisasi terbesar yang digunakan secara umum ialah sepanjang 663 bit, menggunakan metode distribusi mutakhir. Kunci RSA pada umumnya sepanjang 1024—2048 bit. Beberapa pakar meyakini bahwa kunci 1024-bit ada kemungkinan dipecahkan pada waktu dekat (hal ini masih dalam perdebatan), tetapi tidak ada seorangpun yang berpendapat kunci 2048-bit akan pecah pada masa depan yang terprediksi.
Apabila terdapat faktorisasi metode yang baru dan cepat telah dikembangkan, maka ada kemungkinan untuk membongkar RSA.


# Implementasi #

1. Pertama-tama pilih 2 bilangan acak prima p dan q (p != q), dimana bilangan tersebut dipilih dalam range 255 sampai 1000 agar dapat mewakili kode ASCII. Kedua bilangan ini bersifat rahasia.
![alt tag](https://raw.githubusercontent.com/wiramahardika/KIJ2017/b04e0e816bd66f9c0d30b13cd1581b8934c15203/rsa_cryptograph/img/1.png)
![alt tag](https://raw.githubusercontent.com/wiramahardika/KIJ2017/b04e0e816bd66f9c0d30b13cd1581b8934c15203/rsa_cryptograph/img/2.png)

2. Hitung nilai modulus dengan rumus n = p * q. Nilai n bersifat publik atau tidak rahasia.
![alt tag](https://raw.githubusercontent.com/wiramahardika/KIJ2017/b04e0e816bd66f9c0d30b13cd1581b8934c15203/rsa_cryptograph/img/3.png)

3. Hitung nilai m dengan rumus m = (p-1)*(q-1). Nilai m bersifat rahasia.
![alt tag](https://raw.githubusercontent.com/wiramahardika/KIJ2017/b04e0e816bd66f9c0d30b13cd1581b8934c15203/rsa_cryptograph/img/4.png)

4. Cari nilai e atau eksponen publik dimana nilai ini merupakan bilangan relative prima dari m. Nilai e bersifat publik atau tidak rahasia.
![alt tag](https://raw.githubusercontent.com/wiramahardika/KIJ2017/b04e0e816bd66f9c0d30b13cd1581b8934c15203/rsa_cryptograph/img/5.png)
![alt tag](https://raw.githubusercontent.com/wiramahardika/KIJ2017/b04e0e816bd66f9c0d30b13cd1581b8934c15203/rsa_cryptograph/img/6.png)

5. Cari nilai d atau eksponen pribadi dengan rumus ed ≡ 1 mod m atau d = e-1 mod m. Nilai d bersifat rahasia.
![alt tag](https://raw.githubusercontent.com/wiramahardika/KIJ2017/b04e0e816bd66f9c0d30b13cd1581b8934c15203/rsa_cryptograph/img/7.png)
![alt tag](https://raw.githubusercontent.com/wiramahardika/KIJ2017/b04e0e816bd66f9c0d30b13cd1581b8934c15203/rsa_cryptograph/img/8.png)

6. Kemudian didapatkan 2 buah kunci publik [e dan n] dan 2 buah kunci private [d dan n]. Kunci publik ini yang akan dikirimkan kepada user lain dimana bukan si pembuat kunci, sedangkan kunci private tetap berada di komputer pembuat kunci.
![alt tag](https://raw.githubusercontent.com/wiramahardika/KIJ2017/b04e0e816bd66f9c0d30b13cd1581b8934c15203/rsa_cryptograph/img/9.png)

7. Selanjutnya untuk melakukan enkripsi dekripsi pesan dibutuhkan kunci tambahan menggunakan algoritma DES. Dimana kunci ini bersifat simetris dan disepakati oleh kedua belah pihak. Dengan demikian maka hanya 1 user yang akan membuat kunci kemudian kunci tersebut dikirimkan dalam bentuk hasil enkrispi, sedangkan user yang menerima hasil enkripsi akan melakukan dekripsi kunci sehingga didapatkan satu buah kunci yang sama.
![alt tag](https://raw.githubusercontent.com/wiramahardika/KIJ2017/b04e0e816bd66f9c0d30b13cd1581b8934c15203/rsa_cryptograph/img/11.png)

8. Langkah terakhir akan dilakukan sebuah pengiriman dan penerimaan pesan menggunakan algoritma DES-OFB seperti yang telah dijelaskan pada dokumentasi sebelumnya (https://github.com/wiramahardika/KIJ2017/blob/master/encrypted_chat/encrypted_chat.md) sehingga pesan tidak dapat terbaca melalui beberapa tools Network Analyzer.

# Referensi #

http://octarapribadi.blogspot.co.id/2016/02/enkripsi-dan-dekripsi-menggunakan-rsa.html

http://cyberpiratesss.blogspot.co.id/2015/01/algoritma-rsa-di-java.html

http://fjrarnote.blogspot.co.id/2015/01/pengertian-algoritma-rsa.html

