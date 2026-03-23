class MolecularBiquadFilter:
    def __init__(self):
        # Initialize the two delay blocks to 0
        self.D1 = 0.0
        self.D2 = 0.0
        
    def process_cycle(self, X: float, cycle_num: int):
        # 1. Input Summation Node (W)
        W = X + (self.D1 / 8.0) + (self.D2 / 8.0)
        
        # 2. Output Calculation (Y)
        Y = (W / 8.0) + (self.D1 / 8.0) + (self.D2 / 8.0)
        
        # 3. Delay State Updates (Shifting the delays for the next cycle)
        self.D2 = self.D1
        self.D1 = W
        
        # Print the exact formatted output
        print(f"Cycle {cycle_num}: Input X = {X:<3} | Output Y = {Y:.4f}")

def run():
    # The 5 inputs requested by the homework prompt
    inputs = [100, 5, 500, 20, 250]
    
    # Create the filter
    biquad = MolecularBiquadFilter()
    
    # Run the 5 cycles
    for i, x_val in enumerate(inputs, 1):
        biquad.process_cycle(X=x_val, cycle_num=i)

if __name__ == "__main__":
    run()