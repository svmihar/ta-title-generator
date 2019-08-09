# Judul Tugas Akhir Generator
## cara
- pake gpt2 mini
- pake lstm network 

## scraping
mengambil seluruh judul ta dari [sini](http://repository.its.ac.id/view/year/)

## prerequisite
- jangan lupa install pipenc 
- pipenv install
- pipenv shell 
- python scraper.py
    - membuat csv of judul 
- python `generate_rnn.py`
    - ```python 
    model_cfg = {rnn_bidirectional=True,
                rnn_layers=12,
                rnn_size=128,
                dim_embeddings=300,
                num_epochs=1000, gen_epochs=10, batch_size=1024)
    ```
- python 'generator.py` 
    - gpt2 with 1000 iterations

## trained models
- [gpt2](https://drive.google.com/drive/folders/1vLNCp4ZcMxwUL6FXM6NKl5gk3xuD97fR?usp=sharing)
- [bilstm[](https://drive.google.com/drive/folders/1ZS8vqgzinzR91XBYlHj5kNC3zk3nAiHC?usp=sharing)

## hasil 
```bash
Training new model w/ 4-layer, 128-cell Bidirectional LSTMs
Training on 30,680 character sequences.
__________________________________________________________________________________________________
Layer (type)                    Output Shape         Param #     Connected to
==================================================================================================
input (InputLayer)              (None, 40)           0
__________________________________________________________________________________________________
embedding (Embedding)           (None, 40, 300)      18600       input[0][0]
__________________________________________________________________________________________________
rnn_1 (Bidirectional)           (None, 40, 256)      439296      embedding[0][0]
__________________________________________________________________________________________________
rnn_2 (Bidirectional)           (None, 40, 256)      394240      rnn_1[0][0]
__________________________________________________________________________________________________
rnn_3 (Bidirectional)           (None, 40, 256)      394240      rnn_2[0][0]
__________________________________________________________________________________________________
rnn_concat (Concatenate)        (None, 40, 1068)     0           embedding[0][0]
                                                                 rnn_1[0][0]
                                                                 rnn_2[0][0]
                                                                 rnn_3[0][0]
__________________________________________________________________________________________________
attention (AttentionWeightedAve (None, 1068)         1068        rnn_concat[0][0]
__________________________________________________________________________________________________
output (Dense)                  (None, 62)           66278       attention[0][0]
==================================================================================================
Total params: 1,313,722
Trainable params: 1,313,722
Non-trainable params: 0
__________________________________________________________________________________________________

####################
Temperature: 0.2
####################
Analisis Pengambilan Keputusan Terhadap Pemilihan Portofolio Saham Menggunakan Metode Campuran Autoregressive Integrated Moving Average Exogeneous Input Dan Adaptive Neuro Fuzzy ArimaxAnfis Studi Kasus  Instansi Xyz

Penerapan Metode Extended Kalman Filter Untuk Estimasi Transmisi Filariasis

Penerapan Metode Papoulis Untuk Menghitung American Put Option Dengan Dividen

####################
Temperature: 0.5
####################
Penerapan Metode Multiplier Lagrange Untuk Meminimalkan Biaya Persediaan Suku Cadang Dengan Perbedaan Kelas Pelanggan

Pengembangan Perangkat Lunak Deteksi Kecepatan Kendaraan Bergerak Berbasis Pengolahan Citra Digital

Analisis Bifurkasi Hopf Pada Sistem Keuangan Dengan Kontrol Input

####################
Temperature: 1.0
####################
Implementasi Algoritma Genetika Untuk Meminimalkan Biaya Persediaan Produk Sandal

Model ArimaFilter Kalman Untuk Prediksi Harga Komoditas Minyak Mentah

Perbandingan Kinerja Diagram Kontrol Ewma Exponentially Weighted Moving Average Dalam Penentuan Harga American DownAndOut Call Option
```

### menggunakan gpt2 
```bash 
Iteration 976
======== SAMPLE 1 ========
serada Peran Tata Furnace.
Analisis Indikator Perbandingan Kualitas Produk Bagian Jasa Pengiriman Di Lingkungan Kampus Industri Stias.
Optimasi Penjadwalan Staf Rumah Sakit Dengan Menggunakan Algoritma Greedy - Late Purchase - Analysis The Cost Of Working Forger In High School Using Late Purchase Cost.
Studi Penggunaan Empat Pada Proses Bioetanol Fatigue Healing Menggunakan Fatigue Transformation.
Optimasi Tekno-Ekonomi Pada Penggunaan Gedung Bertingkat Asrama Faktor Sinar Mikro, Rusunawa Daerah Dan Indikator Pada Reklamasi Di Surabaya.
Perencanaan Program Greenhouse Cast untuk Direct exchange between Cast and Steam Steam Computers.
Analisis Perencanaan Workshop Repository Managemen Kualitas Cetakan Pada Anak Wisata Digital Dengan Jaringan Utara Internet of Things.
Studi Eksperimen Pengaruh Variasi Debit Pada Jet Set Wenght System Cerdasannya Cerdasannya 4 Kg/Jam - The Effect Of Debit Consumption On The Thickness Of Dry Sand Frame And The Effect Of Crackling Sun At Wenght System Cerdasannya 4 Kg/Hour.
Reduksi Arus Online Tipe Dan Exoskeleton Sedimentasi Untuk Prediksi Bahan Baku Pada Pabrik Gula Nasional 80 Kv/Jam = Potential Hazard And Operability Study (P-SO) Development In The Hazard And Operability Study (HAZOP) Laboratory Environment.
Analisis Kegagalan Keselamatan Dan Kebijakan Perawatan Pada Proyek Interaklinjo Jawa Timur.
Rancang Bangun Mesin Penghubung Bakso Dengan Kapasitor Hibrida Untuk Memperoleh Rugi Daya Berbasis Viewpoint.
Studi Penentuan Aplikasi Ergonomi Pada Kapal Kerugian Tertial Uji Papua Tradisional.
Perencanaan Perkuatan Bendung-Tanah Mutu Loan Program Dengan Menggunakan Metode Renovasi Matic.
Pengaruh Variasi Suhu Dan Stabilitas Enlistering Terhadap Umur Bangunan Perangkat Lunak Dari Sonoc Tokorogo.
Remediasi Tanah Distribusi Bisnis Interaktif: Studi Kasus Kota Denpasar.
Ekstraksi Boundary Integral Method Untuk Monitoring Elektronik Pada Gravitrot Midship Craft 20 Robot Dengan Percobaan.
Analisis Terdukas Kebutuhan Energi Listrik Yang Dihasilkan Mekanisme Epifodic Annularisations Mereduksi Gejestrin Dan Variasi Nirk Bernuan.
Perencanaan Turbin Darriues Blowtoriod Berdasarkan Sistem Multiple Output/Bridge Type Pada Mini Plant 3 Plant 1.
Pengaruh Variasi Arus Pengerinan Terhadap Tegangan Pada Pelapisan Perjugat Terjadi Di Taman Saluran Tanker.
Desain Interior Art Deco Kapal Pada Mini Warung Saga Kapal Katamaran.
Pengelolaan Limbah Plastik T2 Digital Dengan Penambahan Beban Gelombang.
Desain Rantai Pasok Penjalaran Retardasi Body Planing dan Body Structure Examination Pada Rigid Pavement pada Campuran Embankment 2 SMAW.
Analisis Survival Cokeruhan terhadap Stabilitas Tegangan pada Galangan Kapal dalam Pembuluhan 275 dengan Metode SWI-FSC (Studi Kasus : Bandara Internasional Juanda).
Perencanaan Gedung Perkantoran Sasan Menggunakan Fitur Grating-FCM-MSM-SBU Dan Pemasangan GoPros Indom Med Iota.
Pengaruh Meredutif Dan Metode Arus Pada Peramalan Induktor Terhadap Kekerasan dan Persediaan Sebuah Teknis.
Analisa Laju Sedimentasi Akibat Integrasi Gedung Bernuansa Natural Gas Dua Underwater Wet Remote Oceans.
Analisis Pengaruh Variasi Arus Dan Pelarut Gelatin Terhadap Proses Peleburan Direct Reduced Iron (D
```
