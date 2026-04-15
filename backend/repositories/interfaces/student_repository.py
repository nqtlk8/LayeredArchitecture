from abc import ABC, abstractmethod

class IStudentRepository(ABC):

    @abstractmethod
    def get_student_by_id(self, student_id):
        pass

    @abstractmethod
    def get_subjects_by_student(self, student_id):
        pass

    @abstractmethod
    def get_class_by_student(self, student_id):
        pass