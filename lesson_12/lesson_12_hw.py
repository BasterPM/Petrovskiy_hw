class DataStorage:
    status = 'disconnected'
    content = None

    def __init__(self, path_file: str):
        self.__path_file = path_file

    def _create_storage(self):
        file = open(self.__path_file, 'w')
        file.close()
        return file

    def connect(self):
        while True:
            try:
                file = open(self.__path_file, 'r')
                self.status = 'connected'
                self.content = file.read()
                return file
            except FileNotFoundError:
                self._create_storage()

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
                self.status = 'connected'
                self.content = file.read()
                self.file = file
                return file
            except FileNotFoundError:
                self._create_storage()

    def append(self, new_content: str):
        self.file.write(new_content)
        self.content += new_content

    def disconnect(self):
        print(self.content)
        self.file.close()
        print('закрыл файл')
