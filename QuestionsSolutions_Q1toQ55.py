#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  9 14:50:43 2025

@author: srothman
"""
import streamlit as st

# === QUESTIONS 1–10 ===

import streamlit as st

def question_1():
    st.write("50 coins consisting of quarters \\((q)\\) and dimes \\((d)\\) total \\($9.20\\).")
    st.write("Which equations can be used to solve for the number of quarters and dimes?")

    choice = st.radio(
        "Select your answer:",
        [
            r"$q + d = 50,\ 10q + 25d = 920$",
            r"$q + d = 50,\ 25q + 10d = 920$",
            r"$q + d = 9.20,\ 25q + 10d = 50$",
            r"$q + d = 50,\ 0.25q + 0.10d = 920$"
        ],
        index=None,
        key="q1_choice"
    )

    if choice == r"$q + d = 50,\ 25q + 10d = 920$":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")






def question_2():
    #st.markdown("### Question 2")
    st.write("A table of 200 students shows the results of a survey.")
    st.write("One row shows 34 third graders from one category.")
    st.write("If there are a total of 110 third graders, what is the probability of picking this category?")

    choice = st.radio(
        "Select your answer:",
        [
            "34 / 200",
            "34 / 110",
            "76 / 200",
            "76 / 110"
        ],
        index=None,
        key="q2_choice"
    )

    if choice == "34 / 110":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

    


def question_3():
    #st.markdown("### Question 3")
    st.markdown("A 13-ounce box of cereal costs \\$3.90 and another 2.5 lb box of cereal costs \\$6.50.")
    st.markdown("What is the difference in the price per pound for the two boxes of cereal?")

    choice = st.radio(
        "Select your answer:",
        [
            "$0.20",
            "$0.1375",
            "$0.10",
            "$0.25"
        ],
        index=None,
        key="q3_choice"
    )

    if choice == "$0.1375":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

    


def question_4():
    #st.markdown("### Question 4")
    st.write("Given the number 3333.231, which digit to the left of the decimal point is 1000 times the 3 to the right of the decimal?")

    choice = st.radio(
        "Select your answer:",
        [
            "3 (in thousands place)",
            "3 (in ones place)",
            "3 (in hundreds place)",
            "3 (in tens place)"
        ],
        index=None,
        key="q4_choice"
    )

    if choice == "3 (in thousands place)":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

    


def question_5():
    st.latex(r"\text{The time for light to travel back and forth from Uranus to Earth is } 1.74 \times 10^4\ \text{seconds.}")
    st.latex(r"\text{If light travels at } 2.6 \times 10^{14}\ \text{cm/sec, how many kilometers is it from Uranus to Earth (one way)?}")

    choices = [
        "2.262 × 10¹³ km",
        "4.524 × 10¹³ km",
        "2.6 × 10¹⁴ km",
        "1.74 × 10⁴ km"
    ]

    # Display choices using st.markdown to format math
    for idx, option in enumerate(choices, start=1):
        st.markdown(f"**({chr(96+idx)})**  {option}")

    # Radio buttons with plain text options for selection
    choice = st.radio(
        "Select your answer:",
        choices,
        index=None,
        key="q5_choice"
    )

    if choice == "2.262 × 10¹³ km":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")



def question_6():
    #st.markdown("### Question 6")
    st.write("Item A originally costs $2000. If it is (a) reduced by 15% or (b) reduced by 5% and then by 10%, what is the difference in the final prices of item A?")

    choice = st.radio(
        "Select your answer:",
        [
            "$30",
            "$10",
            "$25",
            "$15"
        ],
        index=None,
        key="q6_choice"
    )

    if choice == "$20":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

    


def question_7():
    #st.markdown("### Question 7")
    st.write("If the fraction 3/7 is changed to its equivalent decimal, how many digits repeat?")

    choice = st.radio(
        "Select your answer:",
        [
            "5",
            "6",
            "7",
            "8"
        ],
        index=None,
        key="q7_choice"
    )

    if choice == "6":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

    


def question_8():
    #st.markdown("### Question 8")
    st.write("A company gets 80 responses from 200 surveys sent out. If they want an increase of 20 responses, how many surveys do they need to send out?")

    choice = st.radio(
        "Select your answer:",
        [
            "220",
            "250",
            "300",
            "240"
        ],
        index=None,
        key="q8_choice"
    )

    if choice == "250":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

    


def question_9():
    #st.markdown("### Question 9")
    st.write("If the average speed of an object is measured 20 times over one second, how can we best estimate the average speed?")

    choice = st.radio(
        "Select your answer:",
        [
            "Median",
            "Mean",
            "Mode",
            "Range"
        ],
        index=None,
        key="q9_choice"
    )

    if choice == "Mean":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

    


def question_10():
    # Left-justified question
    st.markdown(
        "10. Given the three points $A(-3,7)$, $D(3,-1)$, and $C(0,-5)$, "
        "find the perimeter of the parallelogram with these points as vertices."
    )

    # Choices: plain text for radio buttons
    choice = st.radio(
        "Select your answer:",
        [
            "63.86",         # ✅ Correct answer
            "31.93",         # ❌ Forgot to double the sides
            "127.72",        # ❌ Double-counted the full perimeter
            "50.00"          # ❌ Rough estimate or calculation error
        ],
        index=None,
        key="q10_choice"
    )

    if choice == "63.86":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")



    



def question_1_solution():
    st.write("✅ Correct answer: (b)")
    st.latex(r"""
    \textbf{Worked-Out Solution} \\
    \text{Let } q \text{ be the number of quarters and } d \text{ the number of dimes.} \\
    q + d = 50 \\
    0.25q + 0.10d = 9.20 \\
    \text{Multiply by 100: } 25q + 10d = 920
    """)

def question_2_solution():
    st.write("✅ Correct answer: (b)")
    st.latex(r"""
    \textbf{Worked-Out Solution} \\
    P(E) = \dfrac{\text{Number of successes}}{\text{Total number of possibilities}} \\
    Here: P(E) = \dfrac{34}{110}
    """)

def question_3_solution():
    st.write("✅ Correct answer: (b)")
    st.latex(r"""
    \textbf{Worked-Out Solution} \\
    \text{Price per ounce for 13 oz box: } \dfrac{\$3.90}{13} \approx \$0.30 \text{ per oz} \\
    \text{Price per ounce for 2.5 lb box: } 2.5 \text{ lb} = 40 \text{ oz} \\
    \dfrac{\$6.50}{40} = \$0.1625 \text{ per oz} \\
    \text{Difference: } \$0.30 - \$0.1625 = \boxed{\$0.1375 \text{ per oz}}
    """)

def question_4_solution():
    st.write("✅ Correct answer: (a)")
    st.latex(r"""
    \textbf{Worked-Out Solution} \\
    \text{The 3 to the right of the decimal is in the } \tfrac{1}{1000} \text{th place.} \\
    \text{The 3 in the thousands place is 1000 times larger.}
    """)


def question_5_solution():
    st.write("✅ Correct answer: \(2.262 \times 10^{13}\ \mathrm{km}\)")
    st.latex(r"""
    \textbf{Worked-Out Solution} \\
    \text{Time for round trip: } 1.74 \times 10^4\ \mathrm{s} \\
    \text{One-way time: } \dfrac{1.74 \times 10^4}{2} = 8.7 \times 10^3\ \mathrm{s} \\
    \text{Speed of light: } 2.6 \times 10^{14}\ \mathrm{cm/s} \\
    \text{Distance (cm): } (2.6 \times 10^{14}) \times (8.7 \times 10^3) \\
    = (2.6 \times 8.7) \times 10^{14+3}\ \mathrm{cm} \\
    = 22.62 \times 10^{17}\ \mathrm{cm} \\
    = 2.262 \times 10^{18}\ \mathrm{cm} \\
    \text{Convert to km: } 1\ \mathrm{km}=10^5\ \mathrm{cm} \\
    \dfrac{2.262 \times 10^{18}\ \mathrm{cm}}{10^5} = 2.262 \times 10^{13}\ \mathrm{km} \\
    \boxed{2.262 \times 10^{13}\ \mathrm{km}}
    """)
# ... Continue similarly for question_6 through question_10 ...

# NOTE: I’ll send Q6–Q10 next.


def question_6_solution():
    st.write("✅ Correct answer: (b)")
    st.latex(r"""
    \mathbf{Worked\text{-}Out\ Solution} \\
    15\%\ \mathrm{reduction:}\ 2000 \times 0.85 = 1700 \\
    5\%\ \mathrm{then}\ 10\%\ \mathrm{reduction:}\ 2000 \times 0.95 \times 0.90 = 1710 \\
    \mathrm{Difference:}\ 1710 - 1700 = \boxed{10}
    """)


def question_7_solution():
    st.write("✅ Correct answer: (b)")
    st.latex(r"""
    \textbf{Worked-Out Solution} \\
    \frac{3}{7} = 0.\overline{428571} \text{ (repeats every 6 digits)} \\
    \boxed{6}
    """)


def question_8_solution():
    st.write("✅ Correct answer: (b)")
    st.latex(r"""
    \textbf{Worked-Out Solution} \\
    \text{Current response rate: } \dfrac{80}{200} = 40\% \\
    \text{Desired responses: } 80 + 20 = 100 \\
    \text{Required surveys: } \dfrac{100}{0.4} = \boxed{250}
    """)


def question_9_solution():
    st.write("✅ Correct answer: (b)")
    st.latex(r"""
    \textbf{Worked-Out Solution} \\
    \text{The mean gives the best estimate for central tendency.} \\
    \boxed{\text{Mean}}
    """)

def question_10_solution():
    st.write("✅ Correct answer: (b)")
    st.latex(r"""
    \textbf{Worked-Out Solution} \\
    \text{We are given three points: } A(-3, 7),\ D(3, -1),\ C(0, -5). \\
    \textbf{Step 1: Find the fourth vertex.} \\
    \overrightarrow{AC} = (0 - (-3),\ -5 - 7) = (3, -12). \\
    B = D + \overrightarrow{AC} = (3, -1) + (3, -12) = (6, -13). \\
    \\
    \textbf{Step 2: Compute side lengths.} \\
    AB = \sqrt{(6 - (-3))^2 + (-13 - 7)^2} \\
    = \sqrt{9^2 + (-20)^2} = \sqrt{81 + 400} = \sqrt{481}. \\
    AD = \sqrt{(3 - (-3))^2 + (-1 - 7)^2} \\
    = \sqrt{6^2 + (-8)^2} = \sqrt{36 + 64} = \sqrt{100} = 10. \\
    \\
    \textbf{Step 3: Find the perimeter.} \\
    P = 2 \times (AB + AD) \\
    = 2 \times \left(\sqrt{481} + 10\right) \\
    \approx 2 \times (21.93 + 10) = 2 \times 31.93 = 63.86. \\
    \\
    \boxed{P = 63.86}
    """)


def question_11():
    # Left-justified and math-like question
    st.markdown(
        "Pressure $P$ is directly proportional to temperature $T$. "
        "The constant of proportionality is 2.6. Write the equation relating pressure and temperature."
    )

    # Render choices as LaTeX
    choice = st.radio(
        "Select your answer:",
        [
            r"$P = \dfrac{2.6}{T}$",
            r"$P = 2.6T$",              # ✅ Correct answer
            r"$P = T + 2.6$",
            r"$P = T - 2.6$"
        ],
        index=None,
        key="q11_choice"
    )

    # Evaluate answer
    if choice:
        if choice == r"$P = 2.6T$":
            st.success("✅ Correct!")
        else:
            st.error("❌ Incorrect. Try again.")




def question_11_solution():
    st.write("✅ Correct answer: (b)")
    st.latex(r"""
    \textbf{Worked-Out Solution} \\
    \text{Since } P \propto T, \text{ we have } P = kT. \\
    \text{Given } k = 2.6, \text{ so } P = 2.6T. \\
    \boxed{P = 2.6T}
    """)

def question_12():
    st.write("The surface area of an object is given by")
    st.latex(r"A = 6\sqrt[3]{V^2}")
    st.markdown("Find $V$ if $A = 18$.")

    choice = st.radio(
        "Select your answer:",
        [
            r"$3$",
            r"$3\sqrt{3}$",
            r"$6$",
            r"$2\sqrt{3}$"
        ],
        index=None,
        key="q12_choice"
    )

    if choice:
        if choice == r"$3\sqrt{3}$":
            st.success("✅ Correct!")
        else:
            st.error("❌ Incorrect. Try again.")




def question_12_solution():
    st.write("✅ Correct answer: (b)")
    st.latex(r"""
    \textbf{Worked-Out Solution} \\
    A = 6\sqrt[3]{V^2},\ A=18 \\
    \dfrac{18}{6} = \sqrt[3]{V^2} \implies 3 = \sqrt[3]{V^2} \\
    (3)^3 = (\sqrt[3]{V^2})^3 \implies 27 = V^2 \\
    V = \sqrt{27} = \sqrt{9 \cdot 3} = 3\sqrt{3} \\
    \boxed{3\sqrt{3}}
    """)

def question_13():
    st.write("The compound interest formula is given by:")
    st.latex(r"A = A_0 (1 + r)^t")
    st.write("If:")
    st.latex(r"A = \$60,000,\ A_0 = \$50,000,\ t = 3")
    st.write("Find the annual interest rate $r$.")

    choice = st.radio(
        "Select your answer:",
        [
            r"$5.5\%$",
            r"$6.27\%$",
            r"$7\%$",
            r"$8\%$"
        ],
        index=None,
        key="q13_choice"
    )

    if choice:
        if choice == r"$6.27\%$":
            st.success("✅ Correct!")
        else:
            st.error("❌ Incorrect. Try again.")




def question_13_solution():
    st.write("✅ Correct answer: (b)")
    st.latex(r"""
    \textbf{Worked-Out Solution} \\
    A = A_0(1 + r)^t,\ 60000 = 50000(1 + r)^3 \\
    \dfrac{60000}{50000} = (1 + r)^3 \implies 1.2 = (1 + r)^3 \\
    (1 + r) = \sqrt[3]{1.2} \approx 1.0627 \\
    r = 1.0627 - 1 = 0.0627 = 6.27\% \\
    \boxed{6.27\%}
    """)

def question_14():
   #st.markdown("### Question 14")
    st.write("Bicycle A travels 35 feet on 5 revolutions while bicycle B travels 49 feet on 10 revolutions. What is the ratio of one revolution of B to one revolution of A?")

    choice = st.radio(
        "Select your answer:",
        [
            "0.6",
            "0.7",
            "0.8",
            "0.75"
        ],
        index=None,
        key="q14_choice"
    )

    if choice:
        if choice == "0.7":
            st.success("✅ Correct!")
        else:
            st.error("❌ Incorrect. Try again.")

    


def question_14_solution():
    st.write("✅ Correct answer: (b)")
    st.latex(r"""
    \textbf{Worked-Out Solution} \\
    \text{A: } \dfrac{35}{5} = 7\ \text{ft/rev} \\
    \text{B: } \dfrac{49}{10} = 4.9\ \text{ft/rev} \\
    \dfrac{\text{B}}{\text{A}} = \dfrac{4.9}{7} = \boxed{0.7}
    """)

def question_15():
    #st.markdown("### Question 15")
    st.write("Given an arithmetic sequence where the third term is 17 and the sixth term is 29, find the 20th term.")

    choice = st.radio(
        "Select your answer:",
        [
            "70",
            "71",
            "72",
            "73"
        ],
        index=None,
        key="q15_choice"
    )

    if choice:
        if choice == "71":
            st.success("✅ Correct!")
        else:
            st.error("❌ Incorrect. Try again.")

    


def question_15_solution():
    st.write("✅ Correct answer: (b)")
    st.latex(r"""
    \textbf{Worked-Out Solution} \\
    \text{Let } a_1 = a,\ d = \text{common difference.} \\
    a_3 = a + 2d = 17,\ a_6 = a + 5d = 29 \\
    (a + 5d) - (a + 2d) = 29 - 17 \implies 3d = 12 \implies d = 4 \\
    a + 2d = 17 \implies a + 8 = 17 \implies a = 9 \\
    a_{20} = a + 19d = 9 + 19(4) = 9 + 76 = \boxed{85}
    """)

def question_16():
    #st.markdown("### Question 16")
    st.write("A fair coin is tossed three times. What is the probability of getting exactly two heads?")

    choice = st.radio(
        "Select your answer:",
        [
            "1/2",
            "3/8",
            "1/8",
            "1/4"
        ],
        index=None,
        key="q16_choice"
    )

    if choice:
        if choice == "3/8":
            st.success("✅ Correct!")
        else:
            st.error("❌ Incorrect. Try again.")

    


def question_16_solution():
    st.write("✅ Correct answer: (b)")
    st.latex(r"""
    \textbf{Worked-Out Solution} \\
    \text{Sample space: } 2^3 = 8\ \text{outcomes.} \\
    \text{Favorable outcomes: HHT, HTH, THH (3 outcomes)} \\
    P(\text{exactly 2 heads}) = \dfrac{3}{8} \\
    \boxed{\dfrac{3}{8}}
    """)

def question_17():
    #st.markdown("### Question 17")
    st.write("Which one is a counterexample to the statement: 'The product of two irrational numbers is an irrational number'?")

    choice = st.radio(
        "Select your answer:",
        [
            "√2 ⋅ √8",
            "√4 ⋅ √8",
            "π ⋅ √2",
            "√3 ⋅ √5"
        ],
        index=None,
        key="q17_choice"
    )

    if choice:
        if choice == "√2 ⋅ √4":
            st.success("✅ Correct!")
        else:
            st.error("❌ Incorrect. Try again.")

    


def question_17_solution():
    st.write("✅ Correct answer: (a)")
    st.latex(r"""
    \textbf{Worked-Out Solution} \\
    \sqrt{2}\ \text{is irrational,}\ \sqrt{8}\ \text{is irrational.} \\
    \sqrt{2} \cdot \sqrt{8} = \sqrt{16} = 4\ \text{is rational.} \\
    \boxed{\sqrt{2} \cdot \sqrt{8}\ \textbf{is a counterexample.}} \\
    """)

def question_18():
    #st.markdown("### Question 18")
    st.write("A box contains 8 white balls and 16 red balls. What is the red-to-white constant of proportionality?")

    choice = st.radio(
        "Select your answer:",
        [
            "1/2",
            "2",
            "3",
            "3/2"
        ],
        index=None,
        key="q18_choice"
    )

    if choice:
        if choice == "2":
            st.success("✅ Correct!")
        else:
            st.error("❌ Incorrect. Try again.")

    



def question_18_solution():
    st.write("✅ Correct answer: (b)")
    st.latex(r"""
    \textbf{Worked-Out Solution} \\
    \text{Red:White ratio } = \dfrac{16}{8} = 2 \\
    \boxed{2}
    """)

def question_19():
    #st.markdown("### Question 19")
    st.write("Given the two similar triangles below, find \(x\).")
    st.image("SimilarTriangles19.png", width=400)

    choice = st.radio(
        "Select your answer:",
        [
            "4",
            "12.5",
            "8",
            "10"
        ],
        index=None,
        key="q19_choice"
    )

    if choice:
        if choice == "12.5":
            st.success("✅ Correct!")
        else:
            st.error("❌ Incorrect. Try again.")

    
def question_19_solution():
    st.write("✅ Correct answer: (b)")
    st.latex(r"""
    \textbf{Worked-Out Solution} \\
    \text{Using similarity, set up a proportion:} \\
    \dfrac{5}{2} = \dfrac{x}{5} \implies x = \dfrac{5 \cdot 5}{2} = 12.5 \\
    \boxed{12.5}
    """)

def question_20():
    #st.markdown("### Question 20")
    st.write("What does the diagram below show?")
    st.image("Fractions20.png", width=400)

    choice = st.radio(
        "Select your answer:",
        [
            "These represent equivalent fractions.",
            "These represent inequivalent fractions.",
            "These represent fractions with a common denominator.",
            "These represent proper fractions."
        ],
        index=None,
        key="q20_choice"
    )

    if choice:
        if choice == "These represent inequivalent fractions.":
            st.success("✅ Correct!")
        else:
            st.error("❌ Incorrect. Try again.")

    



def question_20_solution():
    st.write("✅ Correct answer: (b)")
    st.latex(r"""
    \textbf{Worked-Out Solution} \\
    \text{The fractions in the diagram are NOT equivalent.} \\
    \text{The first represents 4/6 = 1/3 but the second represents}\\ 
    \text{4/12 = 1/3.}\\
    \boxed{\text{Inequivalent Fractions}}
    """)

def question_21():
    st.write("Which equation can be used to find:")
    st.latex(r"x")
    st.image("Pythag21.png", width=400)

    choice = st.radio(
        "Select your answer:",
        [
            r"$x + y = 10$",
            r"$10^2 + (5x)^2 = 20^2$",
            r"$x^2 + y^2 = 25$",
            r"$x^2 - y^2 = 20$"
        ],
        index=None,
        key="q21_choice"
    )

    if choice:
        if choice == r"$10^2 + (5x)^2 = 20^2$":
            st.success("✅ Correct!")
        else:
            st.error("❌ Incorrect. Try again.")


    


def question_21_solution():
    st.write("✅ Correct answer: (b)")
    st.latex(r"""
    \textbf{Worked-Out Solution} \\
    \text{Using Pythagoras: } \\
    (5x)^2 + 10^2 = 20^2 \\
    \boxed{10^2 + (5x)^2 = 20^2}
    """)

def question_22():
    st.write("Which balances with:")
    st.latex(r"x")
    st.image("Scale22.png", width=400)

    choice = st.radio(
        "Select your answer:",
        [
            r"$y$ and a dot",
            r"$2y$ and a dot",
            r"$3y$",
            r"a single dot"
        ],
        index=None,
        key="q22_choice"
    )

    if choice:
        if choice == r"$2y$ and a dot":
            st.success("✅ Correct!")
        else:
            st.error("❌ Incorrect. Try again.")

def question_22_solution():
    st.write("✅ Correct answer: (b)")
    st.latex(r"""
    \textbf{Worked-Out Solution} \\
    \text{Two }y\text{'s and one dot balance with }x. \\
    \boxed{2y + \text{dot}}
    """)

def question_23():
    #st.markdown("### Question 23")
    st.write("Which point is closest to \(\sqrt{1000}\)?")
    st.image("NumberLine23.png", width=400)

    choice = st.radio(
        "Select your answer:",
        [
            "Point C",
            "Point A",
            "Point B",
            "Point D"
        ],
        index=None,
        key="q23_choice"
    )

    if choice:
        if choice == "Point A":
            st.success("✅ Correct!")
        else:
            st.error("❌ Incorrect. Try again.")

    


def question_23_solution():
    st.write("✅ Correct answer: (b)")
    st.latex(r"""
    \textbf{Worked-Out Solution} \\
    \sqrt{1000} \approx 31.62 \\
    \text{Point A is closest to this value.} \\
    \boxed{A}
    """)


def question_24():
    st.write("Container B holds twice as much liquid as container A. "
             "If container A presently has 24 ounces and this is 30% of its capacity, "
             "and container B presently holds 48 ounces, "
             "what percentage of container B will be filled after pouring the contents" 
             "of container A into it?")

    choice = st.radio(
        "Select your answer:",
        [
            "30%",
            "45%",   # ✅ Correct
            "60%",
            "50%"
        ],
        index=None,
        key="q24_choice"
    )

    if choice:
        if choice == "45%":
            st.success("✅ Correct!")
        else:
            st.error("❌ Incorrect. Try again.")


    

def question_24_solution():
    st.write("✅ Correct answer: 45%")
    st.latex(r"""
    \textbf{Worked-Out Solution} \\
    \text{Container A: } 24\ \mathrm{oz} = 30\%\ \text{of its capacity} \\
    \implies \text{Capacity of A} = \dfrac{24}{0.3} = 80\ \mathrm{oz} \\
    \text{Container B: Capacity} = 2 \times 80 = 160\ \mathrm{oz} \\
    \\
    \text{Liquid in B before pouring: } 48\ \mathrm{oz} \\
    \text{Liquid added from A: } 24\ \mathrm{oz} \\
    \text{Total in B: } 48 + 24 = 72\ \mathrm{oz} \\
    \text{Percentage filled: } \dfrac{72}{160} \times 100\% = \boxed{45\%}
    """)



def question_25():
    #st.markdown("### Question 25")
    st.write("Why are these triangles similar?")
    st.image("Slope25.png", width=400)

    choice = st.radio(
        "Select your answer:",
        [
            "Because they are right triangles",
            "Because a straight line has constant slope",
            "Because they have proportional sides",
            "Because their angles add up to 180°"
        ],
        index=None,
        key="q25_choice"
    )

    if choice:
        if choice == "Because a straight line has constant slope":
            st.success("✅ Correct!")
        else:
            st.error("❌ Incorrect. Try again.")

    


def question_25_solution():
    st.markdown("**Worked-Out Solution**  \n"  # <- note the double space before \n
                "A straight line has a constant slope, so the triangles are similar  \n"
                "because the sides are proportional.  \n")
    st.latex(r"\boxed{\text{Constant Slope}}")
    

def question_26():
    st.markdown("Which equation is true for the function $y = f(x)$ drawn below?")
    st.image("Parabola26.png", width=400)

    choice = st.radio(
        "Select your answer:",
        [
            r"$f(x) = -f(x)$",
            r"$f(x) = f(-x)$",      # ✅ Correct
            r"$f(-x) = -f(x)$",
            r"$f(x) = x^2$"
        ],
        index=None,
        key="q26_choice"
    )

    if choice:
        if choice == r"$f(x) = f(-x)$":
            st.success("✅ Correct!")
        else:
            st.error("❌ Incorrect. Try again.")

def question_26():
    st.markdown("Which equation is true for the function $y = f(x)$ drawn below?")
    st.image("Parabola26.png", width=400)

    choice = st.radio(
        "Select your answer:",
        [
            r"$f(x) = -f(x)$",
            r"$f(x) = f(-x)$",      # ✅ Correct
            r"$f(-x) = -f(x)$",
            r"$f(x) = x^2$"
        ],
        index=None,
        key="q26_choice"
    )

    if choice:
        if choice == r"$f(x) = f(-x)$":
            st.success("✅ Correct!")
        else:
            st.error("❌ Incorrect. Try again.")


def question_26_solution():
    st.write("✅ Correct answer: (b)")
    st.latex(r"""
    \textbf{Worked-Out Solution} \\
    \text{The graph is symmetric about the y-axis, so: } \\
    f(x) = f(-x)
    """)

def question_27():
    #st.markdown("### Question 27")
    st.write("Which conversion is correct?")
    # st.image("Conversion27.png", width=400)  # Uncomment if you have an image

    choice = st.radio(
        "Select your answer:",
        [
            "10 centimeters = 1 meter",
            "100,000 centimeters = 1 kilometer",
            "1,000 centimeters = 1 meter",
            "100 centimeters = 1 meter"
        ],
        index=None,
        key="q27_choice"
    )

    if choice:
        if choice == "100 centimeters = 1 meter":
            st.success("✅ Correct!")
        else:
            st.error("❌ Incorrect. Try again.")

    


def question_27_solution():
    st.write("✅ Correct answer: (d)")
    st.latex(r"""
    \textbf{Worked-Out Solution} \\
    \boxed{100\ \text{centimeters} = 1\ \text{meter}}
    """)

def question_28():
    # Left-justified question with inline math
    st.markdown("Which equation is correct?")

    choice = st.radio(
        "Select your answer:",
        [
            r"$8 - (x-y)z = 8 - xz - yz$",
            r"$8 - (x-y)z = 8 - xz + yz$",  # ✅ Correct
            r"$8 - (x-y)z = 8 + xz - yz$",
            r"$8 - (x-y)z = 8 + xz + yz$"
        ],
        index=None,
        key="q28_choice"
    )

    if choice:
        if choice == r"$8 - (x-y)z = 8 - xz + yz$":
            st.success("✅ Correct!")
        else:
            st.error("❌ Incorrect. Try again.")


    


def question_28_solution():
    st.write("✅ Correct answer: (b)")
    st.latex(r"""
    \textbf{Worked-Out Solution} \\
    \text{Distribute the negative sign:} \\
    8 - (x-y)z = 8 - xz + yz
    """)

def question_29():
    #st.markdown("### Question 29")
    st.write("Would you use a histogram, pie chart, or scatter plot to look at students and their GPAs?")

    choice = st.radio(
        "Select your answer:",
        [
            "Pie Chart",
            "Histogram",
            "Scatter Plot",
            "Bar Graph"
        ],
        index=None,
        key="q29_choice"
    )

    if choice:
        if choice == "Histogram":
            st.success("✅ Correct!")
        else:
            st.error("❌ Incorrect. Try again.")

    


def question_29_solution():
    st.write("✅ Correct answer: (b)")
    st.latex(r"""
    \textbf{Worked-Out Solution} \\
    \text{A histogram is best for showing the distribution of GPAs.}
    """)

def question_30():
    st.markdown("Which equation represents the graph of the line drawn?")
    st.image("LineThroughOrigin30.png", width=400)

    choice = st.radio(
        "Select your answer:",
        [
            r"$y = -x$",
            r"$y = x$",        # ✅ Correct
            r"$y = x + 1$",
            r"$y = -x + 1$"
        ],
        index=None,
        key="q30_choice"
    )

    if choice:
        if choice == r"$y = x$":
            st.success("✅ Correct!")
        else:
            st.error("❌ Incorrect. Try again.")


    


def question_30_solution():
    st.write("✅ Correct answer: (b)")
    st.latex(r"""
    \textbf{Worked-Out Solution} \\
    \text{This is a line passing through the origin with slope }1. \\
    \boxed{y = x}
    """)
    
def question_31():
    st.write("What is the correct order (least to greatest)?  3/4, 40%, 2^5, 20, 5/8")
    choice = st.radio(
        "Select your answer:",
        [
            "40%, 5/8, 3/4, 2^5, 20",   # ✅
            "5/8, 40%, 3/4, 20, 2^5",
            "40%, 5/8, 3/4, 20, 2^5",
            "40%, 3/4, 5/8, 2^5, 20",
        ],
        index=None, key="q31_choice"
    )
    if choice == "40%, 5/8, 3/4, 2^5, 20":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")


def question_31_solution():
    st.latex(r"""
    \begin{aligned}
    &40\% = 0.40,\quad \frac{5}{8}=0.625,\quad \frac{3}{4}=0.75,\quad 20=20,\quad 2^5=32 \\
    &\text{Order (least to greatest): } 0.40,\ 0.625,\ 0.75,\ 20,\ 32 \\
    &\Rightarrow\ 40\%,\ 5/8,\ 3/4,\ 2^5,\ 20
    \end{aligned}
    """)

def question_32():
    st.write("In a board game, if you roll doubles, you double your points. "
             "What is the probability that on one roll of two standard dice (1–6) you roll a double?")
    choice = st.radio(
        "Select your answer:",
        ["1/3", "1/6", "1/12", "1/36"],
        index=None, key="q32_choice"
    )
    if choice == "1/6":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

def question_32_solution():
    st.latex(r"\text{Doubles: }(1,1),(2,2),\ldots,(6,6)\Rightarrow 6\ \text{out of }36=\boxed{\tfrac{1}{6}}")

def question_33():
    st.write("If there are 2.54 centimeters in 1 inch, how many centimeters, to the nearest hundredth, are in a yard?")
    st.write("(1 yard = 36 inches)")
    choice = st.radio(
        "Select your answer:",
        ["86.36 cm", "90.14 cm", "91.44 cm", "94.20 cm"],
        index=None, key="q33_choice"
    )
    if choice == "91.44 cm":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

def question_33_solution():
    st.latex(r"1\ \text{yard}=36\ \text{inches}")
    st.latex(r"36\times 2.54=\boxed{91.44\ \text{cm}}")

def question_34():
    st.write("Keisha is ordering merchandise. Shipping is $5.00 for the first 10 oz, then $0.75 per additional ounce.")
    st.write("Which algebraic expression gives the shipping charge for a shipment weighing x ounces, where x > 10?")
    choice = st.radio(
        "Select your answer:",
        ["5 + 0.75x", "5 + 0.75(x - 10)", "0.75(x + 10) + 5", "0.75x - 5"],
        index=None, key="q34_choice"
    )
    if choice == "5 + 0.75(x - 10)":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

def question_34_solution():
    st.latex(r"\text{Base } \$5\ \text{covers first }10\text{ oz; extras: }(x-10)\text{ oz at } \$0.75")
    st.latex(r"\boxed{5 + 0.75(x-10)}\quad (x>10)")

def question_35():
    st.write("Liz lives 150 miles from her favorite beach. The beach is 200 miles from the nation’s capital.")
    st.write("What are the shortest and longest possible distances from Liz’s residence to the capital?")
    choice = st.radio(
        "Select your answer:",
        ["50 miles, 200 miles", "50 miles, 350 miles", "150 miles, 350 miles", "200 miles, 350 miles"],
        index=None, key="q35_choice"
    )
    if choice == "50 miles, 350 miles":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

def question_35_solution():
    st.latex(r"\text{Shortest: }|200-150|=\boxed{50}\ \text{miles}")
    st.latex(r"\text{Longest: }150+200=\boxed{350}\ \text{miles}")

# ----------------------------
# New questions: Q36 – Q42
# ----------------------------

# ----------------------------
# New questions: Q36 – Q42
# ----------------------------

def question_36():
    st.write("If the radius of a right circular cylinder is doubled, how does its volume change?")
    choice = st.radio(
        "Select your answer:",
        [
            "No change",
            "also is doubled",
            "four times the original",  # ✅
            "pi times the original",
        ],
        index=None, key="q36_choice"
    )
    if choice == "four times the original":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

def question_36_solution():
    st.latex(r"""
    \begin{aligned}
    &V=\pi r^2 h,\quad r\to 2r \\
    &V'=\pi(2r)^2 h = 4\pi r^2 h = 4V \\
    &\text{Answer: four times the original.}
    \end{aligned}
    """)


def question_37():
    st.write("An item that sells for $375 is put on sale at $120. What is the percent discount?")
    choice = st.radio(
        "Select your answer:",
        [
            "25%",
            "28%",
            "68%",   # ✅
            "34%",
        ],
        index=None, key="q37_choice"
    )
    if choice == "68%":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

def question_37_solution():
    st.latex(r"""
    \begin{aligned}
    &\text{Discount}=375-120=255 \\
    &\text{Percent discount}=\frac{255}{375}=0.68=68\% \\
    &\text{Answer: }68\%.
    \end{aligned}
    """)


def question_38():
    st.write(
        "Kindergarten students paint one half of a folded paper, close and reopen it. "
        "The picture shows matching sides. What math principle does this demonstrate?"
    )
    choice = st.radio(
        "Select your answer:",
        [
            "Slide",
            "Rotate",
            "Symmetry",     # ✅
            "Transformation",
        ],
        index=None, key="q38_choice"
    )
    if choice == "Symmetry":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

def question_38_solution():
    st.write(
        "Folding and transferring ink/paint creates a mirror image. "
        "This is **reflectional (line) symmetry**.\n\n**Answer:** Symmetry."
    )


def question_39():
    st.write(
        "Given a drawer with 5 black socks, 3 blue socks, and 2 red socks, what is the probability "
        "that you will draw two black socks in two draws (without replacement) in a dark room?"
    )
    choice = st.radio(
        "Select your answer:",
        [
            "2/9",    # ✅
            "1/4",
            "17/18",
            "1/18",
        ],
        index=None, key="q39_choice"
    )
    if choice == "2/9":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

def question_39_solution():
    st.latex(r"""
    \begin{aligned}
    &\text{Total socks}=5+3+2=10 \\
    &P(\text{1st black})=\frac{5}{10}=\frac{1}{2},\quad
      P(\text{2nd black}\mid \text{1st black})=\frac{4}{9} \\
    &P(\text{two blacks})=\frac{1}{2}\cdot\frac{4}{9}=\frac{2}{9} \\
    &\text{Answer: } \frac{2}{9}.
    \end{aligned}
    """)


def question_40():
    st.write("A sofa sells for $520. If the retailer makes a 30% profit, what was the wholesale price?")
    choice = st.radio(
        "Select your answer:",
        [
            "$400",   # ✅
            "$676",
            "$490",
            "$364",
        ],
        index=None, key="q40_choice"
    )
    if choice == "$400":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

def question_40_solution():
    st.latex(r"""
    \begin{aligned}
    &\text{Let wholesale price be } C. \\
    &\text{Retail} = 1.30\,C = 520 \;\Rightarrow\; C=\frac{520}{1.30}=400 \\
    &\text{Answer: } \$400.
    \end{aligned}
    """)


def question_41():
    st.write("Each (x, y) relationship between a pair of values is called the ______ and can be plotted on a graph.")
    choice = st.radio(
        "Select your answer:",
        [
            "Coordinate pair",   # ✅ (a.k.a. ordered pair)
            "parallel value",
            "symbolic rule",
            "proportional function",
        ],
        index=None, key="q41_choice"
    )
    if choice == "Coordinate pair":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

def question_41_solution():
    st.write(
        "A single (x, y) value is an **ordered (coordinate) pair**, which marks a point on the coordinate plane.\n\n"
        "**Answer:** Coordinate pair."
    )


def question_42():
    st.write("In similar polygons, if the perimeters are in a ratio of x:y, the sides are in a ratio of:")
    choice = st.radio(
        "Select your answer:",
        [
            "x:y",        # ✅
            "x^2:y^2",
            "2x:y",
            "1/2 x:y",
        ],
        index=None, key="q42_choice"
    )
    if choice == "x:y":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

def question_42_solution():
    st.latex(r"""
    \begin{aligned}
    &\text{In similar figures, all corresponding \emph{lengths} scale by the same factor.} \\
    &\text{Perimeter is a sum of lengths, so perimeter ratio = side ratio.} \\
    &\text{(Areas would scale as } x^2:y^2\text{.)} \\
    &\text{Answer: } x:y.
    \end{aligned}
    """)

# ----------------------------
# New questions: Q43 – Q48
# ----------------------------

def question_43():
    st.write("The maximum area of a rectangular yard bounded by 42 meters of fencing is …")
    choice = st.radio(
        "Select your answer:",
        [
            "84 m^2",
            "100 m^2",
            "110.25 m^2",  # ✅
            "126 m^2",
        ],
        index=None, key="q43_choice"
    )
    if choice == "110.25 m^2":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

def question_43_solution():
    st.latex(r"""
    \begin{aligned}
    &\text{Let sides } x,y \ \text{with } 2(x+y)=42 \Rightarrow y=21-x.\\
    &A(x)=xy=x(21-x)=21x-x^2 \ \Rightarrow \ A'(x)=21-2x=0 \Rightarrow x=10.5.\\
    &y=10.5,\quad A_{\max}=10.5\cdot 10.5=110.25\ \text{m}^2.\\
    &\text{(Max at a square for fixed perimeter.)}
    \end{aligned}
    """)


def question_44():
    st.write("Which of the following are possible angle measures of an isosceles triangle?")
    choice = st.radio(
        "Select your answer:",
        [
            "70, 70, 70",
            "65, 65, 50",   # ✅
            "80, 70, 30",
            "55, 55, 60",
        ],
        index=None, key="q44_choice"
    )
    if choice == "65, 65, 50":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

def question_44_solution():
    st.latex(r"""
    \begin{aligned}
    &\text{Triangle angle sum }=180^\circ\ \text{and isosceles }\Rightarrow \text{two equal angles.}\\
    &70+70+70=210^\circ\ (\text{invalid});\quad 65+65+50=180^\circ\ (\text{valid, two equal});\\
    &80+70+30=180^\circ\ (\text{no equal angles});\quad 55+55+60=170^\circ\ (\text{invalid}).\\
    &\text{Answer: } 65, 65, 50.
    \end{aligned}
    """)


def question_45():
    st.write("Jane has canaries and ferrets. They are all canaries except 3, and all ferrets except 3. "
             "The total number of pets Jane has is")
    choice = st.radio(
        "Select your answer:",
        [
            "3",
            "5",
            "6",  # ✅
            "8",
        ],
        index=None, key="q45_choice"
    )
    if choice == "6":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

def question_45_solution():
    st.latex(r"""
    \begin{aligned}
    &\text{Let } C=\#\text{canaries},\ F=\#\text{ferrets}.\\
    &\text{"All are canaries except 3"} \Rightarrow F=3.\\
    &\text{"All are ferrets except 3"} \Rightarrow C=3.\\
    &\text{Total}=C+F=3+3=6.
    \end{aligned}
    """)


def question_46():
    st.write("The cost of a round pizza is directly related to its size. Which pizza would cost more: "
             "one with radius 5 inches or one with circumference 50 inches?")
    choice = st.radio(
        "Select your answer:",
        [
            "Pizza with radius 5 inches",
            "Pizza with circumference 50 inches",  # ✅
            "They cost the same",
            "Not enough information",
        ],
        index=None, key="q46_choice"
    )
    if choice == "Pizza with circumference 50 inches":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

def question_46_solution():
    st.latex(r"""
    \begin{aligned}
    &\text{Cost } \propto \text{area} = \pi r^2.\\
    &r_1=5 \Rightarrow A_1=\pi(5)^2=25\pi\approx 78.54.\\
    &C=50 \Rightarrow r_2=\tfrac{C}{2\pi}=\tfrac{50}{2\pi}=\tfrac{25}{\pi}\approx 7.96,\ 
      A_2=\pi r_2^2=\frac{625}{\pi}\approx 198.94.\\
    &A_2>A_1 \Rightarrow \text{circumference-50'' pizza costs more.}
    \end{aligned}
    """)


def question_47():
    st.write("The definition of a parallelogram is")
    choice = st.radio(
        "Select your answer:",
        [
            "A quadrilateral with all 4 sides of equal length",
            "4-sided polygon with exactly 1 pair of parallel sides",
            "4-sided polygon with exactly 2 pairs of parallel sides",  # ✅
            "4-sided polygon having all right angles",
        ],
        index=None, key="q47_choice"
    )
    if choice == "4-sided polygon with exactly 2 pairs of parallel sides":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

def question_47_solution():
    st.write(
        "A parallelogram is a quadrilateral with **both pairs of opposite sides parallel** "
        "(i.e., two pairs of parallel sides). Rectangles, rhombuses, and squares are all parallelograms.\n\n"
        "**Answer:** 4-sided polygon with exactly 2 pairs of parallel sides."
    )


def question_48():
    st.write("Julia has an average of 70 on 3 math tests. The final exam counts as 2 tests. "
             "What score must she get on the final to have an average of 80?")
    choice = st.radio(
        "Select your answer:",
        [
            "85",
            "90",
            "95",  # ✅
            "100",
        ],
        index=None, key="q48_choice"
    )
    if choice == "95":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

def question_48_solution():
    st.latex(r"""
    \begin{aligned}
    &\text{Total weight }=3+2=5 \text{ tests}. \\
    &\text{Need total }=80\cdot 5=400. \\
    &\text{Have } 70\cdot 3=210. \\
    &210 + 2x = 400 \Rightarrow 2x=190 \Rightarrow x=95. \\
    &\text{Answer: } 95.
    \end{aligned}
    """)
 # ----------------------------
# New questions: Q49 – Q55
# ----------------------------

def question_49():
    st.write("As the number of sides of a regular polygon increases, the measure of each interior angle …")
    choice = st.radio(
        "Select your answer:",
        [
            "decreases",
            "increases",  # ✅
            "remains the same",
            "alternates between increasing and decreasing",
        ],
        index=None, key="q49_choice"
    )
    if choice == "increases":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

def question_49_solution():
    st.latex(r"""
    \begin{aligned}
    &\text{Interior angle of regular } n\text{-gon}:\ \ \theta_n=\frac{(n-2)180^\circ}{n}
      =180^\circ-\frac{360^\circ}{n}.\\
    &\text{As }n\text{ increases, } \frac{360^\circ}{n}\text{ decreases }\Rightarrow \theta_n \text{ increases.}
    \end{aligned}
    """)


def question_50():
    st.write(
        "A train leaves point P for point G at an average speed of 40 mph. A half-hour later, an express train "
        "leaves P at 50 mph. Both arrive at G at the same time. Calculate the distance (miles) between P and G."
    )
    choice = st.radio(
        "Select your answer:",
        [
            "100",  # ✅
            "85",
            "58",
            "92",
        ],
        index=None, key="q50_choice"
    )
    if choice == "100":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

def question_50_solution():
    st.latex(r"""
    \begin{aligned}
    &\text{Let distance } D. \\
    &\text{Times: slow }=D/40,\ \text{express }=D/50. \\
    &\text{Express leaves }0.5\text{ hr later: } \frac{D}{40}=\frac{D}{50}+0.5. \\
    &\frac{D}{40}-\frac{D}{50}=\frac{D}{200}=0.5 \Rightarrow D=100\ \text{miles}.
    \end{aligned}
    """)


def question_51():
    st.write(
        "Sales tax is 6.25%. A store has a 10% discount plus $7 shipping/handling. "
        "Which expression gives the total cost T (in dollars) in terms of price P?"
    )
    # NOTE: The original set had no correct option; we include the correct formula below.
    choice = st.radio(
        "Select your answer:",
        [
            "(P - 0.1P) + 0.0625(0.9P + 7)",
            "0.0625 × 0.9P + 7",
            "(0.9P + 7) × 1.0625",  # ✅ correct: tax applied after discount + shipping
            "0.0625 × 0.9P - 0.1P",
        ],
        index=None, key="q51_choice"
    )
    if choice == "(0.9P + 7) × 1.0625":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

def question_51_solution():
    st.latex(r"""
    \begin{aligned}
    &\text{Discounted price} = 0.9P. \\
    &\text{Add shipping: } 0.9P + 7. \\
    &\text{Apply sales tax }6.25\% = 0.0625:\ \ T=(0.9P+7)(1+0.0625)=(0.9P+7)\cdot 1.0625.
    \end{aligned}
    """)


def question_52():
    st.write(
        "The statement “the sum of 2 different integers is 24, where the larger is twice the smaller minus 3” "
        "is expressed as"
    )
    choice = st.radio(
        "Select your answer:",
        [
            "x - 2 = 24",
            "(2x - 3) + x = 24",  # ✅
            "3x - 3 = 21",
            "x + 3x = 24",
        ],
        index=None, key="q52_choice"
    )
    if choice == "(2x - 3) + x = 24":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

def question_52_solution():
    st.latex(r"""
    \begin{aligned}
    &\text{Let the smaller integer be }x,\ \text{so larger }=2x-3. \\
    &\text{Sum }= x + (2x-3) = 24 \ \Longleftrightarrow\ (2x-3)+x=24.
    \end{aligned}
    """)


def question_53():
    st.write("James is 4 times as old as Melissa. The sum of their ages is 40. The age of Melissa is …")
    choice = st.radio(
        "Select your answer:",
        [
            "6",
            "8",   # ✅
            "10",
            "12",
        ],
        index=None, key="q53_choice"
    )
    if choice == "8":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

def question_53_solution():
    st.latex(r"""
    \begin{aligned}
    &\text{Let Melissa }=m,\ \text{James }=4m,\ \ m+4m=40 \Rightarrow 5m=40 \Rightarrow m=8.
    \end{aligned}
    """)


def question_54():
    st.write("The prime factorization of the number 260 is …")
    choice = st.radio(
        "Select your answer:",
        [
            "2² · 5 · 13",  # ✅ (using Unicode superscript for radio display)
            "2 · 5 · 13",
            "2² · 5² · 13",
            "2 · 5² · 13",
        ],
        index=None, key="q54_choice"
    )
    if choice == "2² · 5 · 13":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

def question_54_solution():
    st.latex(r"""
    \begin{aligned}
    &260=26\cdot 10=(2\cdot 13)(2\cdot 5)=2^2\cdot 5 \cdot 13.
    \end{aligned}
    """)


def question_55():
    st.write("The number √5 is")
    choice = st.radio(
        "Select your answer:",
        [
            "irrational",
            "real",
            "a number that cannot be expressed as a ratio of 2 integers",
            "all of the above",  # ✅
        ],
        index=None, key="q55_choice"
    )
    if choice == "all of the above":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

def question_55_solution():
    st.write(
        "√5 is a real number and irrational, i.e., it cannot be written as a ratio of two integers. "
        "**Answer:** all of the above."
    )
   


def run_quiz():
    # Call all 30 questions in order
    question_1()
    question_2()
    question_3()
    question_4()
    question_5()
    question_6()
    question_7()
    question_8()
    question_9()
    question_10()
    question_11()
    question_12()
    question_13()
    question_14()
    question_15()
    question_16()
    question_17()
    question_18()
    question_19()
    question_20()
    question_21()
    question_22()
    question_23()
    question_24()
    question_25()
    question_26()
    question_27()
    question_28()
    question_29()
    question_30()
    question_31()
    question_32()
    question_33()
    question_34()
    question_35()
    question_36()
    question_37()
    question_38()
    question_39()
    question_40()
    question_41()
    question_42()
    question_43()
    question_44()
    question_45()
    question_46()
    question_47()
    question_48()
    question_49()
    question_50()
    question_51()
    question_52()
    question_53()
    question_54()
    question_55()
    