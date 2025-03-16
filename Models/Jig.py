class Jig:
    def __init__(self, _name):
        self.__name = _name  # (str) ExcelDataLoader yükler
        self.__applicable_operations = None  # ExcelDataLoader yükler
        self.__state = None  # (bool value if in use: True) Kullanıcan product eklenirken düzenlenir,
        self.__assigned_product = None  # (holds product object) Kullanıcıdan product eklenirken düzenlenir,
        self.__max_assigned_worker = 4
        self.__number_of_assigned_workers = 0

    def get_name(self):
        return self.__name

    def set_applicable_operations(self, _applicableOperations):
        self.__applicable_operations = _applicableOperations

    def get_applicable_operations(self):
        return self.__applicable_operations

    def set_state(self, _state):
        self.__state = _state

    def get_state(self):
        return self.__state

    def set_assigned_product(self, _assigned_product):
        self.__assigned_product = _assigned_product

    def get_assigned_product(self):
        return self.__assigned_product

    def get_max_assigned_worker(self):
        return self.__max_assigned_worker

    def get_number_of_assigned_workers(self):
        return self.__number_of_assigned_workers

def create_jig(jigList, name):
    for jigObject in jigList:
        if jigObject.get_name() == name:
            return
    jig_object = Jig(name)  # jig objesi oluştur
    jigList.append(jig_object)  # oluşan jig objesini listeye ekle
