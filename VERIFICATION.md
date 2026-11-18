# VERIFICATION — news-image-20261118
# "THE WORLD CHRONICLE" — Rabu 18 November 2026
# Disusun: 19 Nov 2026 ~05:30 WIB (koordinator riset, Fase 1)
# STATUS: riset + konsep SAJA. TIDAK ADA SUBMIT (bos: "jangan sub" — typo dikoreksi 05:09 WIB).
# Kerja lanjut: build + push GitHub saja, lalu lapor bos.

---

## 1. FAKTA KIT (dibaca langsung dari kit yang diunduh)

- Kit: `~/workspace/makefun/news-image-20261118-kit/news-image-20261118-kit/`
  (competition.yaml + RULES.txt dibaca seluruhnya; bundle_sha256 d448959a49da725ffc84e5cb6c40f07aeadbfdc756fb846645400d164d165fea)
- Kompetisi: **"Sum up 18 November's world news in one image"** — Rabu 18 November 2026.
- Deadline submit: **20 Nov 2026 07:00 WIB (2026-11-20T00:00:00Z)** — dari listing kompetisi (bukan dari teks yaml).
- Hadiah $250: 1st $50, 2nd $30, 3rd $15, 4th–10th $5, 11th–50th $3. USDC di Solana.
- Batas gambar: **PNG atau JPEG, ≤1 MiB (1.048.576 byte), ≤1024×1024 px**, nama tetap `entry.png`.
  Paket Chronicle melanggar ini: output.png 1600×2360, 1.321.908 byte → HARUS di-resize.
- Program: main.ts (Node 22) atau main.py (Python 3.13) di root repo; **tanpa network**;
  program jalan 2× dan kedua run harus menulis byte yang IDENTIK.
- Kuota: maks 10 submit/hari, 20 total; submit terakhir sebelum deadline = entry final.
- Juri: **z-ai/glm-5.3-flash** (OpenRouter), reasoning effort high, maks 12.100 token/verdict.
  Juri TIDAK punya feed berita dan TIDAK diberi tahu tanggal kompetisi — menilai dari gambar saja
  + pengetahuannya sendiri. House images menunjukkan 13 Nov 2026; entry tentang hari SEBELUM
  13 Nov kalah dari yang tidak.
- Kriteria juri, BERURUTAN (paling penting dulu):
  1. Satu hari berita + MENYEBUT TANGGAL itu: peristiwa spesifik hari itu, dikenali dari gambar.
  2. Seleksi + breadth: cerita paling konsekuensial, lintas wilayah dan bidang.
  3. Terbaca: penonton yang ketinggalan hari itu bisa tahu apa yang terjadi dari gambar saja;
     tiap cerita jelas dari gambar + label pendek; **tanpa yang kontradiktif, tidak masuk akal,
     atau yang juri TAHU palsu**.
  4. Faithful: apa yang terjadi, seperti dilaporkan, tanpa hype atau spekulasi sebagai fakta.
  5. Craft: satu komposisi jelas, digambar/render bersih, **terbaca di ~300 px**, tanpa smear/
     artefak/teks rusak.
  Kalimat kunci juri: **"Detail for its own sake does not count."**
- Heats: dev = 12 game vs house images; top 100 dev juga main ≤12 game vs sesama (Checked).
  Final: 3 ronde Swiss + playoff top 52. **Yang masuk playoff menempati peringkat di atas
  semua yang tidak masuk playoff, berapa pun ratenya.** Tie-break: game playoff → file lebih
  kecil → submit lebih awal.
- Transcript gate (PENTING untuk builder):
  - `thinking_reproduces`: **≥30% baris terhitung harus authored** (ditulis agen di sesi terekam);
    baris yang pertama muncul di pesan manusia (paste), hasil tool, atau file yang dibaca = "read";
    **baris yang agen ketik ulang / ganti nama / format ulang dari kode yang sudah dilihat = "copied"**;
    baris starter kit dikecualikan; **≤40% baris boleh unwritten** (absent / dibawa masuk via
    git clone, curl/wget ke file, cp dari luar repo, unpack arsip, generator proyek);
    entrypoint (main.ts/main.py) harus punya ≥1 baris authored.
  - Sesi harus dimulai PADA/SETELAH kompetisi dibuka (thinking_in_window).
  - "The image itself counts as one line no transcript wrote."
  - **KESIMPULAN: generator HARUS ditulis fresh di sesi terekam oleh builder. JANGAN copy-paste
    file zip bos (frontpage.html / build_frontpage.py / main.ts / main.py). Layout boleh
    ditiru strukturnya, kodenya harus baru.**
- Teks yang ditujukan ke juri BOLEH ada di gambar dan dibaca juri sebagai bagian dari gambar.
- House bot bisa mengambil tempat berbayar dan hadiahnya TIDAK diberikan ke entry lain.

---

## 2. SPOT-CHECK PAKET CHRONICLE — cerita 17 Nov (apakah bisa dipercaya?)

Paket berisi 48 cerita 17 Nov. Dicek 8 dari sumber primer. Hasil: **4 BENAR, 1 CAMPURAN, 3 TIDAK TERBUKTI / SALAH TANGGAL.**
Paket ini TIDAK bisa dipercaya apa adanya — isinya campuran fakta nyata + karangan AI.

### BENAR terjadi 17 Nov 2026
1. **Xi & Sheinbaum bertemu di Shenzhen** menjelang APEC — BENAR (Reuters/Xinhua).
   Kerja sama teknologi, pertanian, air, kesehatan, pariwisata.
2. **WHO/UNEP "State of the Science on Endocrine Disrupting Chemicals 2026"** — BENAR, dirilis
   Selasa 17 Nov; update besar pertama sejak 2012; paparan bisa mulai sebelum lahir;
   biaya ~$1,1 triliun/tahun.
3. **World Bank "Finance and Prosperity 2026"** — BENAR, dirilis Selasa 17 Nov; kesenjangan
   pembiayaan UMKM $4 triliun (2019–2023); UMKM = 90% bisnis / 75% lapangan kerja.
   (Wording Chronicle "liquidity deficit" longgar, tapi substansi dekat.)
4. **Jembatan Kerch diserang hari ke-2** — BENAR (sudah diverifikasi di C5 kemarin; 18 Nov
   jembatan dilaporkan down — lihat §3 cerita 15).

### CAMPURAN (inti benar, detail tidak terverifikasi)
5. **Selat Hormuz — insiden tanker UKMTO 17 Nov** — BENAR (kapal tanker diserang 2×, atribusi
   ranjau hanya dari IRGC). TAPI "serangan balasan", "konvoi escort", "asuransi +8%"
   TIDAK TERVERIFIKASI — jangan tulis.

### TIDAK TERBUKTI / SALAH TANGGAL — jangan dipakai
6. **JWST "mengonfirmasi air atmosfer di exoplanet" sebagai berita 17 Nov** — TIDAK DITEMUKAN.
   Item nyata terdekat: es WASP-76b (14 Nov), uap air LHS 1140 b (8 Agu / update 14 Nov),
   Beta Pictoris d (15 Jul). Bukan berita 17 Nov.
7. **ITER "menyelesaikan perakitan central solenoid"** — SALAH TANGGAL. Modul terakhir
   ditumpuk **23 Juni 2026**, bukan 17 Nov.
8. **AU "memperpanjang mandat penjaga perdamaian Great Lakes sampai 2027"** — TIDAK DITEMUKAN
   pemungutan suara seperti itu. Item nyata: AS mendukung perpanjangan 1 tahun UNSOS/AUSSOM,
   diumumkan Senin 16 Nov (AFP).

**Pelajaran:** Chronicle punya struktur bagus (koran padat, 48 cerita, peta, indeks) tapi
isinya ~40% meragukan. Untuk 18 Nov, SEMUA konten harus diganti dengan cerita terverifikasi
di bawah ini. Jangan satu pun kalimat dari paket 17 Nov dibawa ke 18 Nov tanpa verifikasi
ulang tanggalnya.

---

## 3. CERITA 18 NOV 2026 TERVERIFIKASI (15 cerita — ini bahan entry)

Urutan = prioritas editorial (lead dulu). Setiap cerita: fakta yang BOLEH ditulis + sumber.
Bagian "JANGAN" = kalimat yang dilarang karena tidak terverifikasi / salah tanggal.

### F1 — LEAD: ESKALASI TELUK — Iran serang pangkalan AS di Kuwait & Bahrain
- Fakta: Semalam 17→18 Nov, Iran menembakkan drone/rudal ke situs drone & rudal AS di
  **Ali Al Salem (Kuwait)** dan **Sheikh Isa (Bahrain)**, setelah AS menyerang situs rudal
  IRGC di Pulau Qeshm (17 Nov). Serangan Iran pertama ke Kuwait sejak September.
  Bahrain mencegat serangan Iran 3× dalam sepekan. Houthi merebut kembali Bab el-Mandeb,
  mendekati Aden. Kilang Bapco Bahrain beroperasi >80% kapasitas. Wapres AS Vance:
  "no forever war" / tidak ada perang tanpa akhir.
- Sumber: Reuters, "Gulf briefing", 18 Nov 2026.
  https://www.reuters.com/world/middle-east/ (live blog Gulf, 18 Nov)
- JANGAN: klaim korban AS ("US casualties") — hanya klaim sumber Iran/media sosial,
  Pentagon TIDAK mengonfirmasi; Kuwait/Bahrain hanya melaporkan intersepsi, tanpa kerusakan.
  JANGAN: tulis "perang AS–Iran dimulai" — ini eskalasi, bukan deklarasi perang.
- Visual: peta Teluk (Kuwait–Bahrain–Qeshm–Bab el-Mandeb) — TANPA wajah pemimpin.

### F2 — APEC SHENZHEN: Xi & Putin berpidato; Trump–Putin & tiga arah dijadwalkan
- Fakta: Xi Jinping & Vladimir Putin berpidato di APEC Shenzhen 18 Nov, mengkritik
  proteksionisme. Putin–Trump bertemu 19 Nov seusai sidang pleno (Kremlin: TANPA
  perundingan bilateral penuh). Pertemuan tiga arah Xi–Trump–Putin Kamis 19 Nov,
  dialokasikan 1 jam. Trump tiba di China 18 Nov.
- Sumber: Reuters, 18 Nov 2026.
  https://www.reuters.com/world/china/putin-trump-meet-apec-summit-no-full-scale-talks-planned-kremlin-says-2026-11-18/
- JANGAN: tulis "Trump & Xi bertemu 18 Nov" — pertemuan mereka 19 Nov, BELUM terjadi.
  JANGAN: tulis "perundingan damai Ukraina" — tidak ada dalam laporan.

### F3 — INDONESIA–CHINA: 4 kemitraan strategis $71,8 M
- Fakta: Indonesia & China sepakati 4 kemitraan strategis **$71,8 miliar** (18 Nov),
  disaksikan Presiden Prabowo Subianto di Shenzhen (APEC): 10 smart city ~$50 M
  (Danantara + Shaanxi Construction); lab & manufaktur peralatan rumah tangga Hisense
  $10 M; pembiayaan infrastruktur $10 M (konsorsium SDIC); teknologi batu bara-ke-etanol
  $1,8 M (Pertamina + Beijing Petrochemical).
- Sumber: Reuters, 18 Nov 2026 13:29 UTC.
  https://www.reuters.com/world/indonesia-china-agree-four-strategic-partnerships-worth-718-billion-2026-11-18/
- JANGAN: tulis "$71,8 M sudah cair/dibangun" — ini kesepakatan, proyek mulai tahun depan.

### F4 — KANADA–CHINA: swap mata uang diperbarui, akses keuangan dibuka
- Fakta: PM Mark Carney di APEC Shenzhen (18 Nov): Kanada–China memperbarui kesepakatan
  swap mata uang bank sentral dan "saling menerbitkan mata uang"; akses lebih luas bagi
  perusahaan keuangan di pasar masing-masing. Xi–Carney sepakat (17 Nov) memperluas akses
  pasar China untuk petani & nelayan Kanada. Ekspor Kanada ke China naik >1/3 pada 2026;
  perdagangan dua arah C$125 M (~US$87 M). Kanada perpanjang 2 tahun keringanan tarif
  produk baja/aluminium China.
- Sumber: Reuters, 18 Nov 2026.
  https://northlandnewsradio.com/2026/11/18/canada-adjusts-china-ties-carney-says-aiming-to-clinch-right-deal-with-us/
- JANGAN: tulis nilai swap (tidak diumumkan) atau "Kanada tinggalkan AS" (Carney: pendekatan
  bertahap, tetap cari kesepakatan dengan AS).

### F5 — AS: Jeffries dinominasikan Ketua DPR, 251–11
- Fakta: Demokrat DPR menominasikan Hakeem Jeffries (New York, 56) sebagai Ketua DPR,
  Rabu 18 Nov, lewat pemungutan suara tertutup **251–11** (2 abstain). Jika terpilih
  pada pemungutan suara pleno 3 Jan 2027, ia jadi Ketua DPR kulit hitam pertama.
  Perlu 218 suara di pleno; Demokrat diproyeksikan pegang ≥257 kursi.
- Sumber: Reuters/NPR, 18 Nov 2026.
  https://www.whro.org/2026-11-18/democrats-formally-nominate-hakeem-jeffries-for-speaker-of-the-house
- JANGAN: tulis "Jeffries TERPILIH jadi Ketua DPR" — ini baru nominasi partai; pemungutan
  suara pleno 3 Jan 2027. JANGAN: sebut nama 11 penentang (pemungutan suara rahasia).

### F6 — TURKI: Imamoglu +2 tahun 1 bulan & larangan politik baru
- Fakta: Pengadilan Turki, Rabu 18 Nov, menjatuhkan hukuman tambahan **2 tahun 1 bulan**
  penjara + larangan politik baru kepada Wali Kota Istanbul Ekrem Imamoglu (yang sedang
  dipenjara) atas pelanggaran UU pemilu, terkait konvensi CHP Nov 2023. Ia salah satu dari
  9 terdakwa. Larangan politik sebelumnya: 2022 & 2025; total hukuman >6 tahun (sedang
  banding). Sebelum ditangkap, ia kandidat penantang utama Presiden Erdogan.
- Sumber: Reuters, 18 Nov 2026 15:59 UTC.
  https://www.reuters.com/business/media-telecom/turkish-court-hands-new-sentence-political-ban-jailed-istanbul-mayor-media-says-2026-11-18/
- JANGAN: tulis "Imamoglu dilarang jadi presiden selamanya" — larangan bisa banding;
  tulis sesuai putusan saja.

### F7 — COP31 ANTALYA: OPEC bela bahan bakar fosil
- Fakta: Sekjen OPEC Haitham Al Ghais, Rabu 18 Nov di COP31 Antalya: elektrifikasi
  "sangat bergantung pada minyak"; "kita akan membutuhkan semua energi". Tuan rumah Turki
  menargetkan pangsa listrik 35% dari permintaan energi akhir pada 2035 (dari ~20% kini);
  75 dari ~200 negara mendukung janji sukarela itu. Perundingan berakhir Jumat 20 Nov.
- Sumber: Reuters, 18 Nov 2026.
  https://www.reuters.com/business/energy/opec-speaks-up-fossil-fuels-cop31-climate-talks-2026-11-18/
- JANGAN: tulis "COP31 gagal/berhasil" — perundingan masih berjalan sampai 20 Nov.

### F8 — COP31: India — "tidak adil bebani negara berkembang"
- Fakta: India menyampaikan pernyataan nasional 18 Nov (Menteri Bhupender Yadav):
  "tidak adil membebani negara berkembang" dengan biaya iklim; transisi energi harus
  "adil, tertib, dan setara"; adaptasi harus dapat 30% pembiayaan iklim. Hari ini juga
  Hari Lautan COP31; rencana kebakaran hutan 23 negara.
- Sumber: The Hindu BusinessLine / UN News, 18 Nov 2026.
  https://www.thehindubusinessline.com/news/cop31-india-national-statement (cek URL saat build)
  https://news.un.org/en/story/2026/11/ (COP31 oceans day, update 18 Nov 07:02 ET)
- JANGAN: tulis angka pendanaan spesifik India tanpa sumber; tulis kutipan inti saja.

### F9 — UE: kesepakatan percepat izin jaringan listrik & energi terbarukan
- Fakta: Dewan UE + Parlemen Eropa mencapai kesepakatan sementara (diumumkan 18 Nov 01:35)
  untuk mempercepat izin proyek energi terbarukan, jaringan listrik & penyimpanan:
  maks 3 bulan untuk peralatan surya + penyimpanan, 6 bulan untuk penyimpanan mandiri &
  stasiun pengisian, 2 tahun untuk pumped hydro; portal digital tunggal; negara anggota
  punya 1,5 tahun untuk mengadopsi. Masih butuh persetujuan formal.
- Sumber: Council of the European Union (press release resmi), 18 Nov 2026.
  https://www.consilium.europa.eu/en/press/press-releases/2026/11/18/grids-package-council-and-parliament-agree-to-streamline-permitting-for-a-faster-clean-energy-transition/
- JANGAN: tulis "aturan sudah berlaku" — ini kesepakatan sementara, belum hukum.

### F10 — EBOLA KONGO: WHO pertahankan status darurat; anak-anak paling parah
- Fakta: 18 Nov, WHO menyatakan wabah Ebola (strain Bundibugyo) di DR Kongo TETAP
  darurat kesehatan masyarakat internasional (PHEIC), mengikuti saran Komite Darurat
  ke-3 (bertemu 17 Nov). Angka: >11.000 kasus, ~5.400 kematian (ECDC 15 Nov: 11.376
  kasus / 5.568 kematian), 67 zona kesehatan, 8 provinsi; 400–500 kasus baru/minggu.
  Anak-anak: >25% kasus, 1/3 kematian, **7 dari 10 anak di bawah 5 tahun yang
  terkonfirmasi meninggal**. Kenya 9 kasus impor (2 meninggal), Nigeria 1 kasus impor.
  Dua vaksin kandidat uji fase 2 di Bunia 26–27 Nov.
- Sumber: UN News "World News in Brief", 18 Nov 2026; WHO (pernyataan Dirjen Tedros, 17 Nov).
  https://europeansting.com/2026/11/18/world-news-in-brief-ebola-cases-double-in-dr-congo-chemical-exposure-starts-before-birth-turk-concern-over-eu-rwanda-transfer-plan/
- JANGAN: tulis angka pasti tunggal — angka WHO (11.000/5.400) dan pemerintah/ECDC
  (11.376/5.568) berbeda karena tanggal potong; tulis "~11.000 kasus, ~5.400 kematian".
  JANGAN: tulis "vaksin sudah ada" — strain Bundibugyo BELUM ada vaksin/treatment berlisensi.
- Catatan tanggal: angka & pernyataan Tedros dari 17 Nov; yang 18 Nov adalah KEPUTUSAN
  PHEIC dipertahankan. Framing benar: "WHO keeps Ebola emergency as child deaths mount".

### F11 — GTA VI: ulasan 99/100; peluncuran bergulir dimulai
- Fakta: Grand Theft Auto VI meluncur tengah malam waktu setempat **Kamis 19 Nov**
  (PS5 & Xbox Series X|S, $79,99; tanpa PC saat launch). 18 Nov: embargo ulasan dicabut
  11:00 GMT; **Metacritic 99/100 dari 140+ ulasan** ("universal acclaim", per 09:30 ET
  18 Nov); Selandia Baru pertama mendapat akses (tengah malam 19 Nov NZDT = 18 Nov di
  belahan barat); game dengan pre-order terbanyak dalam sejarah PlayStation Store;
  8 nominasi The Game Awards 2026 (diumumkan 17 Nov). Sony mewajibkan update firmware
  PS5 14.23 (1,267 GB) sebelum main.
- Sumber: People / Polygon / IGN / Rockstar Games, 18 Nov 2026.
  https://people.com/grand-theft-auto-vi-arrives-after-13-year-wait-as-gamers-worldwide-celebrate-long-awaited-release-12262350
  https://www.polygon.com/gta-6-out-now-spoiler-warning-new-zealand-release/
- JANGAN: tulis "GTA VI RILIS 18 NOV" — rilis resmi 19 Nov; yang 18 Nov adalah ulasan +
  awal peluncuran bergulir. Framing benar: "GTA VI scores 99 as midnight rollout begins".
  JANGAN: tulis angka penjualan hari pertama (belum ada).

### F12 — VOYAGER 1: satu hari-cahaya dari Bumi
- Fakta: **18 Nov 2026, 05:16:07 EST (10:16 UTC)**, Voyager 1 mencapai jarak **satu
  hari-cahaya dari Bumi — 16,094 miliar mil (25,9 miliar km)**; objek buatan manusia
  pertama yang sejauh itu. Sinyal radio kini butuh 24 jam penuh satu arah. Diluncurkan
  5 Sep 1977; melintasi heliopause Agu 2012; Voyager 2 baru mencapai jarak ini Nov 2035.
  Administrator NASA Jared Isaacman: "an extraordinary NASA achievement".
- Sumber: NASA / Smithsonian (National Air and Space Museum) / ScienceAlert / USA Today, 18 Nov 2026.
  https://www.smithsonianmag.com/blogs/air-space-museum/2026/11/18/nasas-voyager-1-has-reached-1-lightday-from-earth-it-is-the-first-humanmade-object-in-space-to-reach-that-distance/
  https://www.sciencealert.com/its-official-voyager-1-is-the-first-spacecraft-to-reach-one-light-day-from-earth
- JANGAN: tulis "Voyager 1 keluar dari tata surya hari ini" — ia keluar 2012; yang 18 Nov
  adalah jarak satu hari-cahaya. Angka boleh: 16,094 miliar mil / 25,9 miliar km / 24 jam.

### F13 — NVIDIA: pendapatan $115,8 M (+103%), laporan pertama tanpa Huang
- Fakta: Nvidia Q3 FY27: pendapatan **$115,8 miliar (+103% YoY)**, data centre $107,6 M,
  EPS $2,70; panduan Q4 $130 M; saham +5,2% setelah jam perdagangan. Laporan pertama
  tanpa Jensen Huang (mengundurkan diri 12 Nov); Ketua Dewan Harvey Jones: tidak ada
  niat mengembalikan Huang; CEO interim Colette Kress.
- Sumber: laporan keuangan Nvidia / Reuters, dirilis 17 Nov waktu AS.
- **NUANSA TANGGAL (PENTING): dirilis 17 Nov waktu AS / 18 Nov Asia–Eropa. Hanya boleh
  dipakai dengan framing "reported overnight / Asia trading 18 Nov" — JANGAN jadikan
  lead, JANGAN tulis "Nvidia melaporkan 18 Nov" tanpa kualifikasi.** Paling aman: item
  pasar kecil di strip bawah ("Nvidia +5.2% after hours on $115.8B quarter").

### F14 — GAZA: hujan dingin; 16 kematian (klaim otoritas kesehatan Hamas)
- Fakta: Hujan deras + dingin melanda Gaza 18 Nov; keluarga mengungsi di tenda, kekurangan
  bahan bakar & air. Otoritas kesehatan yang dikelola Hamas: **16 orang meninggal dalam
  48 jam terakhir "akibat dingin", termasuk 3 anak** — KLAIM, atribusi wajib. Pasukan Israel
  menyerang dua anggota Hamas dekat Khan Younis (Selasa).
- Sumber: UN News, update 18 Nov 2026.
- JANGAN: tulis "16 orang meninggal kedinginan" sebagai fakta tanpa atribusi "menurut
  otoritas kesehatan Hamas". JANGAN: tulis "gencatan senjata runtuh" — tidak dilaporkan.

### F15 — JEMBATAN KERCH: down setelah serangan hari ke-2
- Fakta: Jembatan Kerch (menghubungkan Rusia–Krimea) dilaporkan down/rusak setelah
  serangan hari kedua (17→18 Nov). Perkembangan lanjutan dari cerita C5 kemarin.
- Sumber: Reuters live blog, 18 Nov 2026 ("The Kerch Bridge is down").
- JANGAN: tulis detail kerusakan spesifik (panjang runtuh, korban) — tidak terverifikasi
  dalam sumber yang dibaca. Tulis satu baris pendek saja, atau gabung ke ticker.

### JUMLAH REALISTIS
**15 cerita terverifikasi (14 penuh + 1 borderline tanggal: Nvidia).**
Template Chronicle punya 48 slot (5 fitur + ~43 matriks). **48 cerita 18 Nov yang
terverifikasi TIDAK ADA** — satu hari berita tidak punya 48 peristiwa besar yang
masing-masing bisa diverifikasi dari sumber primer. Builder boleh menambah 3–5 item
kecil yang MASIH HARUS diverifikasi saat build (kandidat: hasil Liga Champions 18 Nov,
penutupan pasar/oil di tengah eskalasi Teluk, cuaca ekstrem lain) — total realistis
**18–22 cerita**. Jangan isi slot kosong dengan karangan.

---

## 4. CERITA YANG DITOLAK (jangan masuk gambar)

| Cerita | Alasan |
|---|---|
| UK sanksi 8 perusahaan pemukim Tepi Barat + Tzav 9 | Diumumkan **Selasa 17 Nov** (Menteri Luar Negeri Ed Miliband). Bukan 18 Nov. Reaksi Israel (ancam balasan) 18 Nov tapi terlalu tipis untuk jadi cerita. |
| Tabrakan kereta Praha, 46 luka-luka | Terjadi **Selasa 17 Nov ~07:20** (jembatan Seifertova; 4 serius termasuk 2 masinis; 1 kereta lewati sinyal bahaya; kerusakan >CZK 16 juta). Bukan 18 Nov. |
| Jet MiG-29 Serbia jatuh dekat Belgrade, pilot tewas | Hanya dari agregator sampah (1arterole.ru, "purportedly"); TIDAK ada sumber primer/tepercaya. Tidak terverifikasi. |
| AS kehilangan status eliminasi campak (PAHO) | Diumumkan **17 Nov**, bukan 18 Nov. |
| "Trump & Xi bertemu 18 Nov" | Pertemuan mereka **19 Nov**. 18 Nov hanya Trump tiba di China. |
| JWST air di exoplanet / ITER solenoid / AU Great Lakes (dari paket) | Bukan berita 17 Nov (lihat §2) — apalagi 18 Nov. |
| Klaim korban AS di Kuwait/Bahrain | Hanya klaim sumber Iran; Pentagon tidak konfirmasi. |
| Ethiopia–Eritrea pengerahan pasukan | Disebut di digest tapi TIDAK sempat diverifikasi dari sumber primer — jangan pakai. |
| "Perang AS–Iran" / "COP31 gagal" / "Jeffries terpilih Ketua DPR" | Spekulasi / belum terjadi — lihat JANGAN di tiap cerita. |

---

## 5. PELAJARAN LEADERBOARD 17 NOV (news-image-20261117, 7.777 entry)

Diambil via API leaderboard (Bearer key dari ~/.makefun/credentials, dibaca lewat script,
nilai key TIDAK pernah ditampilkan). Posisi entry kita "Fresh Sextant" (C5, 7 cerita):
**rank 5.242/7.777** (sebelumnya 5.207), rate ~0,9657 (interval 0,9545–0,9770).
Zona hadiah = top 50. Jauh di luar.

### 20 teratas — polanya JELAS: koran padat, banyak cerita
1. "Daily front page" (nomind)
2. "The world on Tuesday 17 November 2026" (gusade-taruna)
3. "Tuesday 17 November 2026 — the world's day in pictures" (calm-owl-89)
4. "The World in One Day: Tuesday 17 November 2026 (50 stories, date check…" (anon)
5. "The Daily Chronicle — Tuesday 17 November 2026"
6. "41 stories, 13 illustrated, six continents" (anon)
7. "The Daily Meridian — 30 stories, 12 illustrated" (anon)
8. "48 stories, improved" (anon)
9. "46 stories, 13 illustrated" (anon)
10. "The World in a Day — Tuesday 17 November 2026" (anon)
11. "43 stories on one front page, with a map" (anon)
12. "The World in One Day — Tuesday 17 November 2026" (rifkisetiawan) ← nama konsep SAMA dengan C5 kita, rank 12 vs kita 5242
13. "The World in One Day — 43 stories" (anon)
14. "35 stories, 6 continents" (anon)
15. "46 stories, 6 continents, one page" (anon)
16. "35 stories, 6 continents, 16 illustrated" (anon)
17. "50 stories: Tuesday, November 17, 2026" (anon)
18. "34 stories, 6 continents, 10 photos" (anon)
19. "The World in One Day — Tuesday 17 November 2026" (anon)
20. "30 stories, 10 illustrated, 6 continents" (anon)

### Pelajaran konkret
1. **Kepadatan = breadth yang terlihat.** Semua top 20 adalah front page padat dengan
   30–50 cerita, 6 benua, banyak ilustrasi/foto, beberapa pakai peta. C5 kita (7 cerita,
   bersih, lapang) kalah telak di kriteria 2 (breadth) — juri membandingkan dua gambar
   dan yang 40 cerita terlihat "lebih merangkum hari itu" daripada yang 7 cerita.
   Format Chronicle (48 cerita, koran padat, peta, indeks hotspot) adalah format yang
   TEPAT untuk kompetisi ini — strukturnya sudah cocok dengan pemenang.
2. **Kepadatan saja TIDAK cukup.** 5 terbawah ada "The Daily Atlas — 42 stories on one
   page" (rank 7.777, TERAKHIR). Halaman padat bisa mati total kalau ceritanya palsu/
   salah tanggal, tidak terbaca, atau komposisinya berantakan. Juri menghukum cerita
   yang ia TAHU palsu (kriteria 3) — inilah risiko terbesar paket Chronicle 17 Nov
   (§2: ~40% isinya meragukan).
3. **Judul entry menyebut jumlah cerita + tanggal + benua.** Top 20 hampir semua
   menyebut "Tuesday 17 November 2026" + jumlah cerita ("41 stories", "50 stories",
   "6 continents"). Judul bukan bagian gambar, tapi menandakan apa yang juri lihat:
   tanggal jelas + breadth jelas. Di gambar, tanggal HARUS besar dan tidak ambigu.
4. **"Detail for its own sake does not count" (aturan juri) vs realita:** juri TERTULIS
   bilang detail demi detail tidak dihitung, tapi EMPIRIS halaman 30–50 cerita menang.
   Penjelasannya: detail itu dihitung sebagai breadth (kriteria 2), bukan sebagai detail.
   Jadi: banyak cerita BOLEH, asal tiap cerita nyata + terbaca + relevan.
5. **Ilustrasi vs foto:** top 20 menyebut "illustrated" dan "photos" dua-duanya — tidak
   ada pola yang menang mutlak. Pelajaran Takaichi (C5): jangan ilustrasi pemimpin nyata
   yang salah gender/jumlah. Untuk 18 Nov: hero JANGAN gambar wajah pemimpin (ilustrasi
   maupun foto yang tidak pasti). Peta + ikon + foto resmi yang terverifikasi lebih aman.
6. **C5 kalah BUKAN karena nama konsep** — rank 12 pakai nama "The World in One Day"
   yang sama. Yang membedakan: jumlah cerita + breadth + eksekusi.
7. **Rate kita 0,9657 dengan interval sempit** — lapangan sangat rapat di atas (semua
   entry bagus mengalahkan house images). Perbedaan peringkat ditentukan di desimal
   ketiga; masuk top 100 dev (untuk main vs rival) butuh lompatan besar dari 0,9657.

### Implikasi untuk 18 Nov
- Target bentuk: koran padat ala Chronicle, **18–22 cerita terverifikasi** (bukan 7,
  bukan 48 karangan). Itu posisi tengah yang jujur: jauh lebih padat dari C5, tanpa
  satu pun cerita palsu.
- Tanggal "WEDNESDAY 18 NOVEMBER 2026" harus BESAR di masthead + diulang di ticker.
- Enam benua harus terwakili: Amerika Utara (Jeffries, Nvidia, GTA), Amerika Selatan
  (— lemah; cari 1 item saat build, mis. APEC/LatAm — JANGAN karang), Eropa (UE grids,
  Imamoglu, Kerch), Afrika (Ebola, COP31 Mesir? — tidak; Ebola DRC + COP31 Antalya
  secara geografis Afrika diwakili DRC), Asia (Teluk, APEC, Indonesia–China,
  Kanada–China), Oseania (— lemah; GTA NZ unlock bisa jadi jembatan: "New Zealand
  first to play GTA VI").
- Peta dunia dengan penanda hotspot = pembeda yang dipakai pemenang (rank 11: "with a map").

---

## 6. OPSI KONSEP (basis Chronicle, konten 18 Nov)

Struktur yang dipertahankan dari paket bos (7 file): masthead "THE WORLD CHRONICLE",
ticker bawah, indeks hotspot, matriks 6 kawasan, hero image besar, strip angka.
Yang diganti: SELURUH konten → 15 cerita §3; ukuran → 1024×1024, ≤1 MiB;
generator → ditulis fresh di sesi terekam (bukan copy file zip).

### OPSI A — "CHRONICLE PENUH" (direkomendasikan)
- Layout: masthead + tanggal besar → hero (peta Teluk + 3 kolom lead: F1 Teluk, F2 APEC,
  F3 Indonesia–China) → matriks 6 kawasan (masing-masing 2–3 cerita pendek dari 15
  cerita + 3–5 item kecil tambahan yang diverifikasi saat build) → strip angka hari ini
  ($71,8 M · 251–11 · 16,094 miliar mil · 99/100 · $115,8 M · 7 dari 10 anak) → ticker.
- Jumlah cerita: **18–22** (15 terverifikasi + 3–5 kecil saat build).
- Kelebihan: paling dekat dengan format pemenang top 20 (padat, 6 benua, peta); tetap
  100% terverifikasi; tanggal + breadth jelas.
- Risiko: butuh disiplin tipografi — font kecil di 1024 px harus tetap terbaca di
  300 px (lihat §7). Matriks 6 kawasan × 3 cerita = 18 slot; kalau item tambahan
  tidak terverifikasi, kosongkan slotnya daripada mengarang.
- Hero: PETA Teluk (ilustrasi vektor: Kuwait–Bahrain–Qeshm–Bab el-Mandeb + panah),
  tanpa wajah pemimpin. Alternatif hero: foto resmi APEC Shenzhen (family photo —
  builder harus cari sumber resmi Xinhua/AP; kalau tidak ketemu, pakai peta).

### OPSI B — "CHRONICLE RINGKAS" (fallback aman)
- Layout: masthead + tanggal besar → hero besar (peta Teluk) → 5 fitur utama
  (F1–F5) dengan teks lebih besar → matriks 6 kawasan × 1–2 cerita → strip angka → ticker.
- Jumlah cerita: **12–15** (hanya yang §3, tanpa item tambahan).
- Kelebihan: paling terbaca di 300 px; risiko salah ketik/karangan paling kecil;
  tiap cerita dapat gambar/ikon sendiri.
- Risiko: breadth lebih tipis dari pemenang (30–50 cerita); kemungkinan besar kalah
  dari halaman padat di kriteria 2 — seperti C5 kemarin (7 cerita → rank 5242).
  Opsi B hanya dipilih kalau build Opsi A kehabisan waktu.

### REKOMENDASI KOORDINATOR: **OPSI A.**
Alasan: (1) leaderboard membuktikan format padat yang menang; (2) kita punya 15 cerita
nyata lintas 6 benua + 3 bidang (politik, ekonomi, sains/budaya) — cukup untuk halaman
padat yang jujur; (3) risiko utama Opsi A (keterbacaan) bisa diatasi dengan tipografi
disiplin (§7), sementara risiko utama Opsi B (breadth tipis) TIDAK bisa diatasi —
sudah terbukti di C5. Syarat mutlak Opsi A: JANGAN isi slot kosong dengan karangan;
slot yang tidak terverifikasi dikosongkan / digabung.

---

## 7. CATATAN UNTUK BUILDER (bukan bagian riset — instruksi kerja)

1. **TIDAK ADA SUBMIT.** Build + push GitHub saja, lalu lapor. (Koreksi bos 05:09 WIB:
   "submit sebelum jam 7" itu typo — yang benar "jangan sub".)
2. **Resize:** output 1024×1024 (atau 1024×~1024 — Chronicle asli 1600×2360 portrait;
   di 1024 lebar, tinggi maks 1024 → layout HARUS dirombak ke persegi, bukan sekadar
   di-scale. Itu sebabnya generator ditulis ulang, bukan resize gambar lama.)
   Target file <1 MiB; JPEG kualitas ~85 atau PNG terkompresi — pilih yang lebih kecil
   dengan teks tetap tajam.
3. **Generator fresh di sesi terekam:** tulis main.ts + generator dari NOL di sesi build
   (sesi dimulai setelah kompetisi dibuka). JANGAN cp / curl / git clone file zip bos
   ke repo. Struktur layout boleh meniru Chronicle; kode harus baru (authorship ≥30%,
   unwritten ≤40%, entrypoint ≥1 baris authored — lihat §1).
4. **Render:** build_frontpage.py bos memakai path Chrome Mac — TIDAK jalan di Linux.
   VM punya /usr/bin/chromium-browser + Playwright chromium-1255. Builder yang urus
   render (headless Chromium via Playwright/puppeteer, atau gambar digambar langsung
   dengan canvas/SVG → PNG deterministik, tanpa network, tanpa font eksternal —
   Google Fonts via URL TIDAK BOLEH (program tanpa network; font harus di-bundle lokal
   atau pakai font sistem).
5. **Tipografi 300 px:** di 1024 px, teks tubuh minimum ~13–14 px agar di 300 px masih
   ~4 px (batas baca). Judul fitur ≥28 px, headline matriks ≥15 px, ticker ≥13 px.
   Uji: perkecil gambar ke 300 px dan baca — kalau tidak terbaca, kurangi cerita,
   bukan kecilkan font.
6. **Hero:** JANGAN ilustrasi wajah pemimpin (pelajaran Takaichi). Peta Teluk vektor
   atau foto resmi APEC (sumber resmi, atribusi dicatat di luar repo seperti kemarin).
7. **Tanggal:** "WEDNESDAY 18 NOVEMBER 2026" besar di masthead + di ticker. Jangan
   tulis "17 November" di mana pun. Nvidia ditulis dengan framing "reported overnight".
8. **Deterministik:** 2 run = byte identik. Tanpa tanggal/jam runtime, tanpa random,
   tanpa network. Semua teks hardcode dari §3.
9. **Check sebelum push:** jalankan `makefun check` dari kit (transcripts bundle dari
   sesi build); pastikan 0 FAIL; authorship ≥30%.

---

## 8. SUMBER PRIMER YANG DIPAKAI (semua publik, tanpa biaya)

Reuters (Gulf briefing, APEC Putin–Trump, Indonesia–China, Jeffries, Imamoglu, OPEC COP31,
Canada–China), UN News (Ebola brief, Gaza, COP31 oceans), WHO (Tedros 17 Nov),
Council of the EU (grids package), Smithsonian/NASA/ScienceAlert/USA Today (Voyager 1),
People/Polygon/Rockstar (GTA VI), The Hindu BusinessLine (India COP31), NPR (Jeffries),
Xinhua (Xi–Sheinbaum 17 Nov), WHO/UNEP (EDC 17 Nov), World Bank (Finance & Prosperity 17 Nov).
Leaderboard 17 Nov: GET https://make.fun/api/competitions/news-image-20261117/leaderboard
(Bearer key via script dari ~/.makefun/credentials — nilai key tidak pernah ditampilkan).

---

*— Akhir VERIFICATION.md — Fase 1 selesai. Lanjut: parent bawa konsep ke Ting,
lalu builder terpisah build Opsi A (atau B bila Ting putuskan).*
