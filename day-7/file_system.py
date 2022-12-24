class Item:
    def __init__(self, name, is_dir=False):
        self.name = name
        self.is_directory = is_dir

    def __repr__(self):
        return self.name


class Directory(Item):
    def __init__(self, name: str, parent: Item):
        super().__init__(name, True)
        self.items = []
        self.parent = parent

    def __repr__(self):
        return f'Directory(name={self.name})'

    def add_item(self, item: Item):
        self.items.append(item)

    def get_item(self, name: str):
        return next((item for item in self.items if item.name == name), None)

    def get_parent(self):
        return self.parent

    @property
    def size(self):
        return sum([item.size for item in self.items])


class File(Item):
    def __init__(self, name, size):
        super().__init__(name, False)
        self.size = size
