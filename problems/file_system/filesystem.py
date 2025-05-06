from abc import ABC, abstractmethod
from datetime import datetime

class FileSystem(ABC):
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def display(self):
        pass

    @abstractmethod
    def search(self, keyword: str) -> list:
        pass


class File(FileSystem):
    def __init__(self, filename: str, createdTime: datetime = None):
        super().__init__(filename)
        self.filename = filename
        self.createTime = createdTime or datetime.now()

    def display(self):
        print('     ' + f'-File: {self.filename} (Created: {self.createTime})')

    def search(self, keyword: str) -> list:
        if keyword.lower() in self.filename.lower():
            return [self]
        return []


class Directory(FileSystem):
    def __init__(self, name: str):
        super().__init__(name)
        self.children = []
    
    def add(self, component: FileSystem):
        self.children.append(component)
    
    def delete(self, component: FileSystem):
        self.children.remove(component)

    def display(self):
        print('     ' + f'-Directory: {self.name}')
        for child in self.children:
            child.display()

    def search(self, keyword: str) -> list:
        results = []
        for child in self.children:
            results.extend(child.search(keyword))
        return results