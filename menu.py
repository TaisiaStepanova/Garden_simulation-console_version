from library import*
import json

garden = Garden()
garden.get_data_from_file()


def menu() -> None:
    print("Вечера")
    garden.show()
    garden.next_day()
    print("Сегодня")
    command = ['add_bed', 'plant_tree', 'plant_cult', 'watering', 'fertilize', 'kill_pest', 'treatment', 'weeding', 'harvesting', 'exit']
    while True:
        garden.show()
        choice = str(input())
        choice = choice.strip()
        if choice == command[0]:
            garden.add_garden_bed()
        elif choice.startswith(command[1], 0, -1):
            tmp = choice.split(" ", 1)
            garden.plant_tree(tmp[1])
        elif choice.startswith(command[2], 0, -1):
            tmp = choice.split(" ", 2)
            garden.plant_cultivated_plant(tmp[1], int(tmp[2]) - 1)
        elif choice.startswith(command[3], 0, -1):
            tmp = choice.split(" ", 1)
            garden.watering(int(tmp[1]) - 1)
        elif choice.startswith(command[4], 0, -1):
            tmp = choice.split(" ", 1)
            garden.fertilize(int(tmp[1]) - 1)
        elif choice.startswith(command[5], 0, -1):
            tmp = choice.split(" ", 2)
            garden.kill_pest(tmp[1], int(tmp[2]) - 1)
        elif choice.startswith(command[6], 0, -1):
            tmp = choice.split(" ", 2)
            garden.treatment(tmp[1], int(tmp[2]) - 1)
        elif choice.startswith(command[7], 0, -1):
            tmp = choice.split(" ", 1)
            garden.weeding(int(tmp[1]) - 1)
        elif choice.startswith(command[8], 0, -1):
            tmp = choice.split(" ", 2)
            garden.harvesting(tmp[1], int(tmp[2]) - 1)
        elif choice == command[9]:
            return
        else:
            print('WRONG INPUT!')
        garden.set_data_in_file()


menu()
