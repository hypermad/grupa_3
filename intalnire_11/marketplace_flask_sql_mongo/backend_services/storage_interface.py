from abc import ABC, abstractmethod


class StorageInterface(ABC):

    @abstractmethod
    def create_user(self):
        pass

    @abstractmethod
    def list_users(self):
        pass

    @abstractmethod
    def delete_user(self):
        pass

    @abstractmethod
    def update_user(self):
        pass

    @abstractmethod
    def get_user(self):
        pass
