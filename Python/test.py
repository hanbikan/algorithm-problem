def main():
    # a 4 x 4 cell
    #_4x4_Cells = ["CSSS","SSCC","CCCC","CCCC"]
    #_4x4_Cells = ["CWGC","SSWG","CWCW","CCSS"]
    _4x4_Cells = ["CGGG","GGCC","CCCC","CCCC"]
    
    Links = [
        "1110000000000000", # button 0
        "0001000101010000", # button 1
        "0000100000100011", # button 2
        "1000111100000000", # button 3
        "0000001110101000", # button 4
        "1010000000000011", # button 5
        "0001000000000011", # button 6
        "0000110100000011", # button 7
        "0111110000000000", # button 8
        "0001110000000100", # button 9
    ]
    
    pyslot(_4x4_Cells, Links)


def convert_4x4_cells(_4x4_Cells):
    new_cells = []
    for row in _4x4_Cells:
        new_row = []
        for cell in row:
            cell_index = convert_cell_to_cell_index(cell)
            new_row.append(cell_index)
        new_cells.append(new_row)
    
    return new_cells

# C, G, S, W -> 0, 1, 2, 3
def convert_cell_to_cell_index(cell):
    if cell == 'C': return 0
    elif cell == 'G': return 1
    elif cell == 'S': return 2
    else: return 3

def create_buttons_to_positions(Links):
    buttons_to_positions = []
    for link in Links:
        positions = get_positions_from_link(link)
        buttons_to_positions.append(positions)
    
    return buttons_to_positions

# "1110000000000000" -> [[0,0], [0,1], [0,2]]
def get_positions_from_link(link):
    result = []
    for i in range(len(link)):
        if link[i] == '1':
            result.append([i // 4, i % 4])
    
    return result


def press_button(cells, button_positions):
    for x, y in button_positions:
        cells[x][y] = (cells[x][y] + 1) % 4

def cancel_press_button(cells, button_positions):
    for x, y in button_positions:
        cells[x][y] = (cells[x][y] + 3) % 4

def is_big_jackpot(cells):
    for row in cells:
        for cell in row:
            if cell != 0: return False
    return True

def deepcopy(row):
    return [row[i] for i in range(len(row))]


def dfs(index):
    global min_combination_length, pressed_at_min_combination_length, cells, buttons_to_positions, pressed

    for i in range(index, len(buttons_to_positions)):
        if pressed[i] >= 3: continue
        
        # Back tracking
        press_button(cells, buttons_to_positions[i])
        pressed[i] += 1

        # Check big jackpot and update values
        if is_big_jackpot(cells):
            if sum(pressed) < min_combination_length:
                min_combination_length = sum(pressed)
                pressed_at_min_combination_length = deepcopy(pressed)
            return
        
        dfs(i)
        cancel_press_button(cells, buttons_to_positions[i])
        pressed[i] -= 1
        

def pyslot(_4x4_Cells, Links):
    global min_combination_length, pressed_at_min_combination_length, cells, buttons_to_positions, pressed

    # Preprocessing: Convert _4x4_Cells and Links to cells and buttons_to_positions
    cells = convert_4x4_cells(_4x4_Cells)
    if is_big_jackpot(cells):
        print("Big Jackpot!!: []")
        return
    buttons_to_positions = create_buttons_to_positions(Links)

    # Solution
    min_combination_length = float('inf')
    # Ex) [0, 0, 2, 0, 1, 0, 0, 0, 0, 0] means that button 2's pressed 2 times and button 4's pressed one time
    pressed_at_min_combination_length = None
    pressed = [0] * 10
    dfs(0)

    if pressed_at_min_combination_length == None:
        print("Opps")
    else:
        # Convert pressed_at_min_combination_length
        # Ex) [1, 1, 0, 1, 0, 2, 3, 1, 0, 0] → [0, 1, 3, 5, 5, 6, 6, 6, 7]
        result = []
        for i in range(len(pressed_at_min_combination_length)):
            for _ in range(pressed_at_min_combination_length[i]):
                result.append(i)
        print("Big Jackpot!!:", result)

main()