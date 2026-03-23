class MolecularBiquadFilter:
    """
    A discrete-time simulator for the Biquad Filter molecular reactions.
    """
    def __init__(self):
        # Initialize delay buffers to zero
        self.D1 = 0.0  # Output of first delay block (B1)
        self.D2 = 0.0  # Output of second delay block (B2)
        self.Y = 0.0   # Output molecule pool
        
    def process_cycle(self, X: float, cycle_num: int) -> float:
        """Processes a single RGB cycle of the biquad filter."""
        
        # 1. Input Summation Node (W)
        # X adds with the 1/8 scaled feedback from D1 and D2
        W = X + (self.D1 / 8.0) + (self.D2 / 8.0)
        
        # 2. Output Calculation (Y)
        # The output Y sums the 1/8 scaled feedforward from W, D1, and D2
        self.Y = (W / 8.0) + (self.D1 / 8.0) + (self.D2 / 8.0)
        
        # 3. Delay State Updates (Simulating the shift through R->G->B)
        # D2 takes the old value of D1, and D1 takes the new value of W
        self.D2 = self.D1
        self.D1 = W
        
        print(f"Cycle {cycle_num}: Input X = {X:3} | Output Y = {self.Y:8.4f} | "
              f"New D1 = {self.D1:8.4f} | New D2 = {self.D2:8.4f}")
        
        # Simulate "sampling" the output by clearing Y for the next cycle
        sampled_Y = self.Y
        self.Y = 0.0 
        
        return sampled_Y

def run_biquad_simulation():
    # The input sequence provided in the assignment
    inputs = [100, 5, 500, 20, 250]
    
    print("Starting Biquad Filter Simulation for 5 Cycles...")
    print("-" * 75)
    
    biquad = MolecularBiquadFilter()
    
    for i, x_val in enumerate(inputs, 1):
        biquad.process_cycle(X=x_val, cycle_num=i)
        
    print("-" * 75)

if __name__ == "__main__":
    run_biquad_simulation()