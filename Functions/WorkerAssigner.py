from Models.Dictionaries import SHIFT_SCHEDULES
from Models import Worker, Operation, Jig, Product
from datetime import datetime, timedelta


class Schedule:
    def __init__(self):
        self.start_date = None
        self.end_date = None
        self.start_shift = None
        self.dates = None
        self.working_order = None

    def set_start_date(self, date):
        self.start_date = date

    def get_start_date(self):
        return self.start_date

    def set_end_date(self, date):
        self.end_date = date

    def get_end_date(self):
        return self.end_date

    def set_start_shift(self, shift):
        self.start_shift = shift

    def get_start_shift(self):
        return self.start_shift

    def set_working_order(self, _working_order):
        self.working_order = _working_order

    def create_time_intervals(self):
        if not self.start_date or not self.end_date or not self.working_order or not self.start_shift:
            raise ValueError("Start date, end date, working order, and start shift must be set.")

        self.dates = []
        current_date = self.start_date
        is_first_day = True

        while current_date <= self.end_date:
            date_obj = Date()  # Yeni bir Date objesi oluştur
            date_obj.date = current_date
            time_intervals = []

            if is_first_day:
                # İlk gün için start_shift'e göre zaman aralıkları oluştur
                shift_order = self.get_shift_order_for_first_day()
                is_first_day = False
            else:
                # Sonraki günler için working_order'e göre tüm aktif vardiyaları al
                shift_order = self.get_shift_order_for_other_days()

            for shift, intervals in shift_order.items():
                for interval in intervals:
                    time_interval = TimeInterval()  # Yeni bir TimeInterval objesi oluştur
                    time_interval.interval = interval
                    time_interval.shift = shift
                    time_intervals.append(time_interval)  # TimeInterval objesini listeye ekle

            date_obj.time_intervals = time_intervals  # Date objesine time_intervals listesini ata
            self.dates.append(date_obj)  # Date objesini tarih listesine ekle
            current_date += timedelta(days=1)  # Bir sonraki güne geç

    def get_shift_order_for_first_day(self):
        shift_schedule = SHIFT_SCHEDULES.get(self.working_order, {})
        shift_order = {}

        if self.working_order == "V1":
            # V1 seçildiyse sadece I1 aktif
            if self.start_shift == "I1":
                shift_order["I1"] = shift_schedule.get("I1", [])

        elif self.working_order == "V2":
            # V2 seçildiyse başlangıç vardiyası I1 veya I2 olabilir
            if self.start_shift == "I1":
                # İlk gün I1 ve I2 aktif
                shift_order["I1"] = shift_schedule.get("I1", [])
                shift_order["I2"] = shift_schedule.get("I2", [])
            elif self.start_shift == "I2":
                # İlk gün sadece I2 aktif
                shift_order["I2"] = shift_schedule.get("I2", [])

        elif self.working_order == "V3":
            # V3 seçildiyse başlangıç vardiyası I1, I2 veya I3 olabilir
            if self.start_shift == "I1":
                # İlk gün tüm vardiyalar (I1, I2, I3) aktif
                shift_order["I1"] = shift_schedule.get("I1", [])
                shift_order["I2"] = shift_schedule.get("I2", [])
                shift_order["I3"] = shift_schedule.get("I3", [])
            elif self.start_shift == "I2":
                # İlk gün I2 ve I3 aktif
                shift_order["I2"] = shift_schedule.get("I2", [])
                shift_order["I3"] = shift_schedule.get("I3", [])
            elif self.start_shift == "I3":
                # İlk gün sadece I3 aktif
                shift_order["I3"] = shift_schedule.get("I3", [])

        return shift_order

    def get_shift_order_for_other_days(self):
        shift_schedule = SHIFT_SCHEDULES.get(self.working_order, {})
        shift_order = {}

        if self.working_order == "V1":
            # V1 seçildiyse sadece I1 aktif
            shift_order["I1"] = shift_schedule.get("I1", [])

        elif self.working_order == "V2":
            # V2 seçildiyse I1 ve I2 aktif
            shift_order["I1"] = shift_schedule.get("I1", [])
            shift_order["I2"] = shift_schedule.get("I2", [])

        elif self.working_order == "V3":
            # V3 seçildiyse tüm vardiyalar (I1, I2, I3) aktif
            shift_order["I1"] = shift_schedule.get("I1", [])
            shift_order["I2"] = shift_schedule.get("I2", [])
            shift_order["I3"] = shift_schedule.get("I3", [])

        return shift_order

    def get_sorted_time_intervals(self):
        # Tüm TimeInterval objelerini topla
        all_time_intervals = []
        for date_obj in self.dates:
            for time_interval in date_obj.time_intervals:
                # TimeInterval objesine tarih bilgisini ekle
                time_interval.date = date_obj.date
                all_time_intervals.append(time_interval)

        # TimeInterval objelerini önce tarihe, ardından saat bilgisine göre sırala
        sorted_time_intervals = sorted(
            all_time_intervals,
            key=lambda ti: (ti.date, ti.interval[0])  # Önce tarih, ardından saat
        )

        return sorted_time_intervals


class Date:
    def __init__(self):
        self.time_intervals = []  # TimeInterval objelerini tutan liste
        self.date = None

    def get_date(self):
        return self.date


class TimeInterval:
    def __init__(self):
        self.interval = None  # Zaman aralığı (örneğin, (time(8, 0, 0), time(10, 0, 0)))
        self.shift = None  # Vardiya (örneğin, "I1", "I2", "I3")
        self.assignments = []  # (jig, product, operation, workers)
        self.available_workers = None
        self.assignable_operations = None
        self.date = None  # Tarihi tutacak değişken
        
    def set_assignable_operations(self, _ops):
        self.assignable_operations = _ops

    def get_assignable_operations(self):
        return self.assignable_operations

    def get_interval(self):
        return self.interval

    def get_assignments(self):
        return self.assignments

    def get_shift_intervals(self, worker, date, shift):
        for entry in worker.get_shift_schedule():
            if entry[0] == date and entry[1] == shift:
                return entry[2]  # available_hours
        return []
    def get_available_workers(self):
        return self.available_workers

    def get_shift(self):
        return self.shift
        
    def get_date(self):
        return self.date










