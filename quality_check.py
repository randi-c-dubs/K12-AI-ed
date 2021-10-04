# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 17:40:54 2021

@author: Randi
"""
import re
import csv

def clean_line(line_of_text):
    # Strip line
    #line_of_text = line_of_text.strip()
    
    # Remove extra characters
    line_of_text = line_of_text.replace("\"", "")
        
    return line_of_text

## Columns
# 0 Title
# 1 Link
# 2 Author
# 3 Year
# 4 Assessment Types
# 5 Big Ideas
# 6 Concepts
# 7 Practices
# 8 Perspectives
# 9 Results of Assessment or Evaluation
# 10 K-12 User Study?
# 11 Age Group
# 12 Setting

## Concepts
# Big Ideas 1-5, Interdisciplinary, Background
# Big idea #1: Sensors and perception, Computer Vision, Signal processing, Gesture recognition
# Big idea #2: Automata and Intelligent Agents, Graphs and data structures, Sorting and Search, Logic Systems, Path planning
# Big Idea #3: Classification, Prediction, Generation, Machine Learning, Generators vs. Discriminators, Data and Data Visualization,
#              Natural Language Processing, Reinforcement Learning, Bias, Unsupervised Learning
# Big Idea #4: Chatbots, Speech Synthesis, Human-Robot Interaction, Natural Language Processing
#              Systems Development, Human-Computer Interaction
# Big Idea #5: Ethics, Privacy, Bias, Security
# Background: What is AI, History of AI, Humans vs AI
BIG_IDEAS = ["big idea #1", "big idea #2", "big idea #3", "big idea #4", "big idea #5", "interdisciplinary", "background"]
BIG_IDEA_1 = ["sensors and perception", "computer vision", "signal processing", "gesture recognition"]
BIG_IDEA_2 = ["automata and intelligent agents", "graphs and data structures", "sorting and search", "logic systems"]
BIG_IDEA_3 = ["classification", "prediction", "generation", "machine learning", "generators vs. discriminators", "data and data visualization", "natural language processing", "reinforcement learning", "bias", "unsupervised learning"]
BIG_IDEA_4 = ["chatbots", "speech synthesis", "human-robot interaction", "natural language processing", "systems development", "human-computer interaction"]
BIG_IDEA_5 = ["ethics", "Privacy", "Bias", "Security"]
BACKGROUND = ["what is ai", "history of ai", "humans vs. ai"]
INTERDISCIPLINARY = ["robotics", "data science", "sustainability", "aeronautics/astronautics", "bioinformatics", "athletics"]

## Practices
# 0 Recognizing and examining AI artifacts: Recognizing everyday AI ,
#           Identifying the inputs and outputs of ML systems, Evaluating bias in models
# 1 Critically interpreting data: Data analysis,
#           Data selection and feature selection
# 2 Analysis of design intentions: Identifying ethical implications,
#           Identifying stakeholders/values
# 3 Design processes: Design thinking, Problem-Solving,
#           Invention and Creation of Tech, Scientific method
# 4 AI Project Planning: Problem Scoping, Determining which model to use,
#           Adapting and Innovating, Using technology to create new knowledge, Designing AI systems
# 5 Creating AI Artifacts: Prototyping, Creating (non-ML) models,
#           Validating (non-ML) system, Programming and Computational thinking
#           Implementation, Deploy AI in a mobile app, Creating user interfaces
#           Training ML models, Validating ML models, Testing or evaluating ML models
#           Evaluation (of entire artifact)
# 6 ML Advocacy: Advocacy
# 7 21st Century STEM Skills: Collaborating, Tech/Scientific communication, 
#           Skills to be successful as a minority in STEM, Teamwork, Creativity
PRACTICE_HEADERS = ["recognizing and examining ai artifacts", "critically interpreting data", "analysis of design intentions", "design processes", "ai project planning", "creating ai artifacts", "ml advocacy", "21st century stem skills"]
P_HEADER_0 = ["recognizing everyday ai", "identifying the inputs and outputs of ml systems"]
P_HEADER_1 = ["data analysis", "data selection and feature selection"]
P_HEADER_2 = ["identifying ethical implications", "identifying stakeholders/values"]
P_HEADER_3 = ["design thinking", "problem-solving", "invention and creation of tech", "scientific method"]
P_HEADER_4 = ["problem scoping", "determining which model to use", "adapting and innovating", "using technology to create new knowledge", "designing AI systems"]
P_HEADER_5 = ["prototyping", "creating (non-ml) models", "validating (non-ml) system", "programming and computational thinking", "implementation", "deploy ai in a mobile app", "creating user interfaces", "training ml models", "validating ml models", "testing or evaluating ml models", "evaluation"]
P_HEADER_6 = ["advocacy"]
P_HEADER_7 = ["collaborating", "tech/scientific communication", "skills to be successful as a minority in stem", "teamwork", "creativity"]

## Perspectives
# Ethics: stakeholders may have different goals for ai, Ai artifacts can be both beneficial and harmful
# Recognizing AI: awareness of ai in future careers, awareness of AI in personal life, awareness of AI's impact on culture
# Limits of AI: aI strengths and weaknesses
# Programmability: Human role in designing AI systems, features can be added to existing systems
# Identity and Community: recognize personal strengths and interests for future jobs, exposure to expert communities, recognize self as a part of a larger community
# Interest: realize importance of technical skills development for jobs
# Self-efficacy: belief in one's capability
# Self-Expression: using AI to express oneself
PERSPECTIVES = ["ethics", "recognizing ai", "limits of ai", "programmability", "identity and community", "interest", "self-efficacy", "self-expression"]

## Assessment Types
# Knowledge Self-assessment
# Student course feedback
# Knowledge transfer and application
# Knowledge Assessment
# Embedded (knowledge) assessment
# Project-Based Assessment
# Classroom Observation
# Presentation-Based Assessment
# Attitutdes toward computing: stem
# Competition
# Perceptions of AI
# Other
ASSESSMENTS = ["perceptions of ai", "competition", "knowledge self-assessment", "student course feedback", "knowledge transfer and application", "knowledge assessment", "embedded assessment", "project-based assessment", "classroom observation", "presentation-based assessment", "attitudes toward computing", "other"]

count = 0

data_file = open("./AI_studies.txt", "r")

# skip the first line
data_file.readline()

for line in data_file:
    count += 1
    
    line = clean_line(line)
    l = line.split("\t")
    
    # make sure all the big ideas are spelled correctly
    big_ideas = l[5].lower()
    for idea in big_ideas.split(", "):
        if idea != "" and not idea in BIG_IDEAS:
            print(count, l[0], idea)
    
    # make sure all the concepts are spelled correctly
    concepts = l[6].lower()
    for concept in concepts.split(", "):
        empty = concept == ""
        bi1 = concept in BIG_IDEA_1
        bi2 = concept in BIG_IDEA_2
        bi3 = concept in BIG_IDEA_3
        bi4 = concept in BIG_IDEA_4
        bi5 = concept in BIG_IDEA_5
        ind = concept in INTERDISCIPLINARY
        bg = concept in BACKGROUND
        if not empty and not bi1 and not bi2 and not bi3 and not bi4 and not bi5 and not ind and not bg:
            print(count, l[0], concept)
    
    # make sure all the practices are spelled correctly
    practices = l[7].lower()
    for prac in practices.split(", "):
        if not prac == "":
            head_prac = prac.split(": ")
            header = head_prac[0] in PRACTICE_HEADERS
            p0 = head_prac[1] in P_HEADER_0
            p1 = head_prac[1] in P_HEADER_1
            p2 = head_prac[1] in P_HEADER_2
            p3 = head_prac[1] in P_HEADER_3
            p4 = head_prac[1] in P_HEADER_4
            p5 = head_prac[1] in P_HEADER_5
            p6 = head_prac[1] in P_HEADER_6
            p7 = head_prac[1] in P_HEADER_7
            if not header:
                print(count, l[0], head_prac[0])
            if not p0 and not p1 and not p2 and not p3 and not p4 and not p5 and not p6 and not p7:
                print(count, l[0], head_prac[1])
                
    # make sure all perspectives are spelled correctly
    perspectives = l[8].lower()
    for pers in perspectives.split(", "):
        if not pers == "":
            head_pers = pers.split(": ")
            if head_pers[0] not in PERSPECTIVES:
                print(count, l[0], head_pers[0])
    
    # make sure all assessments are spelled correctly
    assessments = l[4].lower()
    for asst in assessments.split(", "):
        if not asst == "":
            if asst not in ASSESSMENTS:
                print(count, l[0], asst)
    
data_file.close()