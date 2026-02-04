import argparse
import math
import csv

"""
RESEARCH ARCHITECTURE NOTE: 
This implementation demonstrates the transition from single-point 
verification to batch processing using external CSV datasets.
"""

class AtmosphericGuardian:
    def __init__(self, d_max, gas_constant=287.05):
        self.d_max = d_max 
        self.R = gas_constant 

    def calculate_density(self, pressure_pa, temp_k):
        return pressure_pa / (self.R * temp_k)

    def verify_stability(self, x_cp, x_cg, pressure, temp):
        rho = self.calculate_density(pressure, temp)
        s_margin = (x_cp - x_cg) / self.d_max
        threshold = 1.5 if rho > 1.225 else 1.0
        is_safe = s_margin >= threshold
        
        return {
            "density_kg_m3": round(rho, 4),
            "static_margin": round(s_margin, 2),
            "status": "PASS" if is_safe else "FAIL"
        }

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Batch Aerospace Stability Logic Gate")
    parser.add_argument("--input", type=str, required=True, help="Path to input CSV file")
    args = parser.parse_args()

    print(f"{'Pressure':<10} | {'Temp':<8} | {'Margin':<8} | {'Status':<6}")
    print("-" * 45)

    with open(args.input, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Initialize guardian with diameter from CSV or default
            diam = float(row.get('diam', 0.042))
            guardian = AtmosphericGuardian(d_max=diam)
            
            # Execute verification logic
            result = guardian.verify_stability(
                x_cp=float(row['cp']), 
                x_cg=float(row['cg']), 
                pressure=float(row['p']), 
                temp=float(row['t'])
            )
            
            # Output row results
            print(f"{row['p']:<10} | {row['t']:<8} | {result['static_margin']:<8} | {result['status']:<6}")