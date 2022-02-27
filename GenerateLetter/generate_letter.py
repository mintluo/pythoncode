# coding:utf-8

import os
import shutil
import sys
import re
import datetime
import logging

from docxtpl import DocxTemplate
from win32com.client import Dispatch

from handle_excel import *

# 日志输出到console
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)  # 指定被处理的信息级别为最低级DEBUG，低于level级别的信息将被忽略
# 日志输出到file
# 不拆分日志文件，a指追加模式,w为覆盖模式
fh = logging.FileHandler("log_%s.txt" % (datetime.datetime.now().strftime('%Y%m%d')), mode='a', encoding='utf-8')
fh.setLevel(logging.DEBUG)

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.addHandler(ch)
logger.addHandler(fh)


def get_date(add_day):
    now = datetime.datetime.today() + datetime.timedelta(days=add_day)
    time = now.timetuple()
    result = str(time.tm_mon) + '月' + str(time.tm_mday) + '日'
    return result


def doc2pdf(input_file):
    # word = Dispatch('Word.Application')
    word = Dispatch('kwps.Application')
    doc = word.Documents.Open(input_file, ReadOnly=1)
    doc.SaveAs(input_file.replace(".docx", ".pdf"), FileFormat=17)
    doc.Close()
    word.Quit()


def backup_files(source, destination):
    if not os.path.exists(destination):
        os.mkdir(destination)
    shutil.move(source, destination)


def do_generate_letter(list_docx_row, series_no, save_dir):
    final_street_name = list_docx_row[0]['street_name']
    if len(list_docx_row) > 3:
        final_name = '{}、{}等{}人'.format(list_docx_row[0]['name'], list_docx_row[1]['name'], len(list_docx_row))
    elif len(list_docx_row) <= 0:
        return
    else:
        final_name = '、'.join([i['name'] for i in list_docx_row])
    # 整个模板的数据
    data_docx = {
        'street_name': final_street_name,
        'name': final_name,
        'name_origin': list_docx_row[0]['name_origin'],
        'series': series_no,
        'cur_date': get_date(0),
        'cur_date_add2': get_date(2),
        'cur_date_add6': get_date(6),
        'cur_date_add7': get_date(7),
        'alerts': list_docx_row
    }
    doc = DocxTemplate('./template/t.docx')  # 加载模板文件
    doc.render(data_docx)  # 填充数据
    letter_name = '关于做好涉疫人员管控的函（{}{}）{}.docx'.format(final_street_name, final_name, series_no)
    target_file_name = save_dir + letter_name
    doc.save(target_file_name)
    doc2pdf(target_file_name)


class GenerateLetter:
    def __init__(self, file):
        self.data = HandleExcel(file)  # 实例化操作excel文件类

    def prepare_template_excel_data(self):
        list_docx_row = []
        rows_count = self.data.get_rows()  # 获取excel行数
        for row in range(5, rows_count):  # 利用行数进行迭代处理每个接口
            street_name = self.data.get_value(row, self.data.index_street_name)
            if len(street_name) == 0:  # 过滤掉空行
                break
            if not street_name.endswith('街道'):
                street_name = street_name + '街道'
            name = self.data.get_value(row, self.data.index_name)
            name_origin = self.data.get_value(row, self.data.index_name_origin)
            sex = self.data.get_value(row, self.data.index_sex)
            age = self.data.get_value(row, self.data.index_age)
            id_number = self.data.get_value(row, self.data.index_id_number)
            phone_number = self.data.get_value(row, self.data.index_phone_number)
            address = self.data.get_value(row, self.data.index_address)
            relation = self.data.get_value(row, self.data.index_relation)
            # 模板中excel每行的数据
            data_dic = {
                'street_name': street_name,
                'name': name,
                'name_origin': name_origin,
                'sex': sex,
                'age': age,
                'id_number': id_number,
                'phone_number': phone_number,
                'address': address,
                'relation': relation,
            }
            list_docx_row.append(data_dic)
        return list_docx_row

    def write_template(self, series_no, source_file):
        save_dir = '{}/涉疫人员管控函_{}/'.format(sys.path[0], get_date(0))
        if not os.path.exists(save_dir):
            os.mkdir(save_dir)
        logger.info('[{}][{}] is processing!'.format(series_no, source_file))
        list_docx_row = self.prepare_template_excel_data()
        do_generate_letter(list_docx_row, series_no, save_dir)
        source = '{}/{}'.format(sys.path[0], source_file)
        destination = save_dir + '转运单原始材料'
        backup_files(source, destination)
        logger.info('[{}][{}] finished!'.format(series_no, source_file))


if __name__ == '__main__':
    key_work = '转运单'
    # series = input("please enter the first series: ")
    series = '0226046'
    cur_dir_file_names = [fs for fs in os.listdir() if fs.endswith(('.xlsx', 'xls'))]
    file_names_sorted = sorted(cur_dir_file_names, key=lambda i: int(re.match(r'(\d+)', i).group()))
    count = 0
    for current_file in file_names_sorted:
        if key_work in current_file:
            excel = GenerateLetter(current_file)
            excel.write_template(str(series).zfill(7), current_file)
            series = int(series) + 1
            count = count + 1
    logger.info('{} letters have generated!'.format(count))
