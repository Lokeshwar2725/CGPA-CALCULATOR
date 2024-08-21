from flask import Flask, render_template, request

app = Flask(__name__)

# Define the subjects and their credits for each semester
subjects = {
    1: {"Engineering Chemistry": 3, "C Programming": 3, "Communicative English": 2, "MDIC": 4, 
        "Engineering Graphics": 4, "Communicative English Lab": 1, "Engineering Chemistry Lab": 1, "C Programming Lab": 2},
    2: {"QA&VR": 1, "IICT": 3, "BEECE": 3, "Python Programming": 4, "VCCF": 4, 
        "Engineering Physics": 3, "COI": 0, "Physics Lab": 1},
    3: {"Fundamental of Nanoscience": 0, "Quantitative Aptitude and Behavioral Skills": 1, "Data Structure": 3, 
        "Digital Logic Circuits": 4, "Computer Architecture": 3, "Mathematics for Data Analysis": 4, 
        "Object Oriented Programming Paradigm in C++ and Java": 3, "Heritage of Tamil": 1},
    4: {"Queuing Theory & Optimization": 4, "Principals of Artificial Intelligence": 3, "EVS": 0, 
        "Quantitative Aptitude and Communication Skills": 1, "Operating System": 3, "Design & Analysis of Algorithms": 4, 
        "Database Management System": 3, "Tamils and Technology": 1},
    5: {"Machine Learning and its Techniques": 4, "OOSE": 3, "Fundamentals of Data Science": 3, 
        "Statistics Foundation and Probability Distribution": 4, "NLP or ICN": 3, "MPMC": 1, 
        "Machine Learning Lab": 1, "Data Science Lab": 1},
    6: {"Data Exploration Using R": 4, "Artificial Neural Network": 4, "Advanced AI": 3, 
        "Web Technologies": 3, "Data and Information Security": 3, "Data Analytics Lab": 1, 
        "Web Technologies Lab": 1, "Mini Project": 1, "Internship": 1},
    7: {"Deep Learning": 3, "Big Data Management": 4, "IoT": 3, "Cloud Computing": 3, 
        "Information Extraction and Retrieval Techniques": 3, "Solid Waste Management": 3, 
        "Deep Learning Lab": 1, "IoT Lab": 1},
    8: {"Software Testing and Quality Assurance": 3, "Edge and Fog Computing": 3, "Project Phase 2": 6}
}

grade_points = {'O': 10, 'A+': 9, 'A': 8, 'B+': 7, 'B': 6, 'C': 5, 'arrear': 0}

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/semester', methods=['POST'])
def semester():
    semesters = int(request.form['semesters'])
    return render_template('semester.html', semesters=semesters, subjects=subjects)

@app.route('/result', methods=['POST'])
def result():
    total_points = 0
    total_credits = 0
    arrear = False

    for sem in range(1, len(subjects) + 1):
        grades = request.form.getlist(f'grades{sem}[]')
        if len(grades) > 0:
            for grade, (subject, credit) in zip(grades, subjects[sem].items()):
                if grade == 'arrear':
                    arrear = True
                total_points += grade_points[grade] * credit
                total_credits += credit

    if arrear:
        return render_template('result.html', arrear=True)
    
    cgpa = round(total_points / total_credits, 2)
    return render_template('result.html', cgpa=cgpa, arrear=False)

if __name__ == '__main__':
    app.run(debug=True)
