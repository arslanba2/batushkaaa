from datetime import time

SHIFT_SCHEDULES = {
    "V1": {
        "I1": [
            (time(8, 0, 0), time(10, 0, 0)),
            (time(10, 0, 0), time(12, 0, 0)),
            (time(13, 0, 0), time(14, 45, 0)),
            (time(14, 45, 0), time(17, 0, 0))
        ]
    },
    "V2": {
        "I1": [
            (time(7, 0, 0), time(9, 0, 0)),
            (time(9, 0, 0), time(11, 0, 0)),
            (time(11, 30, 0), time(13, 15, 0)),
            (time(13, 15, 0), time(15, 0, 0))
        ],
        "I2": [
            (time(15, 0, 0), time(16, 30, 0)),
            (time(16, 30, 0), time(18, 0, 0)),
            (time(18, 30, 0), time(20, 45, 0)),
            (time(20, 45, 0), time(23, 0, 0))
        ]
    },
    "V3": {
        "I1": [
            (time(7, 0, 0), time(9, 0, 0)),
            (time(9, 0, 0), time(11, 0, 0)),
            (time(11, 30, 0), time(13, 15, 0)),
            (time(13, 15, 0), time(15, 0, 0))
        ],
        "I2": [
            (time(15, 0, 0), time(16, 30, 0)),
            (time(16, 30, 0), time(18, 0, 0)),
            (time(18, 30, 0), time(20, 45, 0)),
            (time(20, 45, 0), time(23, 0, 0))
        ],
        "I3": [
            (time(23, 0, 0), time(0, 45, 0)),  # Gece yarısından sonraki saatler
            (time(0, 45, 0), time(2, 30, 0)),
            (time(3, 0, 0), time(5, 0, 0)),
            (time(5, 0, 0), time(7, 0, 0))
        ]
    }
}

SKILLS = {
    "HEPSİ": {"ÜRETİM", "ÜRETİM DIŞI", "KALİTE"},
    "ÜRETİM": {"ÜRETİM", "ÜRETİM DIŞI"},
    "ÜRETİM DIŞI": {"ÜRETİM DIŞI"},
    "KALİTE": {"KALİTE"},
    "KISMİ": {"ÜRETİM", "ÜRETİM DIŞI"}
}