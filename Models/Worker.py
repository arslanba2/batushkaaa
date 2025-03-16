from datetime import datetime


class Worker:
    def __init__(self):
        self.__registration_number = None  # (str)ExcelDataLoader yükler
        self.__fullName = None  # (str) ExcelDataLoader yükler
        self.__skills = None  # (list of str) ExcelDataLoader yükler
        self.__restrictions = None  # (list of operation object) ExcelDataLoader yükler
        self.__shift_schedule = None  # list(date, shift, available_hours) ExcelDataLoader yükler, AddOffDays günceller
        self.__off_days = None  # (start_off_date, end_off_date) Kullanıcıdan AddOffDays ile alınır
        self.__assignments = None  # [product_serial, operation_name, start[date, time], end[date, time]]

    def set_registration_number(self, _registrationNumber):
        self.__registration_number = _registrationNumber

    def get_registration_number(self):
        return self.__registration_number

    def set_name(self, _fullName):
        self.__fullName = _fullName

    def get_name(self):
        return self.__fullName

    def set_skills(self, _skills):
        self.__skills = _skills

    def get_skills(self):
        return self.__skills

    def set_restrictions(self, _restrictions):
        self.__restrictions = _restrictions

    def get_restrictions(self):
        return self.__restrictions

    def set_shift_schedule(self, _shiftSchedule):
        self.__shift_schedule = _shiftSchedule

    def get_shift_schedule(self):
        return self.__shift_schedule

    def set_off_days(self, _off_days):
        self.__off_days = _off_days

    def get_off_days(self):
        return self.__off_days

