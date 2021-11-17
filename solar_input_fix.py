# coding: utf-8
# license: GPLv3

from solar_objects import Star, Planet


def read_space_objects_data_from_file(input_filename):
    """Cчитывает данные о космических объектах из файла, создаёт сами объекты
    и вызывает создание их графических образов

    Параметры:

    **input_filename** — имя входного файла
    """

    objects = []
    with open(input_filename) as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue  # пустые строки и строки-комментарии пропускаем
            object_type = line.split()[0].lower()
            if object_type == "star":  # DONE // FIXME: do the same for planet
                star = Star()
                parse_star_parameters(line, star)
                objects.append(star)
            elif object_type == "planet":
                planet = Planet()
                parse_planet_parameters(line, planet)
                objects.append(planet)
            else:
                print("Unknown space object")

    return objects


def parse_star_parameters(line, star):
    """Считывает данные о звезде из строки.
    Входная строка должна иметь слеюущий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты зведы, (Vx, Vy) — скорость.
    Пример строки:
    Star 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описанием звезды.
    **star** — объект звезды.
    """

    r, color, m, x, y, Vx, Vy = line.split()[1], str(line.split()[2]), line.split()[3], \
                                line.split()[4], line.split()[5], line.split()[6], line.split()[7]
    star.r(r)
    star.c(color)
    star.m(m)
    star.x(x)
    star.y(y)
    star.Vx(Vx)
    star.Vy(Vy)

    # DONE // FIXME: not done yet...

def parse_planet_parameters(line, planet):
    """Считывает данные о планете из строки.
    Предполагается такая строка:
    Входная строка должна иметь слеюущий формат:
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты планеты, (Vx, Vy) — скорость.
    Пример строки:
    Planet 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание планеты.
    **planet** — объект планеты.
    """

    r, color, m, x, y, Vx, Vy = line.split()[1], str(line.split()[2]), line.split()[3], \
                                line.split()[4], line.split()[5], line.split()[6], line.split()[7]
    planet.r(r)
    planet.c(color)
    planet.m(m)
    planet.x(x)
    planet.y(y)
    planet.Vx(Vx)
    planet.Vy(Vy)

    # DONE // FIXME: not done yet...


def write_space_objects_data_to_file(output_filename, space_objects):
    """Сохраняет данные о космических объектах в файл.
    Строки должны иметь следующий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Параметры:

    **output_filename** — имя входного файла
    **space_objects** — список объектов планет и звёзд
    """
    with open(output_filename, 'w') as out_file:
        line = []
        for obj in space_objects:
            print(out_file, "%s %d %s %f" % ('1', 2, '3', 4.5))
            if obj.type == "star":
                line.append("Star")
            elif obj.type == "planet":
                line.append("Planet")
            line.append(obj.r)
            line.append(obj.color)
            line.append(obj.m)
            line.append(obj.x)
            line.append(obj.y)
            line.append(obj.Vx)
            line.append(obj.Vy)
            out_file.write(
                line[0] + " " + line[1] + " " + line[2] + " " + line[3] + " " + line[4] + " "
                + line[5] + " " + line[6] + " " + line[7] + "\n"
            )
            # DONE // FIXME: should store real values


if __name__ == "__main__":
    print("This module is not for direct call!")
