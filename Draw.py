# -*- coding: utf-8 -*-

import random
import xlrd

class Draw():
    def __init__(self):
        self.in_plates = []
        pass
    
    def gen_plates(self, num):
        char_list = 'ABCDEFGHIJKLMNPQRSTUVWXYZ'
        digit_list = '0123456789'
        plates = []
        for i in range(num):
            plate = "渝" + random.choice(list('ABCDFGH')) + random.choice(char_list+digit_list) + random.choice(char_list+digit_list) + random.choice(digit_list) + random.choice(digit_list) + random.choice(digit_list)
            plates.append(plate)
        
        return plates
    
    def read_plates(self, file_name):
        plates = []
        with open(file_name, 'r') as f:
            plate = f.readline()
            while plate:
                plates.append(plate.strip())
                plate = f.readline()
        return plates
        
    def write_plates(self, out_plates, file_name):
        with open(file_name, 'w') as f:
            for i in range(len(out_plates)):
                f.write(out_plates[i] + '\n')
        
    def draw_plates(self, in_plates, num):
        out_plates = []
        for i in range(num):
            plate = random.choice(in_plates)
            in_plates.remove(plate)
            out_plates.append(plate)
        return out_plates
    
    def copy_xls(self, old_file, new_file):
        from xlutils.copy import copy
        old_xls = xlrd.open_workbook(old_file)
        new_xls = copy(old_xls)
        new_xls.save(new_file)
    
    def modify_plates(self, file_name):
        in_workbook = xlrd.open_workbook(file_name)
        in_sheet = in_workbook.sheet_by_index(0)
        out_workbook = copy(in_workbook)
        out_sheet = out_workbook.get_sheet(0)
        
        for i in range(1, in_sheet.nrows):
            plate_0 = str(in_sheet.cell(i, 0).value)
            plate_2 = str(in_sheet.cell(i, 2).value)
            plate_0 = self.pre_plate(plate_0)
            plate_2 = self.pre_plate(plate_2)
            if self.right_plate(plate_0) and self.right_plate(plate_2):
                out_sheet.write(i, 0, plate_0)
                out_sheet.write(i, 2, plate_2)
            else:
                print (plate_0, plate_2)
                out_sheet.write(i, in_sheet.ncols + 1, "错误车牌")
            out_sheet.write(i, in_sheet.ncols, i)
        
        out_workbook.save(file_name.split('.')[0] + '_mod.xls')
        
    def pre_plate(self, plate):
        plate = plate.strip()
        plate = plate.replace(' ', '')
        plate = plate.replace(';', '')
        plate = plate.replace('.', '')
        plate = plate.replace('亅', 'J')
        plate = plate.replace('·', '')
        plate = plate.replace('一', '')
        plate = plate.replace('Ⅴ', 'V')
        plate = plate.replace('丫', 'Y')
        
        
        for c in plate:
            if ord(c) in range(65297, 65313 + 26):
                plate = plate.replace(c, chr(ord(c) - 65248))
                
        return plate
    
    def right_plate(self, plate):
        pat_plate = re.compile('^[川新鲁浙渝贵苏云鄂豫琼][A-Z0-9]{6}')
        return pat_plate.match(plate)

if __name__ == "__main__":
    draw = Draw()
    in_plates = draw.gen_plates(2000)
    draw.write_plates(in_plates, 'a.txt')
    print (draw.read_plates('a.txt'))
    #out_plates = draw.draw_plates(in_plates, 100)
    #print(out_plates)
