friliani-gloria-footballshop.pbp.cs.ui.ac.id

<details>
<Summary><b>Tugas 1</b></Summary>
1. implementasi
- Saya memulai dengan membuat project Django baru. Diawali dengan 
mengaktifkan environment, kemudian menjalankan django-admin startproject football_shop .
- Kemudian saya membuat aplikasi baru bernama main. Di dalam folder main juga berisi file-file inti seperti models.py, views.py, sub-folder templates, dan lainnya.
- kemudian saya tambahkan main ke INSTALLED-APPS pada settings.py
- selanjutnya saya membuat model Product dan menambahkan atribut wajib (name, price, description, thumbnail, category, is_featured), dengan tipe yang sudah ditentukan juga, pada models.py.
- kemudian saya membuat fungsi pada views.py yang akan dikembalikan ke template html. saya juga menambahkan template html untuk menampilkan data dari view ke browser.
- selanjutnya saya membuat sebuah routing pada urls.py.
- kemudian saya melakukan migrasi database.
- terakhir, saya melakukan deployment ke PWS.


2. ![Django MVT Architecture](images/image-1.png)
alur:
- client mengakses URL
- request masuk ke urls.py project
- Django mencari pola URLnya, kemudian mengarahkan ke fungsi di views.py pada aplikasi.
- fungsi di views.py bisa mengambil atau mengolah data dari models.py
- data dikirim ke template HTML untuk ditampilkan ke user
- django mengembalikan HTTP Response ke browser client


3. peran settings.py
settings.py menyimpan konfigurasi global project, seperti daftar aplikasi, database yang dipakai, templates, dan lainnya. settings.py berisi pengaturan dasar project.


4. cara kerja migrasi database
saat kita ubah models.py, django belum langsung mengubah database. 
python manage.py makemigrations -> membuat file migrasi
python manage.py migrate -> mengeksekusi file miggrasi ke database 
migrasi membuat perubahan database terkontrol.


5. mengapa Django?
karena framework django memiliki banyak fitur bawaan yang sangat berguna, memiliki struktur yang jelas, dan menerapkan standar pengembangan yang rapi, mengajarkan pola pikir clean code apalagi untuk pemula. django juga sudah sangat populer dan memiliki dokumentasi yang cukup lengkap, jadi mudah dipelajari.


6. feedback untuk asdos tutorial 1
so far, saya belum ada feedback apapun untuk asisten dosen karena saya juga belum mengalami banyak masalah dalam pengerjaan tutorial.
</details>


<details>
<Summary><b>Tugas 2</b></Summary>

1. Data delivery dibutuhkan agar bisa ada pertukaran data antar sistem
2. JSON lebih baik dan lebih populer karena formatntya lebih ringkas dan mudah dibaca, juga lebih ringan.
3. is_valid() digunakan untuk validasi data yang dimasukkan user ke dalam form. tanpa itu, aplikasi bisa menerima input yang salah atau mungkin berbahaya.
4. jika tidak ada csrf_token, penyerang bisa membuat form palsu di situs lain yang secara diam-diam mengirim permintaan ke aplikasi kita. dengan csrf_token, Django bisa memastikan request memang berasal dari form milik aplikasi kita, bukan dari pihak luar.
5. saya mengimplementasikan dimulai dari menambahkan fungsi-fungsi views baru, kemudian membuat routing untuk URL untuk masing-masing views, membuat fitur add product, dimana saya membuat tombol add product yang membawa kita ke halaman form, kemudian membuat fitur untuk melihat detail product.
6. tidak ada feedback.

![Postman - XML](images/postman-xml.png)
![Postman - JSON](images/postman-json.png)
![Postman - XML by id](images/postman-xml-by-id.png)
![Postman - JSON by id](images/postman-json-by-id.png)

</details>
