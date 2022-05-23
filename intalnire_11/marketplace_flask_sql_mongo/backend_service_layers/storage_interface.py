from abc import ABC, abstractmethod


class StorageInterface(ABC):

    @abstractmethod
    def create_item(self, *args, **kwargs):
        pass

    @abstractmethod
    def list_items(self, *args, **kwargs):
        pass

    @abstractmethod
    def delete_item(self, *args, **kwargs):
        pass

    @abstractmethod
    def get_item(self, *args, **kwargs):
        pass
