class DataStorage:
    status = 'disconnected'
    content = None

    def __init__(self, path_file: str):
        self.__path_file = path_file

    def _create_storage(self):
        file = open(self.__path_file, 'w')
        file.close()
        print('создал новый файл')
        return file

    def connect(self):
        while True:
            try:
                file = open(self.__path_file, 'r')
                print('открыл файл на чтение')
                DataStorage.status = 'connected'
                DataStorage.content = file.read()
                print(file)
                print(DataStorage.content)
                return file
            except FileNotFoundError:
                DataStorage._create_storage(self)

    def disconnect(self, file):
        file.close()
        print('закрыл файл')


class DataStorageWrite(DataStorage):

    def __init__(self, path_file: str):

        super().__init__(path_file)
        self.file = None
        self.__path_file = path_file

    def connect(self):
        while True:
            try:
                file = open(self.__path_file, 'r+')
                print('открыл файл на чтение и дозапись')
                DataStorageWrite.status = 'connected'
                DataStorageWrite.content = file.read()
                self.file = file
                return file
            except FileNotFoundError:
                DataStorageWrite._create_storage(self)

    def append(self, new_content: str):
        self.file.write(new_content)
        DataStorageWrite.content += new_content

    def disconnect(self):
        print(DataStorageWrite.content)
        self.file.close()
        print(self.file)
        print('закрыл файл')
