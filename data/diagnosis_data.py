DIAGNOSIS_DATA: dict[str, dict[str, str]] = {
    "RESULT_ENGINE_MINOR": {
        "title": "Gangguan Mesin Ringan",
        "solution": (
            "Kemungkinan masalah pada **sistem pengapian atau bahan bakar**.\n\n"
            "Penyebab umum:\n"
            "\u2022 Busi kotor atau aus \u2014 bersihkan atau ganti busi\n"
            "\u2022 Filter udara kotor \u2014 bersihkan atau ganti\n"
            "\u2022 Karburator/perangkat injeksi perlu disetel ulang\n\n"
            "Langkah:\n"
            "1. Cek kondisi busi, bersihkan elektroda dari kerak\n"
            "2. Periksa filter udara, bersihkan jika kotor\n"
            "3. Jika masih, lakukan tune up ringan di bengkel"
        ),
    },
    "RESULT_ENGINE_MAJOR": {
        "title": "Gangguan Mesin Berat",
        "solution": (
            "Kemungkinan terdapat masalah serius pada **sistem pembakaran**.\n\n"
            "Penyebab umum:\n"
            "\u2022 Kebocoran kompresi (ring piston aus)\n"
            "\u2022 Kerusakan katup atau rantai timing\n"
            "\u2022 Sistem bahan bakar bermasalah (injektor tersumbat)\n"
            "\u2022 Overheating yang menyebabkan kerusakan internal\n\n"
            "Langkah:\n"
            "1. Jangan paksakan kendaraan dinyalakan terus\n"
            "2. Segera bawa ke bengkel terpercaya\n"
            "3. Minta cek kompresi mesin dan sistem pengapian\n\n"
            "Perkiraan biaya: Rp 500.000 \u2013 Rp 2.000.000 tergantung kerusakan"
        ),
    },
    "RESULT_BATTERY_CHECK": {
        "title": "Masalah Starter",
        "solution": (
            "Kemungkinan ada masalah pada **sistem starter**.\n\n"
            "Penyebab umum:\n"
            "\u2022 Dinamo starter aus (sikat karbon habis)\n"
            "\u2022 Kabel ke starter longgar atau korosi\n"
            "\u2022 Relay starter bermasalah\n"
            "\u2022 Sekring starter putus\n\n"
            "Langkah:\n"
            "1. Cek bunyi starter \u2014 jika \u201cklik\u201d tanpa putaran, "
            "kemungkinan aki lemah\n"
            "2. Jika aki baik, periksa sikat karbon dinamo starter\n"
            "3. Bawa ke bengkel untuk servis starter"
        ),
    },
    "RESULT_BATTERY_WEAK": {
        "title": "Aki Lemah atau Habis",
        "solution": (
            "Kemungkinan **aki lemah atau sudah soak**.\n\n"
            "Penyebab umum:\n"
            "\u2022 Aki sudah tua (lebih dari 2\u20133 tahun)\n"
            "\u2022 Jarang dipakai, aki tidak mendapat pengisian\n"
            "\u2022 Ada kebocoran arus (korsleting kecil)\n"
            "\u2022 Sistem pengisian (alternator/kiprok) rusak\n\n"
            "Langkah:\n"
            "1. Coba jumper dengan kabel dan aki lain\n"
            "2. Jika bisa distarter, biarkan mesin hidup 15\u201330 menit\n"
            "3. Cek tegangan aki (multimeter): minimal 12,4V saat mati\n"
            "4. Jika masih <12V setelah diisi, ganti aki baru\n\n"
            "Tips: Aki kering biasanya lebih tahan lama dan bebas perawatan."
        ),
    },
    "RESULT_ELECTRICAL": {
        "title": "Masalah Kelistrikan",
        "solution": (
            "Kemungkinan ada **gangguan pada sistem kelistrikan**.\n\n"
            "Penyebab umum:\n"
            "\u2022 Sekring putus akibat beban lebih\n"
            "\u2022 Kabel konsleting atau isolasi terbuka\n"
            "\u2022 Soket atau konektor longgar/berkarat\n"
            "\u2022 Dinamo/alternator tidak mengisi dengan benar\n\n"
            "Langkah:\n"
            "1. Periksa sekring yang putus, ganti dengan ampere sesuai\n"
            "2. Cek konektor kabel \u2014 pastikan tidak ada yang longgar\n"
            "3. Jika lampu redup, cek tegangan aki dan sistem pengisian\n"
            "4. Untuk masalah spion/power window, cek motor penggeraknya"
        ),
    },
    "RESULT_BRAKE": {
        "title": "Masalah Sistem Rem",
        "solution": (
            "Kemungkinan ada masalah pada **sistem pengereman**.\n\n"
            "Penyebab umum:\n"
            "\u2022 Kampas rem habis (tipis) \u2014 perlu diganti\n"
            "\u2022 Minyak rem berkurang atau bocor\n"
            "\u2022 Cakram/tromol aus atau tidak rata\n"
            "\u2022 Selang rem menggelembung (brake fade)\n\n"
            "Langkah:\n"
            "1. Periksa ketebalan kampas rem \u2014 jika <2mm, ganti segera\n"
            "2. Cek level minyak rem di reservoir\n"
            "3. Jika rem bunyi, kemungkinan kampas sudah habis atau "
            "ada kerikil di cakram\n"
            "4. Jika rem blong, jangan dipaksakan \u2014 bawa dengan "
            "towing ke bengkel\n\n"
            "Keselamatan: rem adalah komponen vital. Jangan tunda perbaikan!"
        ),
    },
    "RESULT_TIRE": {
        "title": "Masalah Ban",
        "solution": (
            "Kemungkinan ada masalah pada **ban atau roda**.\n\n"
            "Penyebab umum:\n"
            "\u2022 Tekanan angin kurang atau tidak sesuai\n"
            "\u2022 Keausan tidak merata (spooring/balancing salah)\n"
            "\u2022 Ban bocor halus (tertusuk paku/serpihan)\n"
            "\u2022 Velg bengkok atau bearing roda aus\n\n"
            "Langkah:\n"
            "1. Cek tekanan angin \u2014 sesuaikan dengan rekomendasi pabrik\n"
            "2. Periksa TWI (indikator keausan) di alur ban\n"
            "3. Jika aus tidak merata, lakukan spooring & balancing\n"
            "4. Ban bocor kecil bisa ditambal, tapi jika dinding "
            "ban sobek, harus ganti\n\n"
            "Tips: Rotasi ban setiap 10.000 km agar keausan lebih merata."
        ),
    },
    "RESULT_TRANSMISI": {
        "title": "Masalah Transmisi atau Kopling",
        "solution": (
            "Kemungkinan ada masalah pada **sistem transmisi atau kopling**.\n\n"
            "Penyebab umum:\n"
            "\u2022 Kopling aus atau selip (pada motor/mobil manual)\n"
            "\u2022 Oli transmisi kurang atau kotor\n"
            "\u2022 V-belt atau roller CVT aus (pada matic)\n"
            "\u2022 Gigi transmisi aus atau syncromesh rusak (mobil)\n\n"
            "Langkah:\n"
            "1. Untuk matic: cek kondisi v-belt dan roller CVT\n"
            "2. Untuk manual: periksa main kopling dan kabel kopling\n"
            "3. Cek level dan kondisi oli transmisi\n"
            "4. Jika gigi susah masuk atau bunyi, segera bawa ke bengkel transmisi\n\n"
            "Estimasi biaya: Rp 100.000 \u2013 Rp 500.000 tergantung kerusakan"
        ),
    },
    "RESULT_SUSPENSI": {
        "title": "Masalah Suspensi atau Kaki-Kaki",
        "solution": (
            "Kemungkinan ada masalah pada **sistem suspensi atau kaki-kaki**.\n\n"
            "Penyebab umum:\n"
            "\u2022 Shockbreaker bocor atau rusak\n"
            "\u2022 Bushing atau ball joint aus\n"
            "\u2022 Per / coil spring patah atau kendur\n"
            "\u2022 Setelan suspensi tidak sesuai\n\n"
            "Langkah:\n"
            "1. Cek shockbreaker: apakah ada kebocoran oli atau bunyi saat ditekan\n"
            "2. Periksa bushing lengan arm dan stabilizer\n"
            "3. Coba goyangkan kendaraan ke samping \u2014 jika masih oleng, "
            "kemungkinan shock sudah lemah\n"
            "4. Jika suspensi keras, periksa ball joint dan tie rod\n\n"
            "Estimasi biaya: Rp 200.000 \u2013 Rp 1.500.000 "
            "tergantung komponen yang diganti"
        ),
    },
    "RESULT_PENDINGIN": {
        "title": "Masalah Sistem Pendingin atau AC",
        "solution": (
            "Kemungkinan ada masalah pada **sistem pendingin mesin atau AC**.\n\n"
            "Penyebab umum:\n"
            "\u2022 Air radiator kurang atau bocor\n"
            "\u2022 Kipas radiator mati atau tidak berfungsi\n"
            "\u2022 Thermostat macet (tertutup terus)\n"
            "\u2022 Freon AC habis atau bocor (untuk AC mobil)\n"
            "\u2022 Water pump rusak sehingga sirkulasi air terganggu\n\n"
            "Langkah:\n"
            "1. Cek level air radiator \u2014 jangan buka radiator dalam keadaan panas\n"
            "2. Periksa apakah kipas radiator menyala saat mesin panas\n"
            "3. Jika indikator suhu naik, segera matikan mesin dan biarkan dingin\n"
            "4. Untuk AC tidak dingin, coba cek freon di bengkel AC\n\n"
            "Estimasi biaya: Rp 50.000 (isi air radiator) \u2013 "
            "Rp 500.000 (service AC)"
        ),
    },
}
