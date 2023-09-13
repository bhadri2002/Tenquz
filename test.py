import re
import json

txt = '''
['Here are five HTML level 1 questions in JSON format:\n\n1. \n```json\n{\n  "question": "What does HTML stand for?",\n  "questionRelatedTopic": ["HTML Basics"],\n  "options": ["Hyperlinks and Text Markup Language", "Hyper Text Markup Language", "Home Tool Markup Language", "Hyperlinks and Text Markup Layout"],\n  "correctOption": 1,\n  "explanation": "HTML stands for Hyper Text Markup Language, which is used for creating the structure and presentation of web pages."\n}\n```\n\n2. \n```json\n{\n  "question": "Which tag is used to define a hyperlink in HTML?",\n  "questionRelatedTopic": ["HTML Links"],\n  "options": ["<a>", "<h1>", "<p>", "<div>"],\n  "correctOption": 1,\n  "explanation": "The <a> tag is used to define a hyperlink in HTML. It is used to link one web page to another or a specific section within the same page."\n}\n```\n\n3. \n```json\n{\n  "question": "Which tag is used to define the main heading in HTML?",\n  "questionRelatedTopic": ["HTML Headings"],\n  "options": ["<h1>", "<h2>", "<h3>", "<h4>"],\n  "correctOption": 0,\n  "explanation": "The <h1> tag is used to define the main heading in HTML. It represents the highest level of heading and is usually used for the page title."\n}\n```\n\n4. \n```json\n{\n  "question": "What is the correct way to add a comment in HTML?",\n  "questionRelatedTopic": ["HTML Comments"],\n  "options": ["<!-- This is a comment -->", "// This is a comment", "/* This is a comment */", "# This is a comment"],\n  "correctOption": 0,\n  "explanation": "The correct way to add a comment in HTML is <!-- This is a comment -->. Comments are used to add notes or explanations that are ignored by the browser."\n}\n```\n\n5. \n```json\n{\n  "question": "Which attribute is used to specify the CSS style for an element in HTML?",\n  "questionRelatedTopic": ["HTML Styles"],\n  "options": ["class", "id", "style", "src"],\n  "correctOption": 2,\n  "explanation": "The \'style\' attribute is used to specify the CSS style for an element in HTML. It allows you to define inline styles directly on the element."\n}\n```\n\nPlease note that the correctOption value represents the index of the correct option within the options array (starting from 0).']
'''
# Split the text into individual questions using regex
questions_text = re.split(r'\d+\.\s+', txt)[1:]

print("======================",questions_text,"=======================")
# Initialize a list to store the extracted questions
questions = []
# Iterate through the extracted question text
for question_text in questions_text:
    # Use regex to extract relevant information from each question
    question_info = re.search(r'(\d+)\.\s+```json(.*?)```', question_text, re.DOTALL)
    print(question_info)
    if question_info:
        question_number = question_info.group(1)
        question_json = question_info.group(3)

        # Load the extracted JSON data as a dictionary
        question_dict = json.loads(question_json)

        # Append the question dictionary to the list
        questions.append(question_dict)

# Print the list of questions (now in JSON format)
print(json.dumps(questions, indent=2))