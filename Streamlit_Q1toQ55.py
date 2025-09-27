#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CST Math Review — Q1–Q30 with Jump
"""

import streamlit as st

# Must be first Streamlit call
st.set_page_config(
    page_title="CST Math Review",
    page_icon="🧮",
    layout="centered",
    initial_sidebar_state="expanded",
)

# How many questions are wired up right now (bump when you add more)
TOTAL_QUESTIONS = 55

# Slightly widen the container and enable text wrapping
st.markdown(
    """
    <style>
    .block-container {
        max-width: 1200px;
        padding-left: 2rem;
        padding-right: 2rem;
        overflow-wrap: break-word;
        word-wrap: break-word;
        hyphens: auto;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Import your existing question & solution functions (unchanged) ---
from QuestionsSolutions_Q1toQ55 import (
    question_1, question_2, question_3, question_4, question_5,
    question_6, question_7, question_8, question_9, question_10,
    question_11, question_12, question_13, question_14, question_15,
    question_16, question_17, question_18, question_19, question_20,
    question_21, question_22, question_23, question_24, question_25,
    question_26, question_27, question_28, question_29, question_30, question_31, question_32, 
    question_33, question_34,question_35, question_36, question_37, question_38, 
    question_39, question_40,question_41, question_42, question_43,question_44, question_45,
    question_46,question_47, question_48, question_49, question_50,question_51, question_52,
    question_53,question_54, question_55,
    question_1_solution, question_2_solution, question_3_solution, question_4_solution, 
    question_5_solution,question_6_solution, question_7_solution, question_8_solution, question_9_solution, question_10_solution,
    question_11_solution, question_12_solution, question_13_solution, question_14_solution, question_15_solution,
    question_16_solution, question_17_solution, question_18_solution, question_19_solution, question_20_solution,
    question_21_solution, question_22_solution, question_23_solution, question_24_solution, question_25_solution,
    question_26_solution, question_27_solution, question_28_solution, question_29_solution, question_30_solution,
    question_31_solution, question_32_solution, question_33_solution, question_34_solution, question_35_solution,
    question_36_solution, question_37_solution, question_38_solution, question_39_solution, question_40_solution,
    question_41_solution, question_42_solution, question_43_solution, question_44_solution, question_45_solution, 
    question_46_solution, question_47_solution, question_48_solution, question_49_solution, 
    question_50_solution, question_51_solution, question_52_solution, question_53_solution, 
    question_54_solution, question_55_solution
    
)

# -------------------- Session state --------------------
if "page" not in st.session_state:
    st.session_state.page = "intro"
if "question_number" not in st.session_state:
    st.session_state.question_number = 1
if "name" not in st.session_state:
    st.session_state.name = ""
if "email" not in st.session_state:
    st.session_state.email = ""

# -------------------- Student info CSV --------------------
import csv, os
from datetime import datetime

CSV_FILE = "student_info.csv"  # File to save student info

def is_duplicate(email: str) -> bool:
    try:
        with open(CSV_FILE, mode="r", newline="") as file:
            reader = csv.reader(file)
            next(reader, None)  # Skip header
            for row in reader:
                if len(row) > 1 and email.lower() == row[1].lower():  # Case-insensitive match
                    return True
    except FileNotFoundError:
        return False
    return False

def save_student_info(name, email, exam_date):
    file_exists = os.path.isfile(CSV_FILE)
    if is_duplicate(email):
        st.warning("This email is already saved.")
        return
    with open(CSV_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Name", "Email", "Exam Date", "Timestamp"])  # Header
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        writer.writerow([name, email, exam_date, timestamp])
    st.success("✅ Student info saved successfully!")

# -------------------- Pages --------------------
def intro_page():
    st.markdown("<h1 style='text-align: center;'>CST Math Review: Welcome!</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Dr. Rothman</h3>", unsafe_allow_html=True)
    st.write("These practice questions for the mathematics portion of the New York State Content Specialty Exam (CST)")
    st.write("reflect feedback from LIU Post students who have successfully passed this exam.")
    st.write("It is our hope that you will share your exam experience with as an aid to future LIU Post test takers.")
    st.write("Please enter your information before starting the quiz.")
    st.write("This information will only be used to contact you about your CST Exam experience.")

    # Inputs (bound to session_state keys)
    name = st.text_input("Enter your full name:", key="name")
    email = st.text_input("Enter your email address:", key="email")
    exam_date = st.text_input("When do you plan to take the CST State Exam?", key="exam_date")

    if st.button("Start Quiz"):
        if name and email and exam_date:
            save_student_info(name, email, exam_date)
            st.session_state.page = "quiz"
            st.session_state.question_number = 1
            st.rerun()
        else:
            st.warning("Please fill in all fields before starting.")

def show_solution(q_num: int):
    if q_num == 1:
        question_1_solution()
    elif q_num == 2:
        question_2_solution()
    elif q_num == 3:
        question_3_solution()
    elif q_num == 4:
        question_4_solution()
    elif q_num == 5:
        question_5_solution()
    elif q_num == 6:
        question_6_solution()
    elif q_num == 7:
        question_7_solution()
    elif q_num == 8:
        question_8_solution()
    elif q_num == 9:
        question_9_solution()
    elif q_num == 10:
        question_10_solution()
    elif q_num == 11:
        question_11_solution()
    elif q_num == 12:
        question_12_solution()
    elif q_num == 13:
        question_13_solution()
    elif q_num == 14:
        question_14_solution()
    elif q_num == 15:
        question_15_solution()
    elif q_num == 16:
        question_16_solution()
    elif q_num == 17:
        question_17_solution()
    elif q_num == 18:
        question_18_solution()
    elif q_num == 19:
        question_19_solution()
    elif q_num == 20:
        question_20_solution()
    elif q_num == 21:
        question_21_solution()
    elif q_num == 22:
        question_22_solution()
    elif q_num == 23:
        question_23_solution()
    elif q_num == 24:
        question_24_solution()
    elif q_num == 25:
        question_25_solution()
    elif q_num == 26:
        question_26_solution()
    elif q_num == 27:
        question_27_solution()
    elif q_num == 28:
        question_28_solution()
    elif q_num == 29:
        question_29_solution()
    elif q_num == 30:
        question_30_solution()
    elif q_num == 31:
        question_31_solution()
    elif q_num == 32:
        question_32_solution()
    elif q_num == 33:
        question_33_solution()
    elif q_num == 34:
        question_34_solution()
    elif q_num == 35:
        question_35_solution()  
    elif q_num == 36:
        question_36_solution()    
    elif q_num == 37:
        question_37_solution()  
    elif q_num == 38:
        question_38_solution()    
    elif q_num == 39:
        question_39_solution()      
    elif q_num == 40:
        question_40_solution()  
    elif q_num == 41:
        question_41_solution() 
    elif q_num == 42:
        question_42_solution()    
    elif q_num == 43:
        question_43_solution()  
    elif q_num == 44:
        question_44_solution()    
    elif q_num == 45:
        question_45_solution()      
    elif q_num == 46:
        question_46_solution()  
    elif q_num == 47:
        question_47_solution() 
    elif q_num == 48:
        question_48_solution()   
    elif q_num == 49:
        question_49_solution()    
    elif q_num == 50:
        question_50_solution()  
    elif q_num == 51:
        question_51_solution()    
    elif q_num == 52:
        question_52_solution()      
    elif q_num == 53:
        question_53_solution()  
    elif q_num == 54:
        question_54_solution() 
    elif q_num == 55:
        question_55_solution()      

def quiz_page():
    # Clamp question_number BEFORE any widgets use it
    qn = int(st.session_state.get("question_number", 1))
    if qn < 1:
        qn = 1
    if qn > TOTAL_QUESTIONS:
        qn = TOTAL_QUESTIONS
    st.session_state.question_number = qn

    # --- Sidebar Jump ---
    with st.sidebar:
        st.subheader("Jump")
        jump_target = st.number_input(
            "Go to question #",
            min_value=1,
            max_value=TOTAL_QUESTIONS,
            value=st.session_state.question_number,
            step=1,
        )
        if st.button("Go"):
            st.session_state.page = "quiz"
            st.session_state.question_number = int(jump_target)
            st.rerun()

    # Current question
    q_num = st.session_state.question_number
    st.header(f"Question {q_num}")

    # Route to the right question (your existing elif chain)
    if q_num == 1:
        question_1()
    elif q_num == 2:
        question_2()
    elif q_num == 3:
        question_3()
    elif q_num == 4:
        question_4()
    elif q_num == 5:
        question_5()
    elif q_num == 6:
        question_6()
    elif q_num == 7:
        question_7()
    elif q_num == 8:
        question_8()
    elif q_num == 9:
        question_9()
    elif q_num == 10:
        question_10()
    elif q_num == 11:
        question_11()
    elif q_num == 12:
        question_12()
    elif q_num == 13:
        question_13()
    elif q_num == 14:
        question_14()
    elif q_num == 15:
        question_15()
    elif q_num == 16:
        question_16()
    elif q_num == 17:
        question_17()
    elif q_num == 18:
        question_18()
    elif q_num == 19:
        question_19()
    elif q_num == 20:
        question_20()
    elif q_num == 21:
        question_21()
    elif q_num == 22:
        question_22()
    elif q_num == 23:
        question_23()
    elif q_num == 24:
        question_24()
    elif q_num == 25:
        question_25()
    elif q_num == 26:
        question_26()
    elif q_num == 27:
        question_27()
    elif q_num == 28:
        question_28()
    elif q_num == 29:
        question_29()
    elif q_num == 30:
        question_30()
    elif q_num == 31:
        question_31()
    elif q_num == 32:
        question_32()
    elif q_num == 33:
        question_33()
    elif q_num == 34:
        question_34()
    elif q_num == 35:
        question_35()
    elif q_num == 36:
        question_36()
    elif q_num == 37:
        question_37()
    elif q_num == 38:
        question_38()
    elif q_num == 39:
        question_39()
    elif q_num == 40:
        question_40()
    elif q_num == 41:
        question_41()    
    elif q_num == 42:
        question_42()    
    elif q_num == 43:
        question_43()
    elif q_num == 44:
        question_44()
    elif q_num == 45:
        question_45()
    elif q_num == 46:
        question_46()
    elif q_num == 47:
        question_47()    
    elif q_num == 48:
        question_48()  
    elif q_num == 49:
        question_49()
    elif q_num == 50:
        question_50()
    elif q_num == 51:
        question_51()
    elif q_num == 52:
        question_52()
    elif q_num == 53:
        question_53()    
    elif q_num == 54:
        question_54() 
    elif q_num == 54:
        question_55()   
        
    else:
        st.success(f"You’ve completed all {TOTAL_QUESTIONS} questions! 🎉")
        return

    # Navigation buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Show Solution"):
            show_solution(q_num)
    with col2:
        if st.button("Next Question ▶"):
            if q_num < TOTAL_QUESTIONS:
                st.session_state.question_number = q_num + 1
                st.rerun()
            else:
                st.session_state.question_number = TOTAL_QUESTIONS
                st.success(f"You’ve completed all {TOTAL_QUESTIONS} questions! 🎉")

    # Optional: show where CSV saves (handy when testing)
    st.caption(f"Student CSV path: `{os.path.abspath(CSV_FILE)}`")

def main():
    if st.session_state.page == "intro":
        intro_page()
    elif st.session_state.page == "quiz":
        quiz_page()

if __name__ == "__main__":
    main()
