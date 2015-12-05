#
#   Created By Nate Bosscher
#

from PIL import Image
import glob, os
from island import Island
import sys

island_limit = 100

im = Image.open("input.jpg")
sz = im.size
width = sz[0]
height = sz[1]
im.putalpha(1)

def get_bw_pixel_value(px):
    avg = (px[0] + px[1] + px[2]) / 3
    if avg > 90:
        return (255, 255, 255, 255)
    else: 
        return (0, 0, 0, 0)

def convert_to_bw(im):
    sz = im.size
    width = sz[0]
    height = sz[1]
    
    for j in range(0,height):
        for i in range(0,width):
            im.putpixel((i,j), get_bw_pixel_value(im.getpixel((i, j))))


class RemoveIslands:
    def __init__(self, im):
        self.islands = []
        self.status = 0
        sz = im.size
        width = sz[0]
        height = sz[1]
        print "Scanning for islands..."

        for j in range(0,height):
            self.update_status(j, height)
            for i in range(0,width):
                if im.getpixel((i,j))[0] == 255:
                    if not self.pixel_already_part_of_island((i,j)):
                        self.process_island(im, (i,j))
    
    def process_island(self, im, coord):
        island = Island(im, coord)
        if island.get_area() < island_limit:
            self.delete_region(im, island)
        else:
            self.islands.append(Island(im, coord))

    def delete_region(self, im, island):
        for coord in island.coords:
            im.putpixel(coord, (0,0,0,0))

    def update_status(self, i, total):
        sys.stdout.write("\n{}/{}\t{} Islands".format(i, total, len(self.islands)))
        sys.stdout.flush()
    def pixel_already_part_of_island(self, coord):
        for island in self.islands:
            sys.stdout.write("+")
            sys.stdout.flush()
            if island.contains_coord(coord):
                return True
        return False


convert_to_bw(im)
RemoveIslands(im)
im.save("out.png", "PNG")
