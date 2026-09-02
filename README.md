Smart Attendance & 75% Eligibility Tracker

A smart Python data automation tool designed around college attendance criteria. Instead of just logging entry times, this script calculates dynamic eligibility metrics based on the strict 75% mandatory attendance rule.

Key Features
* 75% Compliance Calculator: Automatically tracks if a student meets the minimum attendance threshold.
* Deficit Action Plan: If a student is below 75%, the script calculates the exact number of consecutive lectures they must attend to restore their eligibility.
* Bunk Planner: If a student is safely above 75%, it calculates exactly how many upcoming lectures they can safely skip without dropping below the threshold.
* Automated Data Processing: Eliminates manual human calculation errors using Python data structures.

Tech Stack & Tools
* Language: Python 3.x
* Data Processing & Logic: Built using core mathematical logic and file handling modules.
* Environment: Git / GitHub Version Control

System Logic & Workflow
 * Data Ingestion:* The script reads current total lectures conducted versus total lectures attended for each student.
 * Threshold Check:* It evaluates (Attended / Conducted) * 100.
 * Dynamic Advice Generation:* 
   * If < 75%: Runs a calculation loop to find the minimum incremental attended lectures needed to cross 0.75.
   * If >= 75%: Runs a loop to determine how many upcoming total lectures can be missed before falling below 0.75.

How to Run This Project

1. Clone the repository:
   https://github.com

2. Navigate to the project folder:
   cd first-year-coding
   

3. Run the script:
   python smartattendance_tracker.py
   
Developed as a practical data automation project during my 1st year of B.Sc. in Artificial Intelligence.
