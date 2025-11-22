#!/usr/bin/env python3
"""
Properly reformat formulas to be multi-line and readable
"""
import re
import os

def reformat_formula_fi8():
    """Manually reformat formulas in FI Chapter 8 as example"""
    filepath = 'fi/8.html'

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Formula 1: Coupon Rate
    content = content.replace(
        '''<div class="formula-box">
                    Coupon Rate = Reference Rate + Quoted Margin
                </div>''',
        '''<div class="formula-box">
                    <strong>Coupon Rate Formula:</strong><br><br>
                    <div style="text-align: center; font-size: 1.3rem; margin: 1rem 0;">
                        Coupon Rate = Reference Rate + Quoted Margin
                    </div>
                </div>'''
    )

    # Formula 2: PV for Discount Margin
    old_pv = '''<div class="formula-box">
                    PV = Σ[(Reference Rate + Quoted Margin) × Principal / n] / (1 + (Reference Rate + DM) / n)^t + Principal / (1 + (Reference Rate + DM) / n)^N
                </div>'''

    new_pv = '''<div class="formula-box">
                    <strong>Discount Margin Calculation:</strong><br><br>
                    <div style="text-align: center; font-size: 1.2rem; margin: 1rem 0;">
                        PV = Σ[(Reference Rate + Quoted Margin) × Principal / n] / (1 + (Reference Rate + DM) / n)^t
                        <br>+ Principal / (1 + (Reference Rate + DM) / n)^N
                    </div>
                    <br>
                    <div style="text-align: left; font-size: 1rem; line-height: 2;">
                        <strong>Where:</strong><br>
                        PV = Present Value (market price)<br>
                        DM = Discount Margin<br>
                        n = Number of coupon payments per year<br>
                        N = Total number of periods<br>
                        t = Period number
                    </div>
                </div>'''

    content = content.replace(old_pv, new_pv)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print("✓ Fixed Income Chapter 8 formulas reformatted")

# Run the reformatting
os.chdir('/home/user/tos')
reformat_formula_fi8()
