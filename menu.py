from library import*
import json
import click
from click_shell import shell


@shell(prompt='Garden > ', intro='Starting simulation...')
def main():
    global garden
    garden = Garden()
    garden.get_data_from_file()
    click.echo("Вечера")
    garden.show()
    garden.next_day()
    garden.set_data_in_file()
    click.echo("Сегодня")
    garden.show()

@main.command()
def add_bed():
    garden.add_garden_bed()
    garden.set_data_in_file()
    garden.show()

@main.command(help = 'Plant tree: apple or pear')
@click.argument('type')
def plant_tree(type):
    garden.plant_tree(type)
    garden.set_data_in_file()
    garden.show()

@main.command(help = 'Plant cultivated plant (tomato, potato or pepper) in garden bed №...')
@click.argument('type')
@click.argument('count')
def plant_cult(type, count):
    garden.plant_cultivated_plant(type, int(count) - 1)
    garden.set_data_in_file()
    garden.show()

@main.command(help = 'Watering cultivated plant in garden bed №...')
@click.argument('count')
def watering(count):
    garden.watering(int(count) - 1)
    garden.set_data_in_file()
    garden.show()

@main.command(help = 'Fertilize cultivated plant in garden bed №...')
@click.argument('count')
def fertilize(count):
    garden.fertilize(int(count) - 1)
    garden.set_data_in_file()
    garden.show()

@main.command(help = 'Kill pest on plant (cult or tree) in garden bed №... or on tree №...')
@click.argument('type')
@click.argument('count')
def kill_pest(type, count):
    garden.kill_pest(type, int(count) - 1)
    garden.set_data_in_file()
    garden.show()

@main.command(help = 'Treatment on plant (cult or tree) in garden bed №... or on tree №...')
@click.argument('type')
@click.argument('count')
def treatment(type, count):
    garden.treatment(type, int(count) - 1)
    garden.set_data_in_file()
    garden.show()

@main.command(help = 'Weeding cultivated plant in garden bed №...')
@click.argument('count')
def weeding(count):
    garden.weeding(int(count) - 1)
    garden.set_data_in_file()
    garden.show()

@main.command(help = 'Harvesting on plant (cult or tree) in garden bed №... or on tree №...')
@click.argument('type')
@click.argument('count')
def harvesting(type, count):
    garden.harvesting(type, int(count) - 1)
    garden.set_data_in_file()
    garden.show()


if __name__ == '__main__':
    main()
