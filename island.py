#
#   Created by Nate Bosscher
#
import sys

class Island:
    def __init__(self, im, coord):
        self.coords = set([])
        self.get_island(im, coord)

    def pixel_is_white(self,im,coord):
        if coord[0] < 0 or coord[1] < 0:
            return False
        if not (coord[0] < im.size[0] and coord[1] < im.size[1]):
            return False
         
        if im.getpixel(coord)[0] == 255:
            return coord
        else:
            return False
    
    def contains_coord(self, coord):
        return True if coord in self.coords else False

    '''
        does island touch this island
    '''
    def touches(self, island):
        for coord in self.coords:
            if coord in island.coords:
               return True
        return False

    ''' 
        append coords from island to this island
    '''
    def append(self, island):
        for coord in island.coords:
            self.coords.add(coord)
    
    '''
        check box around pixel to search for white coords
        return a list of coords or False
    '''
    def get_touching_white_pixels(self,im,coord):
        pxs = []
        val = self.pixel_is_white(im, (coord[0]-1, coord[1]+1))
        if val != False:
            pxs.append(val)
        val = self.pixel_is_white(im, (coord[0], coord[1]+1))
        if val != False:
            pxs.append(val)
        val = self.pixel_is_white(im, (coord[0]+1, coord[1]+1))
        if val != False:
            pxs.append(val)
        val = self.pixel_is_white(im, (coord[0]-1, coord[1]))
        if val != False:
            pxs.append(val)
        val = self.pixel_is_white(im, (coord[0]+1, coord[1]))
        if val != False:
            pxs.append(val)
        val = self.pixel_is_white(im, (coord[0]-1, coord[1]-1))
        if val != False:
            pxs.append(val)
        val = self.pixel_is_white(im, (coord[0], coord[1]-1))
        if val != False:
            pxs.append(val)
        val = self.pixel_is_white(im, (coord[0]+1, coord[1]-1))
        if val != False:
            pxs.append(val)
        return pxs

    def get_area(self):
        return len(self.coords)
    
    '''
        start at coord and if it's white follow that group of white
        until it's size is greater than island_limit
    '''
    def get_island(self,im,coord):
        if im.getpixel(coord)[0] == 0:
            return False
        
        whitect = 0
        offset = 0
        done = set([])
        todo = [coord]
        while len(todo) > 0:
            sys.stdout.write("-")
            sys.stdout.flush()
            nextItr = set([])
            for coord in todo: # find border pixels for pixels in todo list, add found ones into list for the next iteration if we haven't counted them already
                for _coord in self.get_touching_white_pixels(im, coord):
                    if _coord not in done:
                        nextItr.add(_coord)
                done.add(coord) # add to done list because it's been completed
            todo = [] # update todo list
            for coord in nextItr:
                todo.append(coord)
        self.coords = done
        sys.stdout.write("\n")
