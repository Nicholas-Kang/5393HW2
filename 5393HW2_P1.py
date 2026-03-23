class MolecularFibonacci:
    """
    A simulator for discrete molecular reactions calculating the Fibonacci sequence.
    """
    def __init__(self, initial_a: int, initial_b: int):
        # setting up initial values
        self.A = initial_a
        self.B = initial_b
        self.I_A = 0
        self.I_B = 0

    def step(self):
        """Executes one discrete phase-locked reaction step."""
        # intermidate buffers
        self.I_B += self.A      # A -> I_B
        self.A = 0
        self.I_A += self.B      # B -> I_A
        self.I_B += self.B      # B -> I_B
        self.B = 0
        
        # putting intermdeiate buffers into new state
        self.A = self.I_A       # I_A -> A
        self.I_A = 0
        self.B = self.I_B       # I_B -> B
        self.I_B = 0
        
        return self.B

    def run(self, steps: int = 11):
        """Runs the reaction to reach the Nth Fibonacci number."""
        print(f"Initial State: A={self.A}, B={self.B}")
        
        # 11 additions to reach step 12: 144
        for i in range(1, steps + 1):
            current_val = self.step()
            #offset the display step by 1 so "Step 12" shows 144
            print(f"Sequence Step {i+1:2}: A={self.A:3}, B={self.B:3} (Current Value: {current_val})")
            
        print("-" * 40)

def run_tests():
    #testing starting from 0,1
    print("Testing starting values: 0, 1")
    fib1 = MolecularFibonacci(0, 1)
    fib1.run(steps=11)

    #testing Starting values 3, 7
    print("Testing starting values: 3, 7")
    fib2 = MolecularFibonacci(3, 7)
    fib2.run(steps=11)

if __name__ == "__main__":
    run_tests()