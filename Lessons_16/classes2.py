class Car:
    colors = ['Orange', 'Cyan', 'Granate']
    def __init__(self, colors):
        self.colors = colors

    def organize(self):
        self._specific_organize()

    def _specific_organize(self): #'_' перед назвою показує, що це прихований метод, що має використовуватись в середині класу
        raise NotImplementedError


class Track(Car):
    def _specific_organize(self):
        self.colors.reverse()
        print(self.colors)

class Cabriolet(Car):
    def _specific_organize(self):
        self.colors = [color.lower() for color in self.colors]
        print(self.colors)


class Minivan(Car):
    def _specific_organize(self):
        self.colors = [color.upper() for color in self.colors]
        print(self.colors)

class Outlander(Car):
    def _specific_organize(self):
        self.colors = sorted(self.colors)
        print(self.colors)


new_track = Track(['blue', 'Red', 'green', 'BLACK', 'yellow'])
new_minivan = Minivan(['blue', 'Red', 'green', 'BLACK', 'yellow'])
new_cabriolet = Cabriolet(['blue', 'Red', 'green', 'BLACK', 'yellow'])
new_outlander = Outlander(['blue', 'Red', 'green', 'BLACK', 'yellow'])

new_track.organize()
new_minivan.organize()
new_cabriolet.organize()
new_outlander.organize()
