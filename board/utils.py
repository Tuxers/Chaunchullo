import uuid
import os

def save_uploaded_file(f):
    path = '/home/donkeysharp/tmp/'
    file_name, fileExtension = os.path.splitext(f.name)
    file_name = ''.join(uuid.uuid1().__str__().split('-')) + fileExtension

    with open(path + file_name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

    return file_name
