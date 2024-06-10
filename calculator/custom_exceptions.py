class ValueEntryError(Exception):
    def __str__(self):
        return 'Value entry error'


class UnknownOperation(Exception):
    def __str__(self):
        return 'Unknown operation'
