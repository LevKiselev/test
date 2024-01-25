import os

import sys

import requests

import pygame

server_address = "https://static-maps.yandex.ru/1.x/"

params = {

    "l": "map",

    "spn": "0.12,0.12",

    "pl": "c:0077F5FF,w:5," +

    "30.3141676,59.9419749," +

    "30.3135324,59.9427766," +

    "30.3131731,59.9434688," +

    "30.3102389,59.9445046," +

    "30.3019238,59.9461243," +

    "30.2960658,59.9463929," +

    "30.2864528,59.9484131," +

    "30.2746081,59.951916," +

    "30.2672482,59.9556119," +

    "30.260725,59.9579753," +

    "30.2421856,59.9601667," +

    "30.2330875,59.9630024," +

    "30.2203846,59.9641194," +

    "30.2058792,59.9649357," +

    "30.1744667,59.9622124," +

    "30.150261,59.9581042," +

    "30.1334381,59.9556978," +

    "30.1186782,59.9522698," +

    "30.0942993,59.9460706," +

    "30.0682068,59.9386762," +

    "30.0383377,59.9304202," +

    "30.0251186,59.9267218," +

    "30.0125885,59.9226783," +

    "29.9748069,59.9098603," +

    "29.9325943,59.8973755," +

    "29.9138832,59.8918218"

}

map_file = "map.png"

screen_size = (600, 450)

response = requests.get(server_address, params=params)

if not response:

    print("HTTP status:", response.status_code, "(", response.reason, ")")

    sys.exit(1)

with open(map_file, "wb") as f:

    f.write(response.content)

pygame.init()

screen = pygame.display.set_mode(screen_size)

screen.blit(pygame.image.load(map_file), (0, 0))

pygame.display.flip()

os.remove(map_file)

while pygame.event.wait().type != pygame.QUIT:

    pass

pygame.quit()

