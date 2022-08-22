import os
import shutil


def quotes_appender():
    file_path = '/home/danyldo/Загрузки/whatismybrowser-user-agent-database.txt'
    dir_path = '/home/danyldo/Загрузки'
    with open(file_path) as i:  # open file for reading, i = input file
        with open(dir_path + "temp.txt", "w") as o:  # open temp file in write mode, o = output
            for l in i:  # read line by line
                o.write("'%s'\n" % l[:-1])  # concate ' and text
                #       ^  ^ added `'` for each line
    os.remove(file_path)  # delete old file. Note:this is not needed in postfix system
    os.rename(dir_path + "temp.txt", file_path)  # rename file


def company_name_appender():
    dir_name = '/home/danyldo/Изображения/gfg/raw images/exchange'
    subfolders = [f.path for f in os.scandir(dir_name) if f.is_dir()]

    for sub in subfolders:

        for f in os.listdir(sub):
            os.rename(sub + "/" + f, sub + "/" + os.path.basename(sub) + "_" + f)

            # filename, file_extension = os.path.splitext(sub + "/" + f)


def annotation_index_changer():
    os.chdir('/home/danyldo/p_List/dev/annotation_index_changer/test')
    for paths, folders, files in os.walk(os.getcwd()):
        for file in files:
            if file.endswith("txt"):
                reading_file = open(file, "r")
                new_str = ""
                for line in reading_file:
                    new_line = (line[0].replace(line[0], '9') + line[1:])
                    new_str += new_line
                writing_file = open(file, "w")
                writing_file.write(new_str)
                writing_file.close()


def delete_a_few_files():
    dir_name = '/home/danyldo/p_List/learn/new/lra/dataset/resnet50/test'
    subfolders = [f.path for f in os.scandir(dir_name) if f.is_dir()]

    for sub in subfolders:
        i = 0
        for f in os.listdir(sub):
            if i == 20:
                break
            src = os.path.join(sub, f)
            os.remove(src)
            i += 1


def insert_files_into_folders():
    dir_name = '/home/danyldo/p_List/dev/archive/logo_recognition/logo'
    files = os.listdir(dir_name)
    for i in files:
        os.mkdir(os.path.join(dir_name, i.split(".")[0]))
        shutil.move(os.path.join(dir_name, i), os.path.join(dir_name, i.split(".")[0]))


def extract_files_from_directories():
    dir_name = '/home/danyldo/Изображения/gfg/yolov5/images/train'
    subfolders = [f.path for f in os.scandir(dir_name) if f.is_dir()]

    for sub in subfolders:
        for f in os.listdir(sub):
            src = os.path.join(sub, f)
            dst = os.path.join(dir_name, f)
            shutil.move(src, dst)
        shutil.rmtree(sub)


if __name__ == "__main__":
    k = int(input(
        "Введите тип действия: \n1. Создать для каждого изображения директорию\n2. Вытащить изображения из "
        "директорий\n3. Удалить несколько файлов\n4. Изменить индексы аннотаций\n5. Изменить названия\n6. Добавить "
        "кавычки "
        "картинок\nДействие: "))
    match k:
        case 1:
            insert_files_into_folders()
        case 2:
            extract_files_from_directories()
        case 3:
            delete_a_few_files()
        case 4:
            annotation_index_changer()
        case 5:
            company_name_appender()
        case 6:
            quotes_appender()
        case _:
            print("Такой опции нет")
