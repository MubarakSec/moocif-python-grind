def print_layers(layers):
    size = 2 * layers - 1
    for i in range(size):
        row = []
        # Loop over every column in the current row
        for j in range(size):
            # Calculate minimum distance to any edge of the square
            layer_index = min(i, j, size - 1 - i, size - 1 - j)
            
            # Convert layer_index to the corresponding letter
            # The ord converts the letter into ASCII code
            # The chr coverts forom ASCII into letter
            # Outer layer is 'A' + (layers - 1), inner layers go down by 1 letter each step
            letter = chr(ord('a') + (layers - 1) - layer_index)
            
            # Add the letter to the current row
            row.append(letter)
        
        # Join all letters in the row into a string and print it 
        print(''.join(row))

layers = int(input("Layers: "))
print_layers(layers)
#XD
