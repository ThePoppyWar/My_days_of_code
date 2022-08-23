from datetime import datetime


class HouseProject:
    number_of_floors = 2
    area = 100

    def describe_project():
        print(f"Area: {HouseProject.area} m2.")  
        print(f"Number of floats: {HouseProject.number_of_floors}")

print(HouseProject.__dict__)

HouseProject.describe_project()

print("-----------------------------------------Foto--------------------------------------------------------")

class Foto:

    execution_time = datetime.now().strftime("%H:%M:%S")
    fname = 'image_' + execution_time + '.png'

    def currtery_time():
        return datetime.now().strftime("%H:%M:%S")

print(Foto.execution_time)
print(Foto.fname)
print("------------------------------------------------------------------------------------")
foto = Foto()
print(foto.execution_time)
print(Foto.currtery_time())

print(Foto.__mro__)
