import os
import zipfile
import xml.etree.ElementTree as ET

file_path = r"c:\Users\구매팀\Desktop\삼성AI컨설팅\2026하반기과제\재고의정도생성기\기초자료정리본\담당자별 목표 재고 일수.xlsx"

print(f"File size: {os.path.getsize(file_path)} bytes")

try:
    with zipfile.ZipFile(file_path, 'r') as z:
        shared_strings = []
        if 'xl/sharedStrings.xml' in z.namelist():
            ss_data = z.read('xl/sharedStrings.xml')
            root = ET.fromstring(ss_data)
            ns = {'ns': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
            for si in root.findall('ns:si', ns):
                t = si.find('ns:t', ns)
                if t is not None:
                    shared_strings.append(t.text if t.text else '')
                else:
                    text_parts = []
                    for r_el in si.findall('ns:r', ns):
                        t_el = r_el.find('ns:t', ns)
                        if t_el is not None and t_el.text:
                            text_parts.append(t_el.text)
                    shared_strings.append(''.join(text_parts))
        
        if 'xl/worksheets/sheet1.xml' in z.namelist():
            sheet_data = z.read('xl/worksheets/sheet1.xml')
            root = ET.fromstring(sheet_data)
            ns = {'ns': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
            
            rows = []
            for row in root.findall('.//ns:row', ns):
                row_data = []
                for c in row.findall('ns:c', ns):
                    v_el = c.find('ns:v', ns)
                    v = v_el.text if v_el is not None else None
                    t = c.get('t')
                    
                    if t == 's' and v is not None:
                        val = shared_strings[int(v)]
                    elif v is not None:
                        val = v
                    else:
                        val = ''
                    row_data.append(val)
                rows.append(row_data)
            
            print("--- Sheet1 Content ---")
            for idx, r in enumerate(rows[:30]):
                print(f"Row {idx+1}: {r}")
except Exception as e:
    print(f"Error parsing with zipfile: {e}")
