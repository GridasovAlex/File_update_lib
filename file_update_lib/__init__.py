import zipfile
import hashlib
import shutil
import os
import urllib.request


def download_file(zip_url, file_name):
    """Скачивает архив по прямой ссылке

    Args:
        zip_url (str): ссылка на архив
        file_name (str): имя, которой будет иметь архив, после загрузки(путь)

    Return: путь до сохраненного файла
    """
    urllib.request.urlretrieve(zip_url, file_name)
    return(file_name)


def unpacking(file_name, path):
    """Распаковывает архив в определенную папку

    Args:
        file_name (str): имя файла
        path (str): путь, куда распаковать

    Return: путь до распакованного файла (файлов)
    """
    with zipfile.ZipFile(file_name, "r") as myzip:
        myzip.extractall(path=path)
    return(path)


def calculate_checksum(file_path):
    """Pассичтывает контрольную сумму файла по переданному пути

    Args:
        file_path (str): путь до файла, чью контрольную сумму необходимо рассчитать

    Return: контрольную сумму
    """
    with open(file_path, 'rb') as file:
        hash = hashlib.md5(file.read()).hexdigest()
    return(hash)


def overwrite_file(or_file_path, overw_file_path):
    """Перезаписывает файл на новый, при условии равенства разрешений

    Args:
        or_file_path (str): путь до нового файла, на который юудет производиться перезапись
        overw_file_path (str): путь до файла, котрый необходимо преезаписать

    Return: путь до преезаписанного файла
    """
    if (or_file_path[-3::] != overw_file_path[-3::]): # проверяем разрешение файла
        print("Не совпадают разрешения файлов")
        return None
    else:
        shutil.copyfile(or_file_path, overw_file_path)
        return(overw_file_path)


def multi_checksum(path):
    """Выводит контрольную сумму всех файлов в папке на экран,
    при условии, что в папке нет других папок

    Args:
        path (str): Путь до папки, контрольную сумму файлов которой нам нужно вывести
    """

    if os.path.isfile(path):
        with open(path, 'rb') as file:
            hash = hashlib.md5(file.read()).hexdigest()
        print(f"{path}: {hash}")
    else:
        file_names = os.listdir(path)
        for name in file_names:
            if os.path.isfile(path+ "\\" +name):
                with open(path+ "\\" +name , 'rb') as file:
                    hash = hashlib.md5(file.read()).hexdigest()
                print(f"{name}: {hash}")
            else:
                multi_checksum(path+ "\\" +name)
    return None


def create_archive(folder_path, archive_path):
    """Создает архив

    Args:
        folder_path (str): путь до папки(файла), которую необходимо заархивировать
        archive_path (str): путь до места, куда сохраняем архив
    """
    if os.path.isfile(folder_path):
        with zipfile.ZipFile(archive_path, "w") as myzip:
            myzip.write(folder_path)
    else:
        list_file_names = os.listdir(folder_path)
        with zipfile.ZipFile(archive_path, "w") as myzip:
            for name in list_file_names:
                myzip.write(folder_path + "//" + name)
    return(archive_path)
