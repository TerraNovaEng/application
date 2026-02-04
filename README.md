# application
illustrative prototype for research

Script: illustrativeprototype.py

Purpose: Verify core physics logic using specific hand-calculated variables.

In terminal: python illustrativeprototype.py --cp 0.35 --cg 0.28 (or your variables)

What it does: Processes the provided Center of Pressure and Center of Gravity against "Standard Day" atmospheric conditions.

Result: Displays a single PASS or FAIL status.
----------------------------------------
Script: illustrativeprototypebatchauto.py

Purpose: Bridge the gap between local simulations and real-world coastal weather at Logan Airport.

In terminal: python illustrativeprototypebatchauto.py

Action: Connects to the Massport/Logan API, extracts current pressure and temperature, and saves the entry to logan_data.csv. Make sure you read notes on code

Result: A new atmospheric "Fact" is appended to the research log.
-----------------------------------------------

Script: illustrativeprototypebatch.py

Purpose: Execute a high-fidelity "Numerical Truth" check across the entire collected history.

In terminal: python illustrativeprototypebatch.py --input logan_data.csv

Action: Iterates through every row in the CSV file and runs the physics solver for each unique environment.

Result: A formatted table displaying pressure, temperature, stability margin, and status for all recorded trials.
-----------------------
