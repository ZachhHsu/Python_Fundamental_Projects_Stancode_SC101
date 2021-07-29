"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

YOUR DESCRIPTION HERE:
This program will visualize the rank for the trend of various baby names' popularity.
Users could input different names in the "Search" box to find available names,
or input in the "Names" box to retrieve the graphical result(Line graph).
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    interval_width = (width - 2*GRAPH_MARGIN_SIZE) / len(YEARS)             # equal width for each year interval
    x_coordinate = GRAPH_MARGIN_SIZE + year_index * interval_width
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')                                                    # delete all existing lines from the canvas

    # Create horizontal lines
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,
                       CANVAS_WIDTH-GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE)

    # Create vertical lines
    for i in range(len(YEARS)):
        vertical_x = get_x_coordinate(CANVAS_WIDTH, i)
        canvas.create_line(vertical_x, 0, vertical_x, CANVAS_HEIGHT)

        # Label years below the lower horizontal line
        year_x = get_x_coordinate(CANVAS_WIDTH, i) + TEXT_DX
        canvas.create_text(year_x, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text=YEARS[i], anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)                                                # draw the fixed background grid

    # Dictionary that stores x and y coordinates to draw line graphs
    line_dict = {}

    # Loop over input names
    for i in range(len(lookup_names)):
        if lookup_names[i] in name_data:                                    # make sure the name is in outer dictionary

            # Assign different colors for different names
            color = COLORS[i - len(COLORS)*(i//len(COLORS))]

            # Create text for names and ranks
            for year, rank in name_data[lookup_names[i]].items():           # loop over key-value pairs
                for j in range(len(YEARS)):                                 # loop over different years

                    # Determine x coordinate
                    x_coordinate = get_x_coordinate(CANVAS_WIDTH, j) + TEXT_DX

                    # Differentiate whether certain year is in the inner dictionary
                    if str(YEARS[j]) in name_data[lookup_names[i]]:

                        # Determine y coordinate and draw the text
                        if int(year) == YEARS[j]:                           # make sure each year is given the text once
                            rank_interval = (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) / MAX_RANK
                            y_coordinate = GRAPH_MARGIN_SIZE + rank_interval * int(rank)
                            canvas.create_text(x_coordinate, y_coordinate,
                                               text=lookup_names[i] + ' ' + rank, anchor=tkinter.SW, fill=color)

                            # Include x and y coordinates for line graphs
                            line_dict[YEARS[j]] = {x_coordinate: y_coordinate}

                    # Mark the rank '*' if the year is not in the inner dictionary(out of rank 1000)
                    else:
                        y_coordinate = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                        canvas.create_text(x_coordinate, y_coordinate,
                                           text=lookup_names[i] + ' *', anchor=tkinter.SW, fill=color)

                        # Include x and y coordinates for line graphs
                        line_dict[YEARS[j]] = {x_coordinate: y_coordinate}

            # Create line graphs
            for k in range(len(YEARS)-1):                                   # ensure lines won't go beyond the last year
                for start_x, start_y in line_dict[YEARS[k]].items():        # start point
                    for end_x, end_y in line_dict[YEARS[k+1]].items():      # end point
                        canvas.create_line(start_x, start_y, end_x, end_y, width=LINE_WIDTH, fill=color)


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
