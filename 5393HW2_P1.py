class MolecularFibonacci:
    """
    A simulator for discrete molecular reactions calculating the Fibonacci sequence.
    """
    def __init__(self, initial_a: int, initial_b: int):
        # Initial molecular concentrations
        self.A = initial_a
        self.B = initial_b
        
        # Intermediate buffer species
        self.I_A = 0
        self.I_B = 0

    def step(self):
        """Executes one discrete phase-locked reaction step."""
        # Phase 1: Transfer current concentrations to intermediate buffers
        self.I_B += self.A      # A -> I_B
        self.A = 0
        
        self.I_A += self.B      # B -> I_A
        self.I_B += self.B      # B -> I_B
        self.B = 0
        
        # Phase 2: Commit intermediate buffers to new state
        self.A = self.I_A       # I_A -> A
        self.I_A = 0
        
        self.B = self.I_B       # I_B -> B
        self.I_B = 0
        
        return self.B

    def run(self, steps: int = 11):
        """Runs the reaction to reach the Nth Fibonacci number."""
        print(f"Initial State: A={self.A}, B={self.B}")
        
        # Starting from F_0=0 and F_1=1, it takes 11 additions 
        # to reach the 12th sequence number (144).
        for i in range(1, steps + 1):
            current_val = self.step()
            # Offset the display step by 1 so "Step 12" shows 144
            print(f"Sequence Step {i+1:2}: A={self.A:3}, B={self.B:3} (Current Value: {current_val})")
            
        print("-" * 40)

def run_tests():
    # Test 1: Starting values 0, 1 [cite: 16]
    # Expected to produce 144 as the 12th sequence value [cite: 17]
    print("Testing starting values: 0, 1")
    fib1 = MolecularFibonacci(0, 1)
    fib1.run(steps=11)

    # Test 2: Starting values 3, 7 [cite: 17]
    print("Testing starting values: 3, 7")
    fib2 = MolecularFibonacci(3, 7)
    fib2.run(steps=11)

if __name__ == "__main__":
    run_tests()