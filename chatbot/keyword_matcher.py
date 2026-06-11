from automata.events import Event

KEYWORD_MAP: list[tuple[list[str], Event]] = [
    ([
        "diagnosa", "diagnosis", "diagnose", "diagnostic",
        "kerusakan", "rusak", "mogok", "ngadat", "macet",
        "masalah", "bermasalah", "gangguan", "error", "trouble",
        "cek kerusakan", "cari masalah", "cari tahu masalah",
        "identifikasi", "analisa",
    ], Event.DIAGNOSA),
    ([
        "servis", "service", "diservis", "di-service",
        "perawatan berkala", "servis berkala", "service berkala",
        "servis rutin", "service rutin", "servis periodik",
        "jadwal servis", "jadwal service", "waktu servis", "kapan servis",
        "servis motor", "servis mobil", "service motor", "service mobil",
        "booking servis", "booking service",
        "servis besar", "servis kecil", "service besar", "service kecil",
        "cek servis", "cek service", "perlu servis", "perlu service",
        "km servis", "km service", "berdasar km",
    ], Event.SERVIS),
    ([
        "tips", "tip", "trik",
        "perawatan", "rawat", "merawat", "merawat kendaraan",
        "edukasi", "belajar", "panduan", "guide", "tutorial",
        "cara merawat", "cara menjaga", "cara rawat",
        "menjaga", "menjaga kendaraan", "menjaga motor", "menjaga mobil",
        "saran", "suggestion", "rekomendasi", "rekomendasi perawatan",
        "info perawatan", "informasi perawatan", "pengetahuan",
        "tips motor", "tips mobil", "tips kendaraan",
        "tips merawat", "tips perawatan motor", "tips perawatan mobil",
        "penting", "wajib tahu", "harus tahu",
        "edukasi kendaraan", "belajar otomotif", "ilmu otomotif",
        "bengkel", "info bengkel",
    ], Event.TIPS),
    ([
        "motor", "sepeda motor", "motoran", "motoran",
        "roda dua", "roda 2", "kendaraan roda dua", "kendaraan roda 2",
        "matic", "bebek", "sport", "naked", "cub", "skutik",
        "vespa", "variasi", "moped",
    ], Event.MOTOR),
    ([
        "mobil", "mobilan", "mobilan",
        "roda empat", "roda 4", "kendaraan roda empat", "kendaraan roda 4",
        "mobil pribadi", "sedan", "SUV", "MPV", "pickup", "pick up",
        "hatchback", "coupe", "convertible", "crossover",
        "LCGC", "city car", "family car",
    ], Event.MOBIL),
    ([
        "mesin", "engine", "enjin",
        "piston", "karburator", "karbu", "injeksi",
        "busi", "businya", "ganti busi", "cek busi",
        "starter", "distarter", "starter motor", "elektrik starter",
        "oli mesin", "oli samping", "oli 2 tak",
        "knalpot", "muffler", "exhaust",
        "mesin brebet", "mesin ngempos", "mesin loyo",
        "mesin bunyi", "mesin berisik", "mesin kasar",
        "mesin ngobok", "mesin brebet", "mesin stut",
        "mesin mati", "mendadak mati",
        "susah hidup", "susah dihidupkan", "susah start", "susah distarter",
        "tidak mau hidup", "gak mau hidup",
        "tidak bisa starter", "gak bisa starter", "starter mati",
        "nggak bisa jalan", "gak bisa jalan", "nggak mau jalan",
        "tarikan berat", "tarikan kurang", "tidak bertenaga",
        "boros bensin", "boros bahan bakar", "boros",
    ], Event.MESIN),
    ([
        "aki", "accu", "battery", "batre", "batere", "baterai",
        "aki mobil", "aki motor", "aki matic",
        "aki soak", "aki mati", "aki drop", "aki lemah",
        "aki kering", "aki basah", "aki kering basah",
        "aki MF", "maintenance free",
        "tegangan aki", "volt aki", "cek aki",
        "lampu aki", "indikator aki",
        "ganti aki", "beli aki", "aki baru",
        "jumper", "jumper aki", "stroom",
    ], Event.AKI),
    ([
        "kelistrikan", "listrik",
        "lampu", "lampu mati", "lampu redup", "lampu sen",
        "dinamo", "dinamo starter", "spion listrik",
        "sekring", "fuse",
        "starter elektrik", "elektrik",
        "kabel", "kabel putus", "kabel konsleting",
        "konsleting", "korsleting", "short circuit",
        "lampu indikator", "indikator",
        "klakson", "klakson mati", "klakson lemah",
        "spedometer", "speedometer",
        "power window", "central lock",
    ], Event.KELISTRIKAN),
    ([
        "transmisi", "transmission", "gigi", "persneling",
        "kopling", "clutch", "sambung kopling",
        "gigi susah masuk", "gigi macet", "gigi loncat",
        "gigi ngelos", "gigi tidak mau masuk",
        "transmisi matic", "matic", "CVT",
        "v-belt", "roller", "belt CVT",
        "kopling selip", "kopling aus", "kopling habis",
        "tarikan berat gigi", "transmisi bermasalah",
        "oli transmisi", "oli gardan", "gardan",
    ], Event.TRANSMISI),
    ([
        "suspensi", "suspension", "shock", "shockbreaker",
        "kejutan", "guncangan", "hentakan",
        "suspensi keras", "suspensi bocor", "shock bocor",
        "per", "spring", "koil", "coil spring",
        "kaki-kaki", "understeer", "oversteer",
        "mobil oleng", "motor oleng",
        "bushing", "ball joint", "tie rod",
        "stabilizer", "suspensi mobil", "suspensi motor",
        "setelan suspensi", "kencangkan suspensi",
    ], Event.SUSPENSI),
    ([
        "pendingin", "coolant",
        "radiator", "air radiator", "coolant mesin",
        "panas", "panas banget", "cepat panas", "sering panas", "mesin panas",
        "overheat", "kepanasan", "suhu tinggi", "suhu naik",
        "temperatur naik", "indikator panas", "temperature",
        "ac", "air conditioner", "ac mobil", "ac motor",
        "ac tidak dingin", "ac panas", "freon", "freon ac",
        "kompresor ac", "kipas radiator", "kipas pendingin",
        "thermostat", "cooling fan", "water pump",
        "sirkulasi pendingin", "bocor radiator",
    ], Event.PENDINGIN),
    ([
        "rem", "brake", "brek",
        "pengereman", "ngerem",
        "kampas", "kampas rem", "kempas",
        "cakram", "disc brake", "tromol",
        "minyak rem", "oli rem", "booth",
        "rem blong", "rem tidak pakem", "rem kurang pakem",
        "rem bunyi", "rem berdecit", "rem ngoceh",
        "rem keras", "rem dalam", "rem kosong",
        "rem tangan", "hand brake", "parkir brake",
        "ABS", "rem abs",
    ], Event.REM),
    ([
        "ban", "tire", "tyre",
        "roda", "velg", "rim",
        "tubles", "tubeless", "tubles", "ban tubeless",
        "ban dalam", "ban luar",
        "ban bocor", "bocor", "kempes", "ban kempes",
        "tekanan ban", "angin ban", "angin",
        "aus", "ban aus", "ban gundul", "ban tipis",
        "rotasi ban", "tukar ban",
        "spooring", "balancing", "spooring balancing",
        "ban motor", "ban mobil",
    ], Event.BAN),
    ([
        "oli", "pelumas", "lumas", "lubricant",
        "mesin oli", "oil", "oli mesin",
        "ganti oli", "tukar oli", "oles",
        "oli gardan", "oli transmisi", "oli kopling",
        "oli rem", "minyak rem",
        "oli samping", "oli 2 tak",
        "kekentalan oli", "viskositas", "SAE",
        "oli motor", "oli mobil", "oli matic",
    ], Event.OLI),
    ([
        "iya", "ya", "y", "iyaa", "iyya",
        "betul", "benar", "tentu", "tentunya", "pastinya",
        "siap", "siap bos", "ok", "oke", "okay", "okelah",
        "yakin", "pasti", "setuju", "sepakat",
        "boleh", "boleh juga", "lanjut", "lanjutkan",
        "good", "fine", "baik", "baek",
        "iya betul", "iya benar", "betul sekali", "benar sekali",
        "iya dong", "iya lah", "tentu saja", "pasti dong",
        "silahkan", "silakan", "monggo",
        "masih", "masih iya", "masih betul", "masih begitu",
        "masih sama", "masih seperti itu",
        "berbunyi aneh", "bunyi aneh",
        "normal", "normal saja", "suara normal", "berfungsi normal",
        "berfungsi", "tidak berfungsi", "nggak berfungsi", "gak berfungsi",
        "mati total", "mati semua", "mati lampu",
        "susah dipindah",
        "terasa oleng", "oleng",
        "suhu naik", "temperatur naik",
        "indikator nyala", "lampu nyala",
        "nyala", "menyala",
        "berbunyi", "bunyi",
        "terasa", "terasa aneh",
        "masih berfungsi", "masih nyala",
        "gak normal", "nggak normal", "tidak normal",
        "hidup", "masih hidup",
    ], Event.YA),
    ([
        "tidak", "nggak", "ga", "gak", "enggak", "kagak",
        "bukan", "ndak", "nda", "kaga",
        "gak mau", "nggak mau", "nggak pengen",
        "belum", "belum juga", "belum sama sekali",
        "jangan", "jangan dulu",
        "tidak ada", "nggak ada", "gak ada",
        "tidak mau", "tidak ingin",
        "tidak setuju", "nggak setuju",
        "enggak usah", "nggak usah", "gak usah",
        "skip", "lewat", "lewati",
        "ngga", "ngg",
    ], Event.TIDAK),
    ([
        "25000", "25.000", "25 ribu", "25rb",
        "dua puluh lima ribu", "25 km", "25 kilometer",
    ], Event.MILEAGE_25000),
    ([
        "20000", "20.000", "20 ribu", "20rb",
        "dua puluh ribu", "20 km", "20 kilometer",
    ], Event.MILEAGE_20000),
    ([
        "15000", "15.000", "15 ribu", "15rb",
        "lima belas ribu", "15 km", "15 kilometer",
    ], Event.MILEAGE_15000),
    ([
        "10000", "10.000", "10 ribu", "10rb",
        "sepuluh ribu", "10 km", "10 kilometer",
    ], Event.MILEAGE_10000),
    ([
        "5000", "5.000", "5 ribu", "5rb",
        "lima ribu", "5 km", "5 kilometer",
    ], Event.MILEAGE_5000),
    ([
        "menu", "kembali", "back", "kembali ke menu",
        "utama", "awal", "ke awal", "ke menu utama",
        "menu utama", "home", "ke home",
        "kembali ke awal", "kembali ke utama",
        "balik", "balik lagi",
    ], Event.MENU),
    ([
        "selesai", "sudah", "cukup", "udah", "udahan",
        "terimakasih", "terima kasih", "makasih", "thanks", "thank you",
        "bye", "dadah", "daah", "sampai jumpa",
        "keluar", "tidak ada", "ga ada lagi", "nggak ada lagi",
        "selesai dulu", "cukup dulu", "sudah dulu",
        "tidak mau tanya", "nggak mau tanya",
        "beres", "done", "finish", "selesai semua",
    ], Event.SELESAI),
    ([
        "mulai", "start", "mulai chat", "mulai konsultasi",
        "hello", "halo", "hai", "hallo", "helo",
        "siang", "pagi", "sore", "malam",
        "assalamualaikum", "assalamu alaikum",
        "permisi", "maaf", "mau tanya", "mau nanya",
        "boleh tanya", "boleh nanya", "boleh minta bantuan",
        "tolong", "bantu", "bantuan", "help",
        "ada orang", "ada admin", "ada yang bisa bantu",
        "tes", "test", "coba", "testing",
        "hallo", "halo halo",
        "chat", "chatbot", "bot",
    ], Event.START_CHAT),
]

SINGLE_WORD_MAP: dict[str, Event] = {}
for keywords, event in KEYWORD_MAP:
    for kw in keywords:
        if " " not in kw and len(kw) > 1:
            SINGLE_WORD_MAP[kw] = event

MODULE_EVENTS: set[Event] = {Event.DIAGNOSA, Event.SERVIS, Event.TIPS}

MIN_KEYWORD_LENGTH = 3

MILEAGE_EVENTS: list[tuple[int, Event]] = [
    (5000, Event.MILEAGE_5000),
    (10000, Event.MILEAGE_10000),
    (15000, Event.MILEAGE_15000),
    (20000, Event.MILEAGE_20000),
    (25000, Event.MILEAGE_25000),
]

MILEAGE_RANGES: list[tuple[range, Event]] = [
    (range(0, 7501), Event.MILEAGE_5000),
    (range(7501, 12501), Event.MILEAGE_10000),
    (range(12501, 17501), Event.MILEAGE_15000),
    (range(17501, 22501), Event.MILEAGE_20000),
    (range(22501, 100000), Event.MILEAGE_25000),
]


class KeywordMatcher:
    def match(self, user_input: str) -> Event:
        text = user_input.lower().strip()
        best_event = Event.UNKNOWN
        best_length = 0

        for keywords, event in KEYWORD_MAP:
            for keyword in keywords:
                klen = len(keyword)
                if klen < MIN_KEYWORD_LENGTH:
                    continue
                if keyword in text and klen > best_length:
                    best_event = event
                    best_length = klen

        if best_event != Event.UNKNOWN:
            return best_event

        for word in text.split():
            clean = word.strip(".,!?;:\"'()[]{}")
            if clean in SINGLE_WORD_MAP:
                return SINGLE_WORD_MAP[clean]

        digits = "".join(c for c in text if c.isdigit())
        if digits and len(digits) >= 4:
            num = int(digits)
            for mval, mev in MILEAGE_EVENTS:
                if num == mval:
                    return mev
            for mrange, mev in MILEAGE_RANGES:
                if num in mrange:
                    return mev

        return Event.UNKNOWN

    def match_excluding(self, user_input: str, exclude: set[Event]) -> Event:
        text = user_input.lower().strip()
        best_event = Event.UNKNOWN
        best_length = 0

        for keywords, event in KEYWORD_MAP:
            if event in exclude:
                continue
            for keyword in keywords:
                klen = len(keyword)
                if klen < MIN_KEYWORD_LENGTH:
                    continue
                if keyword in text and klen > best_length:
                    best_event = event
                    best_length = klen

        if best_event != Event.UNKNOWN:
            return best_event

        for word in text.split():
            clean = word.strip(".,!?;:\"'()[]{}")
            if clean in SINGLE_WORD_MAP and SINGLE_WORD_MAP[clean] not in exclude:
                return SINGLE_WORD_MAP[clean]

        digits = "".join(c for c in text if c.isdigit())
        if digits and len(digits) >= 4:
            num = int(digits)
            for mval, mev in MILEAGE_EVENTS:
                if num == mval:
                    return mev
            for mrange, mev in MILEAGE_RANGES:
                if num in mrange:
                    return mev

        return Event.UNKNOWN