import argparse
import math

"""
RESEARCH ARCHITECTURE NOTE: 
This implementation does not define specific research parameters; it illustrates, 
in general terms, the proposed research trajectory for boundary condition injection.
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
    # 1. Setup the Command Line Parser
    parser = argparse.ArgumentParser(description="Aerospace Stability Logic Gate")
    
    # 2. Define expected variables
    parser.add_argument("--cp", type=float, required=True, help="Center of Pressure (m)")
    parser.add_argument("--cg", type=float, required=True, help="Center of Gravity (m)")
    parser.add_argument("--p", type=float, default=101325, help="Pressure in Pa (Default: Std Day)")
    parser.add_argument("--t", type=float, default=288.15, help="Temp in Kelvin (Default: 15C)")
    parser.add_argument("--diam", type=float, default=0.042, help="Rocket diameter in meters")

    # 3. Parse the arguments from the terminal
    args = parser.parse_args()

    # 4. Initialize the class and run the logic
    guardian = AtmosphericGuardian(d_max=args.diam)
    result = guardian.verify_stability(x_cp=args.cp, x_cg=args.cg, pressure=args.p, temp=args.t)
    
    print(f"\n--- Integrity Check Results ---")
    for key, value in result.items():
        print(f"{key.replace('_', ' ').title()}: {value}")