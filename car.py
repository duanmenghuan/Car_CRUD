def main():
    while True:
        menu()
        choice=int(input('请输入您想选择的操作：'))
        if choice in [0,1,2,3,4,5,6,7]:
            if choice==0:
                answer=input('您确认要退出系统嘛？Y/N:')
                if answer=='Y':
                    break
                else:
                    continue
            elif choice == 1:
                insert()
            elif choice == 2:
                search()
            elif choice == 3:
                delete()
            elif choice == 4:
                modify()
            elif choice == 5:
                sort()
            elif choice == 6:
                total()
            elif choice == 7:
                show()
def menu():
    print('==============================车辆信息管理系统==============================')
    print('---------------------------------功能菜单----------------------------------')
    print('\t\t\t\t\t\t1.录入车辆信息')
    print('\t\t\t\t\t\t2.查找车辆信息')
    print('\t\t\t\t\t\t3.删除车辆信息')
    print('\t\t\t\t\t\t4.修改车辆信息')
    print('\t\t\t\t\t\t5.排序')
    print('\t\t\t\t\t\t6.统计车辆总车数')
    print('\t\t\t\t\t\t7.读取车辆信息')
    print('\t\t\t\t\t\t0.退出')
    print('-------------------------------------------------------------------------')

def insert():
    lis = []
    while True:
        id = input('请输入ID(如1001):')
        if not id:
            break
        name = input('请输入车辆名称:')
        if not name:
            break
        try:
            colour = input('请输入车辆颜色：')
            price = eval(input('请输入车辆价格:'))
        except:
            print('您输入的信息无效！不是整数类型，请重新输入')
            continue
        # 将录入的车辆信息保存到字典中
        lis1 = {'id': id, 'name': name, 'colour': colour, 'price': price,}
        # 将车辆信息添加到列表中
        lis.append(lis1)
        answer = input('是否继续添加？y/n')
        if answer == 'y':
            continue
        else:
            break
    # 调用sava（）函数，保存列表中的内容
    save(lis)
    print('车辆信息已录入完毕！')


def save(l):
    try:
        stu_txt = open('car.txt', 'a', encoding='utf-8')
    except:
        stu_txt = open('car.txt', 'w', encoding='utf-8')
    for item in l:
        stu_txt.write(str(item) + '\n')
    stu_txt.close()


def search():
    car_query = []
    while True:
        id = ''
        name = ''
        if os.path.exists('car.txt'):
            mode = input('按ID查找请输入1，按车辆查找请输入2：')
            if mode == '1':
                id = input('请输入车辆ID')
            elif mode == '2':
                name = input('请输入车辆名称')
            else:
                print('您的输入有误，请重新输入')
                search()
            with open('car.txt', 'r', encoding='utf-8') as rfile:
                car = rfile.readlines()  # 按行读取所有内容
                for item in car:
                    d = dict(eval(item))
                    if id != '':
                        if d['id'] == id:
                            car_query.append(d)
                    elif name != '':
                        if d['name'] == name:
                            car_query.append(d)
            show_car(car_query)  # 显示查询结果
            car_query.clear()  # 清空列表
            answer = input('是否要继续查询？y/n\n')
            if answer == 'y':
                continue
            else:
                break
        else:
            print('暂未保存车辆信息')
            return


def show_car(lst):
    if len(lst) == 0:
        print('没有查询到车辆信息，无数据显示！！！')
        return
    # 定义标题显示格式
    format_title = '{:^6}\t{:^12}\t{:^8}\t{:^10}'
    print(format_title.format('ID', '车辆名称', '颜色', '价格'))
    # 定义内容的显示模式
    format_data = '{:^6}\t{:^12}\t{:^8}\t{:^10}'
    for item in lst:
        print(format_data.format(item.get('id'),
                                 item.get('name'),
                                 item.get('colour'),
                                 item.get('price'),
                                 ))


import  os
def delete():
    while True:
        stu_id = input('请输入要删除的车辆ID:')
        if stu_id != '':  # 判断stu_id是否输入了ID
            if os.path.exists('car.txt'):  # 判断磁盘上有没有filename这个文件，判断这个文件是否存在
                with open('car.txt', 'r', encoding='utf-8') as file:
                    stu_old = file.readlines()
            else:
                stu_old = []
            flag = False  # 用来标记数据是否删除
            if stu_old:
                with open('car.txt', 'w', encoding='utf-8') as wfile:
                    d = {}  # 将删除数据之后的字典存进磁盘文件中
                    for item in stu_old:
                        d = dict(eval(item))  # 将字符串类型转成字典
                        if d['id'] != stu_id:
                            wfile.write(str(d) + '\n')
                        else:
                            flag = True
                    if flag:
                        print(f'id为{stu_id}的车辆信息已被删除')  # 格式化字符串
                    else:
                        print(f'没有找到id为{stu_id}的车辆信息')
            else:
                print('无车辆信息！')
                break
            show()  # 重新显示车辆信息
            answer = input('是否继续删除？y/n')
            if answer == 'y':
                continue
            else:
                break
def modify():
    show()
    if os.path.exists('car.txt'):
        with open('car.txt', 'r', encoding='utf-8') as rfile:
            stu_old = rfile.readlines()
    else:
        return
    car_id = input('请输入要修改的车辆ID:')
    if car_id != '':
        with open('car.txt', 'w', encoding='utf-8') as wfile:
            for item in stu_old:  # 遍历从文件当中读取的车辆信息
                d = dict(eval(item))
                if d['id'] == car_id:
                    print('找到车辆信息，可以进行修改他的关联信息了！')
                    while True:
                        try:
                            d['name'] = input('请输入车辆名称：')
                            d['colour'] = input('请输入车辆颜色：')
                            d['price'] = input('请输入车辆价格：')
                        except:
                            print('您的输入有误，请重新输入！！！')
                        else:
                            break
                    wfile.write(str(d) + '\n')
                    print('修改成功！！！')
                else:
                    wfile.write(str(d) + '\n')
            answer = input('是否继续修改其他车辆信息?y/n')
            if answer == 'y':
                modify()
def sort():
    show()
    car_new = []
    if os.path.exists('car.txt'):
        with open('car.txt', 'r', encoding='utf-8') as rfile:
            car = rfile.readlines()
            for item in car:
                car_new.append(dict(eval(item)))
    else:
        return
    asc_or_desc = input('请选择{0:升序 1:降序}：')
    if asc_or_desc == '0':
        asc_or_desc_bool = False
    elif asc_or_desc == '1':
        asc_or_desc_bool = True
    else:
        print('您的输入有误，请重新输入')
        sort()
    mode = input('请选择排序方式（1，按车辆价格排序):')
    if mode == '1':
        car_new.sort(key=lambda x: int(x['price']), reverse=asc_or_desc_bool)
    else:
        print('您的输入有误，请重新输入！！！')
        sort()
    show_car(car_new)    
def total():
    if os.path.exists('car.txt'):
        with open('car.txt', 'r', encoding='utf-8') as rfile:
            car = rfile.readlines()
            if car:
                print(f'一共有{len(car)}俩汽车')
            else:
                print('还没有录入汽车6信息')
    else:
        print('暂未保存数据信息...')

def show():
    car_lst = []
    if os.path.exists('car.txt'):
        with open('car.txt', 'r', encoding='utf-8') as rfile:
            car = rfile.readlines()
            for item in car:
                car_lst.append(eval(item))
            if car_lst:
                show_car(car_lst)
    else:
        print('暂未保存过数据')


if __name__ == '__main__':
    main()
