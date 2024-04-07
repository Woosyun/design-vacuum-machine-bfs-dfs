import pygame
import random
from collections import deque  
from collections import OrderedDict

pygame.init()

# Screen dimensions
screen_width = 300
screen_height = 300

# Grid and Cell size dimensions
cell_size = 60  # Adjusted for 20x20 grid to fit in the 600x600 window
grid_width = 5
grid_height = 5

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
light_blue = (173, 216, 230) 
yellow = (255, 255, 0)  

# Set up the display
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Vacuum Cleaner')

# Load and scale the vacuum cleaner icon
vacuum_icon = pygame.image.load('vacuum_icon.png')
vacuum_icon = pygame.transform.scale(vacuum_icon, (cell_size, cell_size))
# Load and scale the dirt icon
dirt_icon = pygame.image.load('dust_icon.png')
dirt_icon = pygame.transform.scale(dirt_icon, (cell_size, cell_size))

# Initialize exactly eight unique dirt positions
dirt_positions = set()
cleaned_positions = set()  
while len(dirt_positions) < 5:
    dirt_positions.add((random.randint(0, grid_width - 1), random.randint(0, grid_height - 1)))


class VacuumCleaner:
    def __init__(self):
        self._position = (random.randint(0, grid_width - 1), random.randint(0, grid_height - 1))
        
        self.visited = OrderedDict()

    def location_sensor(self):
        """Returns the current position of the vacuum as a tuple, acting as the location sensor."""
        return self._position

    def dirt_sensor(self):
        """Checks if there is dirt at the vacuum's current position, acting as the dirt sensor."""
        return self.location_sensor() in dirt_positions

    def position_to_label(self, position):
        row, col = position
        return col + 1 + row * grid_width

    def actuator_BFS(self):
        starting_label = self.position_to_label(self.location_sensor())
        print(f"Starting position: {starting_label}")
        
        screen.fill(black)  # Clear screen
        draw_grid_and_vacuum()  # Redraw grid with new vacuum position
        pygame.display.flip()  # Update display
        pygame.time.delay(1000) # Slow down the movement for visualization
        
        # TODO 
        # You only need to fill out actuator_BFS part.
        # You don't need to use other libraries because every library you need is already implemented.
        # Check your anaconda env before you launch this program.
        # Use OrderedDict() to store visited location.
        
        # For each iteration, you should update screen.
        # You must use below code snippet for EVERY ITERATION to successfully implement Coding Assignment.
        '''
            screen.fill(black)
            draw_grid_and_vacuum()
            pygame.display.flip()
            pygame.time.delay(500)
        '''
        
        # Also, You need to print out Current Vacuum Position, Whether you sucked dirt, etc. Below is code snippet related to them.
        '''
            print(f"Current Vacuum Position: {self.position_to_label({current Position of Vacuum})}")
        '''
        '''
            print(f"Sucked dirt at: {self.position_to_label({current Position of Vacuum})}")
        '''
        
        # Write your code below here
        running = True
        while running:
            screen.fill(black)
            draw_grid_and_vacuum()
            pygame.display.flip()
            pygame.time.delay(500)
            print(f"Current Vacuum Position: {self.position_to_label(self._position)}")
        
        
        # Write your code above here.

def draw_grid_and_vacuum():
    for x in range(grid_height):
        for y in range(grid_width):
            rect = pygame.Rect(y * cell_size, x * cell_size, cell_size, cell_size)
            if (x, y) in cleaned_positions:  # Check if the cell has been cleaned
                pygame.draw.rect(screen, yellow, rect)  # Fill cleaned cell with yellow
            elif (x, y) in vacuum.visited:  # Check if the cell is visited
                pygame.draw.rect(screen, light_blue, rect)  # Fill visited cell with light blue
            else:
                pygame.draw.rect(screen, white, rect, 1)  # Draw border for unvisited cells
            if (x, y) in dirt_positions:
                screen.blit(dirt_icon, (y * cell_size, x * cell_size))
    
    vacuum_pos = vacuum.location_sensor()
    screen.blit(vacuum_icon, (vacuum_pos[1] * cell_size, vacuum_pos[0] * cell_size))

vacuum = VacuumCleaner()

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    vacuum.actuator_BFS()
    if not dirt_positions:
        break

pygame


