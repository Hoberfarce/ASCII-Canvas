# Define the size of the canvas
CANVAS_WIDTH = 20
CANVAS_HEIGHT = 10

# Create the canvas as a 2D array of spaces
canvas = [[' ' for y in range(CANVAS_HEIGHT)] for x in range(CANVAS_WIDTH)]

# Print the canvas to the console
def print_canvas():
    for y in range(CANVAS_HEIGHT):
        for x in range(CANVAS_WIDTH):
            print(canvas[x][y], end='')
        print()

# Draw a point on the canvas at the specified coordinates
def draw_point(x, y, char='*'):
    if x < 0 or x >= CANVAS_WIDTH or y < 0 or y >= CANVAS_HEIGHT:
        return  # ignore out-of-bounds points
    canvas[x][y] = char

# Clear the canvas by resetting all the points to spaces
def clear_canvas():
    for y in range(CANVAS_HEIGHT):
        for x in range(CANVAS_WIDTH):
            canvas[x][y] = ' '

# Main loop for the app
while True:
    # Print the canvas and get user input
    print_canvas()
    command = input('Enter command (e.g., p 5 3): ')

    # Parse the command and execute it
    parts = command.split()
    if len(parts) == 0:
        continue
    if parts[0] == 'p':
        if len(parts) < 3:
            continue
        x = int(parts[1])
        y = int(parts[2])
        char = parts[3] if len(parts) > 3 else '*'
        draw_point(x, y, char)
    elif parts[0] == 'c':
        clear_canvas()
    elif parts[0] == 'q':
        break  # quit the app
