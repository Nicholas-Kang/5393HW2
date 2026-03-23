class MolecularBiquadFilter:
    def __init__(self):
        #init delays as 0
        self.D1 = 0.0
        self.D2 = 0.0
        
    def process_cycle(self, X: float, cycle_num: int):
        # input calc
        W = X + (self.D1 / 8.0) + (self.D2 / 8.0)
        
        #output calc
        Y = (W / 8.0) + (self.D1 / 8.0) + (self.D2 / 8.0)
        
        #updating the delay states
        self.D2 = self.D1
        self.D1 = W
        
        print(f"Cycle {cycle_num}: Input X = {X:<3} | Output Y = {Y:.4f}")

def run():
    #5 inputs
    inputs = [100, 5, 500, 20, 250]
    
    # filter init
    biquad = MolecularBiquadFilter()
    
    # run for 5 cycles
    for i, x_val in enumerate(inputs, 1):
        biquad.process_cycle(X=x_val, cycle_num=i)

if __name__ == "__main__":
    run()