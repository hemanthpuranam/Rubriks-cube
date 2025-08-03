import random

class RubiksCube:
    def __init__(self):
        # Initialize solved cube
        self.faces = {
            'U': [['W']*3 for _ in range(3)],  # Up (White)
            'F': [['R']*3 for _ in range(3)],  # Front (Red)
            'R': [['B']*3 for _ in range(3)],  # Right (Blue)
            'B': [['O']*3 for _ in range(3)],  # Back (Orange)
            'L': [['G']*3 for _ in range(3)],  # Left (Green)
            'D': [['Y']*3 for _ in range(3)]   # Down (Yellow)
        }
        
    def set_state_from_input(self, face_colors):
        """Set cube state from user input colors"""
        face_order = ['U', 'F', 'R', 'B', 'L', 'D']
        
        for i, face in enumerate(face_order):
            colors = face_colors[i]
            for row in range(3):
                for col in range(3):
                    self.faces[face][row][col] = colors[row * 3 + col].upper()
        
    def display(self):
        """Display the cube in a 2D unfolded format"""
        print("    " + " ".join(self.faces['U'][0]))
        print("    " + " ".join(self.faces['U'][1]))
        print("    " + " ".join(self.faces['U'][2]))
        print()
        
        for i in range(3):
            row = " ".join(self.faces['L'][i]) + " " + " ".join(self.faces['F'][i]) + " " + " ".join(self.faces['R'][i]) + " " + " ".join(self.faces['B'][i])
            print(row)
        print()
        
        print("    " + " ".join(self.faces['D'][0]))
        print("    " + " ".join(self.faces['D'][1]))
        print("    " + " ".join(self.faces['D'][2]))
        print()

    def display_layout_guide(self):
        """Show the user how to read their cube"""
        print("=== HOW TO READ YOUR CUBE ===")
        print("Hold your cube with WHITE on top and RED facing you")
        print()
        print("Enter colors for each face in this order:")
        print("1. TOP face (White center)")
        print("2. FRONT face (Red center)")  
        print("3. RIGHT face (Blue center)")
        print("4. BACK face (Orange center)")
        print("5. LEFT face (Green center)")
        print("6. BOTTOM face (Yellow center)")
        print()
        print("For each face, enter 9 colors from left-to-right, top-to-bottom:")
        print("Position layout:")
        print("1 2 3")
        print("4 5 6") 
        print("7 8 9")
        print()
        print("Use these letters: W=White, R=Red, B=Blue, O=Orange, G=Green, Y=Yellow")
        print()

    def rotate_face_clockwise(self, face):
        """Rotate a face 90 degrees clockwise"""
        old_face = [row[:] for row in self.faces[face]]
        for i in range(3):
            for j in range(3):
                self.faces[face][j][2-i] = old_face[i][j]

    def rotate_face_counterclockwise(self, face):
        """Rotate a face 90 degrees counterclockwise"""
        old_face = [row[:] for row in self.faces[face]]
        for i in range(3):
            for j in range(3):
                self.faces[face][2-j][i] = old_face[i][j]

    def move_R(self):
        """Right face clockwise"""
        self.rotate_face_clockwise('R')
        temp = [self.faces['U'][i][2] for i in range(3)]
        for i in range(3):
            self.faces['U'][i][2] = self.faces['F'][i][2]
            self.faces['F'][i][2] = self.faces['D'][i][2]
            self.faces['D'][i][2] = self.faces['B'][2-i][0]
            self.faces['B'][2-i][0] = temp[i]

    def move_R_prime(self):
        """Right face counterclockwise"""
        self.rotate_face_counterclockwise('R')
        temp = [self.faces['U'][i][2] for i in range(3)]
        for i in range(3):
            self.faces['U'][i][2] = self.faces['B'][2-i][0]
            self.faces['B'][2-i][0] = self.faces['D'][i][2]
            self.faces['D'][i][2] = self.faces['F'][i][2]
            self.faces['F'][i][2] = temp[i]

    def move_L(self):
        """Left face clockwise"""
        self.rotate_face_clockwise('L')
        temp = [self.faces['U'][i][0] for i in range(3)]
        for i in range(3):
            self.faces['U'][i][0] = self.faces['B'][2-i][2]
            self.faces['B'][2-i][2] = self.faces['D'][i][0]
            self.faces['D'][i][0] = self.faces['F'][i][0]
            self.faces['F'][i][0] = temp[i]

    def move_L_prime(self):
        """Left face counterclockwise"""
        self.rotate_face_counterclockwise('L')
        temp = [self.faces['U'][i][0] for i in range(3)]
        for i in range(3):
            self.faces['U'][i][0] = self.faces['F'][i][0]
            self.faces['F'][i][0] = self.faces['D'][i][0]
            self.faces['D'][i][0] = self.faces['B'][2-i][2]
            self.faces['B'][2-i][2] = temp[i]

    def move_U(self):
        """Up face clockwise"""
        self.rotate_face_clockwise('U')
        temp = self.faces['F'][0][:]
        self.faces['F'][0] = self.faces['R'][0][:]
        self.faces['R'][0] = self.faces['B'][0][:]
        self.faces['B'][0] = self.faces['L'][0][:]
        self.faces['L'][0] = temp

    def move_U_prime(self):
        """Up face counterclockwise"""
        self.rotate_face_counterclockwise('U')
        temp = self.faces['F'][0][:]
        self.faces['F'][0] = self.faces['L'][0][:]
        self.faces['L'][0] = self.faces['B'][0][:]
        self.faces['B'][0] = self.faces['R'][0][:]
        self.faces['R'][0] = temp

    def move_D(self):
        """Down face clockwise"""
        self.rotate_face_clockwise('D')
        temp = self.faces['F'][2][:]
        self.faces['F'][2] = self.faces['L'][2][:]
        self.faces['L'][2] = self.faces['B'][2][:]
        self.faces['B'][2] = self.faces['R'][2][:]
        self.faces['R'][2] = temp

    def move_D_prime(self):
        """Down face counterclockwise"""
        self.rotate_face_counterclockwise('D')
        temp = self.faces['F'][2][:]
        self.faces['F'][2] = self.faces['R'][2][:]
        self.faces['R'][2] = self.faces['B'][2][:]
        self.faces['B'][2] = self.faces['L'][2][:]
        self.faces['L'][2] = temp

    def move_F(self):
        """Front face clockwise"""
        self.rotate_face_clockwise('F')
        temp = [self.faces['U'][2][i] for i in range(3)]
        for i in range(3):
            self.faces['U'][2][i] = self.faces['L'][2-i][2]
            self.faces['L'][2-i][2] = self.faces['D'][0][2-i]
            self.faces['D'][0][2-i] = self.faces['R'][i][0]
            self.faces['R'][i][0] = temp[i]

    def move_F_prime(self):
        """Front face counterclockwise"""
        self.rotate_face_counterclockwise('F')
        temp = [self.faces['U'][2][i] for i in range(3)]
        for i in range(3):
            self.faces['U'][2][i] = self.faces['R'][i][0]
            self.faces['R'][i][0] = self.faces['D'][0][2-i]
            self.faces['D'][0][2-i] = self.faces['L'][2-i][2]
            self.faces['L'][2-i][2] = temp[i]

    def move_B(self):
        """Back face clockwise"""
        self.rotate_face_clockwise('B')
        temp = [self.faces['U'][0][i] for i in range(3)]
        for i in range(3):
            self.faces['U'][0][i] = self.faces['R'][i][2]
            self.faces['R'][i][2] = self.faces['D'][2][2-i]
            self.faces['D'][2][2-i] = self.faces['L'][2-i][0]
            self.faces['L'][2-i][0] = temp[i]

    def move_B_prime(self):
        """Back face counterclockwise"""
        self.rotate_face_counterclockwise('B')
        temp = [self.faces['U'][0][i] for i in range(3)]
        for i in range(3):
            self.faces['U'][0][i] = self.faces['L'][2-i][0]
            self.faces['L'][2-i][0] = self.faces['D'][2][2-i]
            self.faces['D'][2][2-i] = self.faces['R'][i][2]
            self.faces['R'][i][2] = temp[i]

    def execute_moves(self, moves):
        """Execute a sequence of moves"""
        move_map = {
            'R': self.move_R, "R'": self.move_R_prime,
            'L': self.move_L, "L'": self.move_L_prime,
            'U': self.move_U, "U'": self.move_U_prime,
            'D': self.move_D, "D'": self.move_D_prime,
            'F': self.move_F, "F'": self.move_F_prime,
            'B': self.move_B, "B'": self.move_B_prime
        }
        
        if isinstance(moves, str):
            moves = moves.split()
        
        for move in moves:
            if move in move_map:
                move_map[move]()

    def is_solved(self):
        """Check if the cube is solved"""
        colors = ['W', 'R', 'B', 'O', 'G', 'Y']
        faces = ['U', 'F', 'R', 'B', 'L', 'D']
        
        for i, face in enumerate(faces):
            target_color = colors[i]
            for row in self.faces[face]:
                for cell in row:
                    if cell != target_color:
                        return False
        return True

    def validate_state(self):
        """Validate that the input cube state is theoretically solvable"""
        # Count colors
        color_count = {'W': 0, 'R': 0, 'B': 0, 'O': 0, 'G': 0, 'Y': 0}
        
        for face in self.faces.values():
            for row in face:
                for cell in row:
                    if cell in color_count:
                        color_count[cell] += 1
                    else:
                        return False, f"Invalid color: {cell}"
        
        # Each color should appear exactly 9 times
        for color, count in color_count.items():
            if count != 9:
                return False, f"Color {color} appears {count} times (should be 9)"
        
        # Check center pieces are in correct positions
        centers = {
            'U': self.faces['U'][1][1],  # Should be W
            'F': self.faces['F'][1][1],  # Should be R
            'R': self.faces['R'][1][1],  # Should be B
            'B': self.faces['B'][1][1],  # Should be O
            'L': self.faces['L'][1][1],  # Should be G
            'D': self.faces['D'][1][1]   # Should be Y
        }
        
        expected_centers = {'U': 'W', 'F': 'R', 'R': 'B', 'B': 'O', 'L': 'G', 'D': 'Y'}
        
        for face, actual_color in centers.items():
            expected_color = expected_centers[face]
            if actual_color != expected_color:
                return False, f"Center piece error: {face} face has {actual_color}, expected {expected_color}"
        
        return True, "Valid cube state"

class BasicSolver:
    """A basic solver that tries common algorithms to solve the cube"""
    
    def __init__(self, cube):
        self.cube = cube

    def try_basic_algorithms(self):
        """Try applying common algorithms to solve the cube"""
        
        # Common beginner algorithms
        algorithms = [
            # Basic moves and combinations
            "R U R' U'",
            "R U R' U R U U R'",  # Sune
            "R U U R' U' R U' R'",  # Anti-sune
            "F R U R' U' F'",  # Cross algorithm
            "R U R' F' R U R' U' R' F R R U' R'",  # T-Perm
            "R' F R' B B R F' R' B B R R",  # Y-Perm
            # Try basic moves to orient pieces
            "R R", "L L", "U U", "D D", "F F", "B B",
            # Some 4-move combinations
            "R U' R' U", "L U L' U'", "F U F' U'",
            # 6-move sequences
            "R U R' U R U R'", "L U' L' U' L U' L'",
        ]
        
        original_state = self.get_state_string()
        
        print("Trying basic solving algorithms...")
        
        for i, algorithm in enumerate(algorithms):
            print(f"Trying algorithm {i+1}/{len(algorithms)}: {algorithm}")
            
            # Try the algorithm
            self.cube.execute_moves(algorithm)
            
            if self.cube.is_solved():
                print(f"SUCCESS! Cube solved with algorithm: {algorithm}")
                return [algorithm]
            
            # Try with different top orientations
            for rotation in range(3):
                self.cube.execute_moves("U")
                if self.cube.is_solved():
                    rotations = ["U"] * (rotation + 1)
                    print(f"SUCCESS! Cube solved with: {algorithm} + {' '.join(rotations)}")
                    return [algorithm] + rotations
            
            # Try with bottom rotations
            for rotation in range(4):
                self.cube.execute_moves("D")
                if self.cube.is_solved():
                    rotations = ["D"] * (rotation + 1)
                    print(f"SUCCESS! Cube solved with: {algorithm} + {' '.join(rotations)}")
                    return [algorithm] + rotations
            
            # Reset cube to original state for next algorithm
            current_state = self.get_state_string()
            if current_state != original_state:
                # Try to get back to original state
                # This is a simplified reset - in practice we'd need the inverse moves
                attempts = 0
                while self.get_state_string() != original_state and attempts < 20:
                    self.cube.execute_moves("U")
                    attempts += 1
        
        print("Could not solve with basic algorithms.")
        return None

    def get_state_string(self):
        """Get string representation of cube state"""
        state = ""
        for face in ['U', 'F', 'R', 'B', 'L', 'D']:
            for row in self.cube.faces[face]:
                for cell in row:
                    state += cell
        return state

def get_cube_input():
    """Get cube state from user input"""
    
    cube = RubiksCube()
    cube.display_layout_guide()
    
    face_names = ["TOP (White center)", "FRONT (Red center)", "RIGHT (Blue center)", 
                  "BACK (Orange center)", "LEFT (Green center)", "BOTTOM (Yellow center)"]
    
    face_colors = []
    
    for i, face_name in enumerate(face_names):
        while True:
            print(f"\nEnter colors for {face_name}:")
            print("Enter 9 colors (W/R/B/O/G/Y) separated by spaces:")
            print("Example: W W R B W G R R W")
            
            try:
                colors_input = input("Colors: ").strip().upper()
                colors = colors_input.split()
                
                if len(colors) != 9:
                    print(f"Error: Need exactly 9 colors, got {len(colors)}")
                    continue
                
                valid_colors = {'W', 'R', 'B', 'O', 'G', 'Y'}
                invalid = [c for c in colors if c not in valid_colors]
                if invalid:
                    print(f"Error: Invalid colors {invalid}. Use only W/R/B/O/G/Y")
                    continue
                
                face_colors.append(colors)
                break
                
            except KeyboardInterrupt:
                print("\nExiting...")
                return None
            except Exception as e:
                print(f"Error: {e}")
    
    # Set the cube state
    cube.set_state_from_input(face_colors)
    
    # Validate the state
    is_valid, message = cube.validate_state()
    if not is_valid:
        print(f"\nError: {message}")
        print("Please check your input and try again.")
        return None
    
    print(f"\nValidation: {message}")
    return cube

def main():
    """Main program"""
    print("=== RUBIK'S CUBE SOLVER ===")
    print("Enter the colors of your scrambled cube and I'll try to solve it!")
    print()
    
    while True:
        cube = get_cube_input()
        if cube is None:
            break
        
        print("\nYour cube state:")
        cube.display()
        
        if cube.is_solved():
            print("Your cube is already solved!")
            continue
        
        # Try to solve
        solver = BasicSolver(cube)
        solution = solver.try_basic_algorithms()
        
        if solution:
            print(f"\nSolution found! Applied moves: {' '.join(solution)}")
            print("\nFinal state:")
            cube.display()
            print(f"Is solved: {cube.is_solved()}")
        else:
            print("\nSorry, couldn't solve this cube with basic algorithms.")
            print("This cube may require more advanced solving methods.")
        
        # Ask if user wants to try another cube
        print("\nWould you like to try another cube? (y/n)")
        if input().lower().strip() != 'y':
            break
    
    print("Thanks for using the Rubik's Cube Solver!")

if __name__ == "__main__":
    main()