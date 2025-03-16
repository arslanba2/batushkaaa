class Product:
    def __init__(self, serial_number):
        self.__serial_number = serial_number if serial_number else None  # (str) Mainscreeen'da kullanıcıdan alınır
        self.__operations = []  # (Holds operation objects) ExcelDataLoader yükler
        self.__current_jig = None  # (Holds jig object) Mainscreen'da kullanıcıdan alınır,
        self.__progress = None  # (float) MainController hesaplar-yazar
        self.__critical_operations = []  # (list of critical operation objects)

    def get_serial_number(self):
        return self.__serial_number

    def add_operation(self, operation):
        self.__operations.append(operation)

    def get_operations(self):
        return self.__operations

    def set_current_jig(self, jig):
        self.__current_jig = jig  # kullacıdan alınacak jig buraya getirilecek

    def get_current_jig(self):
        return self.__current_jig

    def get_operation_by_name(self, op_name):
        for operation in self.__operations:
            if op_name == operation.get_name():
                return operation

    def set_progress(self, _progress):
        self.__progress = _progress

    def get_progress(self):
        return self.__progress

    def append_critical_operations(self, _critical_ops):
        self.__critical_operations = _critical_ops

    def get_critical_operations(self):
        return self.__critical_operations


def create_product(productList, serial_number):
    product_object = Product(serial_number)  # seri numaraya göre product objesi oluştur
    productList.append(product_object)  # oluşan product objesini listeye ekle
