# coding:utf-8
import xlrd


class HandleExcel:
    index_name_origin = 2
    index_name = 4
    index_sex = 5
    index_age = 6
    index_id_number = 7
    index_phone_number = 8
    index_address = 9
    index_street_name = 10
    index_relation = 11
    """封装操作excel的方法"""
    def __init__(self, file, sheet_id=0):
        self.file = file
        self.sheet_id = sheet_id
        self.data = self.get_data()
        self.refresh_index()
        # 为了在创建一个实例时就获得excel的sheet对象，可以在构造器中调用get_data()
        # 因为类在实例化时就会自动调用构造器，这样在创建一个实例时就会自动获得sheet对象了

    # 获取某一页sheet对象
    def get_data(self):
        data = xlrd.open_workbook(self.file)
        sheet = data.sheet_by_index(self.sheet_id)
        return sheet

    # 获取某一页sheet对象
    def refresh_index(self):
        col_count = self.get_cols()
        for col in range(0, col_count):
            value = self.get_value(1, col)
            if value == '关联病例':
                self.index_name_origin = col
            elif value == '姓名':
                self.index_name = col
            elif value == '性别':
                self.index_sex = col
            elif value == '年龄':
                self.index_age = col
            elif value == '身份证':
                self.index_id_number = col
            elif value == '电话':
                self.index_phone_number = col
            elif value == '现住址':
                self.index_address = col
            elif value == '街道':
                self.index_street_name = col
            elif value == '接触方式':
                self.index_relation = col

    # 获取excel数据行数
    def get_rows(self):
        rows = self.data.nrows
        return rows

    # 获取excel数据列数
    def get_cols(self):
        rows = self.data.ncols
        return rows

    # 获取某个单元格数据
    def get_value(self, row, col):
        ctype = self.data.cell(row, col).ctype
        value = self.data.cell_value(row, col)
        if ctype == 2 and value % 1 == 0.0:  # ctype为2且为浮点数
            value = int(value)
        return str(value)

    # 向某个单元格写入数据
    def write_value(self):
        pass


if __name__ == '__main__':
    test = HandleExcel("./xxx.xls")
    print(test.get_data())
    print(test.get_rows())
    print(test.get_value(0, 0))

