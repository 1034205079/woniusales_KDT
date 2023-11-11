import openpyxl


class ReadExcleCase(object):
    def __init__(self, case_file):
        self.case_file = case_file
        self.wb = openpyxl.load_workbook(self.case_file)

    def read_by_sheet(self, sheetname):
        """根据sheetname读取用例"""
        sheet = self.wb[sheetname]
        sheet_values = list(sheet.values)
        sheet_header = sheet_values[0]
        sheet_data = sheet_values[1:]
        case_list = []  # 存储用例的列表，每个用例是一个字典
        for row in sheet_data:
            if row[0] is not None:
                new_case = {header: value for header, value in zip(sheet_header, row)}
                new_case[sheet_header[5]] = []  # 每个用例的步骤用列表送入
                case_list.append(new_case)  # 保存用例信息
            new_step = [step_info for step_info in row[5:] if step_info is not None]
            new_case[sheet_header[5]].append(new_step)  # 把用例加入步骤

        return case_list

    def read_all_sheets(self):
        """读取所有sheet中的用例"""
        all_sheet_names = self.wb.sheetnames
        case_all_sheet = []
        for sheet_name in all_sheet_names:
            case_all_sheet.extend(self.read_by_sheet(sheet_name))  # 因为read_by_sheet返回的是列表，所以这边要extend展开
        return case_all_sheet


if __name__ == '__main__':
    file = "../cases/API.xlsx"
    rec = ReadExcleCase(file)
    print(rec.read_by_sheet("test_login_api"))
