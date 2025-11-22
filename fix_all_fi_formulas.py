#!/usr/bin/env python3
"""
Comprehensively reformat all formulas in Fixed Income chapters to be multi-line and readable
"""
import re
import os

os.chdir('/home/user/tos')

def fix_fi1():
    """Fix formulas in Chapter 1"""
    filepath = 'fi/1.html'
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Formula: Current Yield
    content = content.replace(
        '<div class="formula">Current Yield = Annual Coupon Interest / Bond Price</div>',
        '''<div class="formula-box">
                    <span class="formula-title">Current Yield Formula</span><br><br>
                    <span class="formula-main">
                        Current Yield = Annual Coupon Interest / Bond Price
                    </span><br><br>
                    <span class="formula-where">
                        <strong>Where:</strong><br>
                        Annual Coupon Interest = Coupon Rate × Par Value<br>
                        Bond Price = Current Market Price
                    </span>
                </div>'''
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("✓ Fixed Income Chapter 1 formulas reformatted")

def fix_fi6():
    """Fix formulas in Chapter 6"""
    filepath = 'fi/6.html'
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Formula: Bond Price
    content = content.replace(
        '''<div class="formula">
                <strong>Full Bond Price Formula:</strong><br>
                PV =
                (PMT / (1+r)¹) + (PMT / (1+r)²) + ... + (PMT + FV) / (1+r)ᴺ<br><br>
                Where:<br>
                <strong>PV</strong> = Present Value (the bond's price)<br>
                <strong>PMT</strong> = Coupon Payment per period<br>
                <strong>FV</strong> = Future Value (the par or principal value)<br>
                <strong>r</strong> = Market discount rate per period<br>
                <strong>N</strong> = Number of periods until maturity
            </div>''',
        '''<div class="formula-box">
                    <span class="formula-title">Full Bond Price Formula</span><br><br>
                    <span class="formula-main">
                        PV = (PMT / (1+r)¹) + (PMT / (1+r)²) + ... +<br>
                        (PMT + FV) / (1+r)ᴺ
                    </span><br><br>
                    <span class="formula-where">
                        <strong>Where:</strong><br>
                        PV = Present Value (the bond's price)<br>
                        PMT = Coupon Payment per period<br>
                        FV = Future Value (the par or principal value)<br>
                        r = Market discount rate per period<br>
                        N = Number of periods until maturity
                    </span>
                </div>'''
    )

    # Formula: Accrued Interest
    content = content.replace(
        '<div class="formula">AI = (t / T) × PMT</div>',
        '''<div class="formula-box">
                        <span class="formula-title">Accrued Interest Formula</span><br><br>
                        <span class="formula-main">
                            AI = (t / T) × PMT
                        </span><br><br>
                        <span class="formula-where">
                            <strong>Where:</strong><br>
                            AI = Accrued Interest<br>
                            t = Days from last coupon to settlement<br>
                            T = Total days in coupon period<br>
                            PMT = Coupon payment
                        </span>
                    </div>'''
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("✓ Fixed Income Chapter 6 formulas reformatted")

def fix_fi7():
    """Fix formulas in Chapter 7"""
    filepath = 'fi/7.html'
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Formula: Periodicity Conversion
    content = content.replace(
        '''<div class="formula">
                (1 + APRₘ/m)ᵐ = (1 + APRₙ/n)ⁿ<br><br>
                Where:<br>
                <strong>APRₘ</strong> = APR with m compounding periods per year.<br>
                <strong>APRₙ</strong> = APR with n compounding periods per year.
            </div>''',
        '''<div class="formula-box">
                    <span class="formula-title">Periodicity Conversion Formula</span><br><br>
                    <span class="formula-main">
                        (1 + APRₘ/m)ᵐ = (1 + APRₙ/n)ⁿ
                    </span><br><br>
                    <span class="formula-where">
                        <strong>Where:</strong><br>
                        APRₘ = APR with m compounding periods per year<br>
                        APRₙ = APR with n compounding periods per year<br>
                        m = Number of compounding periods for first rate<br>
                        n = Number of compounding periods for second rate
                    </span>
                </div>'''
    )

    # Formula: Call Option Value
    content = content.replace(
        '<div class="formula">Value of Call Option = Price of Option-Free Bond - Price of Callable Bond</div>',
        '''<div class="formula-box">
                    <span class="formula-title">Call Option Value Formula</span><br><br>
                    <span class="formula-main">
                        Value of Call Option =<br>
                        Price of Option-Free Bond − Price of Callable Bond
                    </span><br><br>
                    <span class="formula-where">
                        <strong>Note:</strong> The call option has value to the issuer,<br>
                        reducing the price investors pay for callable bonds
                    </span>
                </div>'''
    )

    # Formula: OAS
    content = content.replace(
        '<div class="formula">OAS = Z-Spread - Option Value</div>',
        '''<div class="formula-box">
                    <span class="formula-title">Option-Adjusted Spread (OAS) Formula</span><br><br>
                    <span class="formula-main">
                        OAS = Z-Spread − Option Value
                    </span><br><br>
                    <span class="formula-where">
                        <strong>Where:</strong><br>
                        OAS = Option-Adjusted Spread<br>
                        Z-Spread = Zero-Volatility Spread<br>
                        Option Value = Value of embedded options
                    </span>
                </div>'''
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("✓ Fixed Income Chapter 7 formulas reformatted")

def fix_fi8():
    """Fix formulas in Chapter 8"""
    filepath = 'fi/8.html'
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Formula: Coupon Rate
    content = content.replace(
        '''<div class="formula-box">
                    Coupon Rate = Reference Rate + Quoted Margin
                </div>''',
        '''<div class="formula-box">
                    <span class="formula-title">Floating-Rate Coupon Formula</span><br><br>
                    <span class="formula-main">
                        Coupon Rate = Reference Rate + Quoted Margin
                    </span><br><br>
                    <span class="formula-where">
                        <strong>Where:</strong><br>
                        Reference Rate = Benchmark rate (e.g., LIBOR, SOFR)<br>
                        Quoted Margin = Fixed spread over reference rate
                    </span>
                </div>'''
    )

    # Formula: Discount Margin PV
    content = content.replace(
        '''<div class="formula-box">
                    PV = Σ[(Reference Rate + Quoted Margin) × Principal / n] / (1 + (Reference Rate + DM) / n)^t + Principal / (1 + (Reference Rate + DM) / n)^N
                </div>''',
        '''<div class="formula-box">
                    <span class="formula-title">Discount Margin Present Value Formula</span><br><br>
                    <span class="formula-main">
                        PV = Σ[(Reference Rate + Quoted Margin) × Principal / n]<br>
                        ÷ (1 + (Reference Rate + DM) / n)^t<br>
                        + Principal / (1 + (Reference Rate + DM) / n)^N
                    </span><br><br>
                    <span class="formula-where">
                        <strong>Where:</strong><br>
                        PV = Present Value (market price)<br>
                        DM = Discount Margin<br>
                        n = Number of coupon payments per year<br>
                        N = Total number of periods<br>
                        t = Period number
                    </span>
                </div>'''
    )

    # Fix the malformed inverse floater formula
    content = content.replace(
        '''<div class="formula-box">
<span class="formula-title"></span>
<span class="formula-main">Inverse Floater Coupon = C - L × (Reference Rate)
                    <br></span>

<span class="formula-where">where:
C = Maximum coupon rate, L = Leverage factor</span>
</div>''',
        '''<div class="formula-box">
                    <span class="formula-title">Inverse Floater Coupon Formula</span><br><br>
                    <span class="formula-main">
                        Inverse Floater Coupon = C − L × (Reference Rate)
                    </span><br><br>
                    <span class="formula-where">
                        <strong>Where:</strong><br>
                        C = Maximum coupon rate<br>
                        L = Leverage factor<br>
                        Reference Rate = Benchmark interest rate
                    </span>
                </div>'''
    )

    # Formula: Modified Duration
    content = content.replace(
        '''<div class="formula-box">
                    Modified Duration ≈ Time to Next Reset Date
                </div>''',
        '''<div class="formula-box">
                    <span class="formula-title">Floating-Rate Bond Duration Approximation</span><br><br>
                    <span class="formula-main">
                        Modified Duration ≈ Time to Next Reset Date
                    </span><br><br>
                    <span class="formula-where">
                        <strong>Note:</strong> Floating-rate bonds have very low duration<br>
                        because coupons adjust with market rates
                    </span>
                </div>'''
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("✓ Fixed Income Chapter 8 formulas reformatted")

def fix_fi9():
    """Fix formulas in Chapter 9"""
    filepath = 'fi/9.html'
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Formula: Bond Price with Spot Rate
    content = content.replace(
        '''<div class="formula-box">
                    Bond Price = Face Value / (1 + Spot Rate)^Time to Maturity
                </div>''',
        '''<div class="formula-box">
                    <span class="formula-title">Zero-Coupon Bond Pricing Formula</span><br><br>
                    <span class="formula-main">
                        Bond Price = Face Value / (1 + Spot Rate)^Time to Maturity
                    </span><br><br>
                    <span class="formula-where">
                        <strong>Where:</strong><br>
                        Face Value = Par value at maturity<br>
                        Spot Rate = Zero-coupon yield for the maturity<br>
                        Time to Maturity = Years until bond matures
                    </span>
                </div>'''
    )

    # Fix malformed forward rate formula
    content = content.replace(
        '''<div class="formula-box">
<span class="formula-title"></span>
<span class="formula-main">(1 + s₂)² = (1 + s₁) × (1 + f₁,₁)
                    <br><br></span>

<span class="formula-where">where:
s₂ = 2-year spot rate, s₁ = 1-year spot rate, f₁,₁ = 1-year forward rate starting in 1 year</span>
</div>''',
        '''<div class="formula-box">
                    <span class="formula-title">Forward Rate Calculation Formula</span><br><br>
                    <span class="formula-main">
                        (1 + s₂)² = (1 + s₁) × (1 + f₁,₁)
                    </span><br><br>
                    <span class="formula-where">
                        <strong>Where:</strong><br>
                        s₂ = 2-year spot rate<br>
                        s₁ = 1-year spot rate<br>
                        f₁,₁ = 1-year forward rate starting in 1 year
                    </span>
                </div>'''
    )

    # Formula: Forward Rate and Liquidity Premium
    content = content.replace(
        '''<div class="formula-box">
                    Forward Rate = Expected Future Spot Rate + Liquidity Premium
                </div>''',
        '''<div class="formula-box">
                    <span class="formula-title">Liquidity Preference Theory Formula</span><br><br>
                    <span class="formula-main">
                        Forward Rate = Expected Future Spot Rate + Liquidity Premium
                    </span><br><br>
                    <span class="formula-where">
                        <strong>Where:</strong><br>
                        Forward Rate = Rate implied by term structure<br>
                        Expected Future Spot Rate = Market expectation<br>
                        Liquidity Premium = Compensation for maturity risk
                    </span>
                </div>'''
    )

    # Fix Vasicek Model
    content = content.replace(
        '''<div class="formula-box">
<span class="formula-title">Vasicek Model</span>
<span class="formula-main"> dr = a(b - r)dt + σdW
                    <br></span>

<span class="formula-where">where:
a = mean reversion speed, b = long-term mean, σ = volatility, dW = Brownian motion increment</span>
</div>''',
        '''<div class="formula-box">
                    <span class="formula-title">Vasicek Model</span><br><br>
                    <span class="formula-main">
                        dr = a(b − r)dt + σdW
                    </span><br><br>
                    <span class="formula-where">
                        <strong>Where:</strong><br>
                        dr = Change in short-term interest rate<br>
                        a = Mean reversion speed<br>
                        b = Long-term mean interest rate<br>
                        r = Current interest rate<br>
                        σ = Volatility parameter<br>
                        dW = Brownian motion increment
                    </span>
                </div>'''
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("✓ Fixed Income Chapter 9 formulas reformatted")

def fix_fi10():
    """Fix formulas in Chapter 10"""
    filepath = 'fi/10.html'
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Formula: Total Return
    content = content.replace(
        '''<div class="formula-box">
                    Total Return = Coupon Income + Capital Gain/Loss + Reinvestment Income
                </div>''',
        '''<div class="formula-box">
                    <span class="formula-title">Total Return Formula</span><br><br>
                    <span class="formula-main">
                        Total Return = Coupon Income + Capital Gain/Loss +<br>
                        Reinvestment Income
                    </span><br><br>
                    <span class="formula-where">
                        <strong>Where:</strong><br>
                        Coupon Income = Periodic interest payments<br>
                        Capital Gain/Loss = Change in bond price<br>
                        Reinvestment Income = Interest earned on reinvested coupons
                    </span>
                </div>'''
    )

    # Fix Macaulay Duration
    content = content.replace(
        '''<div class="formula-box">
<span class="formula-title"></span>
<span class="formula-main">MacDur = Σ[t × (CF_t / (1+y)^t)] / Bond Price
                    <br></span>

<span class="formula-where">where:
t = time period, CF_t = cash flow at time t, y = yield to maturity</span>
</div>''',
        '''<div class="formula-box">
                    <span class="formula-title">Macaulay Duration Formula</span><br><br>
                    <span class="formula-main">
                        MacDur = Σ[t × (CF_t / (1+y)^t)] / Bond Price
                    </span><br><br>
                    <span class="formula-where">
                        <strong>Where:</strong><br>
                        MacDur = Macaulay Duration (in years)<br>
                        t = Time period<br>
                        CF_t = Cash flow at time t<br>
                        y = Yield to maturity<br>
                        Bond Price = Current market price
                    </span>
                </div>'''
    )

    # Modified Duration
    content = content.replace(
        '''<div class="formula-box">
                    ModDur = MacDur / (1 + y)
                    <br><br>
                    % Price Change ≈ -ModDur × Δy
                </div>''',
        '''<div class="formula-box">
                    <span class="formula-title">Modified Duration Formulas</span><br><br>
                    <span class="formula-main">
                        ModDur = MacDur / (1 + y)<br><br>
                        % Price Change ≈ −ModDur × Δy
                    </span><br><br>
                    <span class="formula-where">
                        <strong>Where:</strong><br>
                        ModDur = Modified Duration<br>
                        MacDur = Macaulay Duration<br>
                        y = Yield to maturity<br>
                        Δy = Change in yield
                    </span>
                </div>'''
    )

    # Money Duration
    content = content.replace(
        '''<div class="formula-box">
                    Money Duration = Modified Duration × Bond Price
                    <br>
                    PVBP = Money Duration × 0.0001
                </div>''',
        '''<div class="formula-box">
                    <span class="formula-title">Money Duration and PVBP Formulas</span><br><br>
                    <span class="formula-main">
                        Money Duration = Modified Duration × Bond Price<br><br>
                        PVBP = Money Duration × 0.0001
                    </span><br><br>
                    <span class="formula-where">
                        <strong>Where:</strong><br>
                        Money Duration = Dollar duration<br>
                        PVBP = Price Value of a Basis Point<br>
                        0.0001 = One basis point (0.01%)
                    </span>
                </div>'''
    )

    # Convexity
    content = content.replace(
        '''<div class="formula-box">
                    Convexity = [1 / (P × (1+y)²)] × Σ[t × (t+1) × CF_t / (1+y)^t]
                    <br><br>
                    % Price Change ≈ -ModDur × Δy + 0.5 × Convexity × (Δy)²
                </div>''',
        '''<div class="formula-box">
                    <span class="formula-title">Convexity Formulas</span><br><br>
                    <span class="formula-main">
                        Convexity = [1 / (P × (1+y)²)] × Σ[t × (t+1) × CF_t / (1+y)^t]<br><br>
                        % Price Change ≈ −ModDur × Δy + 0.5 × Convexity × (Δy)²
                    </span><br><br>
                    <span class="formula-where">
                        <strong>Where:</strong><br>
                        P = Bond Price<br>
                        y = Yield to maturity<br>
                        t = Time period<br>
                        CF_t = Cash flow at time t<br>
                        Δy = Change in yield
                    </span>
                </div>'''
    )

    # Fix Effective Duration
    content = content.replace(
        '''<div class="formula-box">
<span class="formula-title"></span>
<span class="formula-main">Effective Duration = (P₋ - P₊) / (2 × P₀ × Δy)
                    <br></span>

<span class="formula-where">where:
P₋ = price if yields decrease, P₊ = price if yields increase, P₀ = initial price, Δy = yield change</span>
</div>''',
        '''<div class="formula-box">
                    <span class="formula-title">Effective Duration Formula</span><br><br>
                    <span class="formula-main">
                        Effective Duration = (P₋ − P₊) / (2 × P₀ × Δy)
                    </span><br><br>
                    <span class="formula-where">
                        <strong>Where:</strong><br>
                        P₋ = Bond price if yields decrease by Δy<br>
                        P₊ = Bond price if yields increase by Δy<br>
                        P₀ = Initial bond price<br>
                        Δy = Yield change (e.g., 0.0025 for 25 bps)
                    </span>
                </div>'''
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("✓ Fixed Income Chapter 10 formulas reformatted")

def fix_fi11():
    """Fix formulas in Chapter 11"""
    filepath = 'fi/11.html'
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Fix Merton Model
    content = content.replace(
        '''<div class="formula-box">
<span class="formula-title">Merton Model</span>
<span class="formula-main"> Default occurs when V_T < D
                    <br></span>

<span class="formula-where">where:
V_T = firm value at maturity, D = debt obligation</span>
</div>''',
        '''<div class="formula-box">
                    <span class="formula-title">Merton Model Default Condition</span><br><br>
                    <span class="formula-main">
                        Default occurs when V_T &lt; D
                    </span><br><br>
                    <span class="formula-where">
                        <strong>Where:</strong><br>
                        V_T = Firm asset value at debt maturity<br>
                        D = Face value of debt obligation<br>
                        <br>
                        <strong>Note:</strong> The Merton model treats equity as a call option<br>
                        on the firm's assets with strike price D
                    </span>
                </div>'''
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("✓ Fixed Income Chapter 11 formulas reformatted")

def fix_fi12():
    """Fix formulas in Chapter 12"""
    filepath = 'fi/12.html'
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Formula: CDS Premium
    content = content.replace(
        '''<div class="formula-box">
                    CDS Premium = (CDS Spread × Notional Amount × Days in Period) / 360
                </div>''',
        '''<div class="formula-box">
                    <span class="formula-title">CDS Premium Calculation Formula</span><br><br>
                    <span class="formula-main">
                        CDS Premium = (CDS Spread × Notional Amount × Days in Period) / 360
                    </span><br><br>
                    <span class="formula-where">
                        <strong>Where:</strong><br>
                        CDS Spread = Annual spread in basis points<br>
                        Notional Amount = Protected principal amount<br>
                        Days in Period = Days in payment period<br>
                        360 = Day count convention
                    </span>
                </div>'''
    )

    # Formula: Cash Settlement
    content = content.replace(
        '''<div class="formula-box">
                    Cash Settlement Payment = Notional Amount × (100% - Recovery Rate)
                </div>''',
        '''<div class="formula-box">
                    <span class="formula-title">CDS Cash Settlement Formula</span><br><br>
                    <span class="formula-main">
                        Cash Settlement Payment =<br>
                        Notional Amount × (100% − Recovery Rate)
                    </span><br><br>
                    <span class="formula-where">
                        <strong>Where:</strong><br>
                        Notional Amount = Protected principal<br>
                        Recovery Rate = % of face value recovered after default<br>
                        100% − Recovery Rate = Loss given default (LGD)
                    </span>
                </div>'''
    )

    # Formula: CDS Spread Approximation
    content = content.replace(
        '''<div class="formula-box">
                    CDS Spread ≈ Credit Spread × (1 - Recovery Rate) / (1 - Bond Recovery Rate)
                </div>''',
        '''<div class="formula-box">
                    <span class="formula-title">CDS Spread Approximation Formula</span><br><br>
                    <span class="formula-main">
                        CDS Spread ≈<br>
                        Credit Spread × (1 − Recovery Rate) / (1 − Bond Recovery Rate)
                    </span><br><br>
                    <span class="formula-where">
                        <strong>Where:</strong><br>
                        CDS Spread = Credit default swap spread<br>
                        Credit Spread = Bond yield spread over risk-free rate<br>
                        Recovery Rate = Expected recovery on CDS<br>
                        Bond Recovery Rate = Expected recovery on bond
                    </span>
                </div>'''
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("✓ Fixed Income Chapter 12 formulas reformatted")

def fix_fi13():
    """Fix formulas in Chapter 13"""
    filepath = 'fi/13.html'
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Fix Monthly Payment formula
    content = content.replace(
        '''<div class="formula-box">
<span class="formula-title"></span>
<span class="formula-main">Monthly Payment = P × [r(1+r)^n] / [(1+r)^n - 1]
                    <br></span>

<span class="formula-where">where:
P = loan principal, r = monthly interest rate, n = number of payments</span>
</div>''',
        '''<div class="formula-box">
                    <span class="formula-title">Mortgage Monthly Payment Formula</span><br><br>
                    <span class="formula-main">
                        Monthly Payment = P × [r(1+r)^n] / [(1+r)^n − 1]
                    </span><br><br>
                    <span class="formula-where">
                        <strong>Where:</strong><br>
                        P = Loan principal amount<br>
                        r = Monthly interest rate (annual rate / 12)<br>
                        n = Total number of monthly payments<br>
                        (1+r)^n = Compounding factor
                    </span>
                </div>'''
    )

    # Formula: Credit Enhancement
    content = content.replace(
        '''<div class="formula-box">
                    Credit Enhancement = (Subordination + Overcollateralization + Reserve Accounts) / Pool Balance
                </div>''',
        '''<div class="formula-box">
                    <span class="formula-title">Credit Enhancement Level Formula</span><br><br>
                    <span class="formula-main">
                        Credit Enhancement =<br>
                        (Subordination + Overcollateralization + Reserve Accounts)<br>
                        / Pool Balance
                    </span><br><br>
                    <span class="formula-where">
                        <strong>Where:</strong><br>
                        Subordination = Junior tranches providing protection<br>
                        Overcollateralization = Excess collateral value<br>
                        Reserve Accounts = Cash reserves for losses<br>
                        Pool Balance = Total asset pool value
                    </span>
                </div>'''
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("✓ Fixed Income Chapter 13 formulas reformatted")

# Run all fixes
fix_fi1()
fix_fi6()
fix_fi7()
fix_fi8()
fix_fi9()
fix_fi10()
fix_fi11()
fix_fi12()
fix_fi13()

print("\n✓✓✓ All Fixed Income formula reformatting completed! ✓✓✓")
