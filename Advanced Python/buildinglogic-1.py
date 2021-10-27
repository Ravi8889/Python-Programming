def area_triangle(base, height):
    return 1/2* base*height;

def read_file(file_path):
    items =[]
    with open(file_path,'r')as f:
        for line in f:
            base, height =line.split(',')
            height= height.replace('\n','')
            if base.isnumeric() and height.isnumeric():
                items.append({
                    'base':float(base),
                    'height':float(base)
                })
    return items

def find_area(file_path):
    items =read_file(file_path)
    for item in items:
        area =area_triangle(item['base'],item['height'])
        print(f"base : {item['base']},height: {item['height']},area:{area}")
        
if __name__ == '__main__':
    find_area("sample.csv");