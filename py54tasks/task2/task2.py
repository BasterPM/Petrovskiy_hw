class Kettle:
    def __init__(self, volume):
        if not isinstance(volume, int):
            raise TypeError('Volume must be an integer')
        if volume < 300:
            raise ValueError('volume cannot be less than 300 ml')
        self.volume = volume

    def __repr__(self):
        start = '|******************|\n'
        conclusion = start
        for i in range(int(self.volume // 100)):
            if i <= 2:
                conclusion += '|                  |' + ('*' * (2 - i) + '/\n')
            else:
                conclusion += '|                  |\n'
        end = '|******************|'
        conclusion += end
        return f'{conclusion}'

