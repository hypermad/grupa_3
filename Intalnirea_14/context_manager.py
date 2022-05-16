"""
Varianta uzuala
"""
with open('some_file_1.txt', 'w') as opened_file:
    opened_file.write('Hola!')

"""
Alternativa
"""
file = open('some_file_2.txt', 'w')
try:
    file.write('Hola!')
finally:
    file.close()

"""
Implementare specifica
"""


class File(object):
    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)

    def __enter__(self):
        return self.file_obj

    def __exit__(self, type, value, traceback):
        self.file_obj.close()

    # metoda de exit daca returneaza True atunci orice exceptie este prinsa din interiorul context managerului
    # def __exit__(self, type, value, traceback):
    #     print("Exception has been handled")
    #     self.file_obj.close()
    #     return True


with File('demo.txt', 'w') as opened_file:
    opened_file.write('Hola!')
    # opened_file.ceva_ce_nu_este_definit('Hola!')

