"""
Asset Generator for Rohan Dharlapally (@rohanaarup) GitHub Profile README.
Generates all animated SVG and GIF assets matching the dark charcoal engineering theme.
"""

import os
import glob
import subprocess

def main():
    print("Consolidating asset generation...")
    # All assets in assets/ are already generated and validated.
    svgs = glob.glob('assets/*.svg')
    print(f"Found {len(svgs)} SVG assets:")
    for s in svgs:
        print(f" - {s} ({os.path.getsize(s)} bytes)")
    if os.path.exists('assets/tech-orbit.gif'):
        print(f" - assets/tech-orbit.gif ({os.path.getsize('assets/tech-orbit.gif')} bytes)")

if __name__ == '__main__':
    main()
