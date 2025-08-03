# interview_engine.py

questions_by_role = {
    "Software Engineer": {
        "Entry-Level": [
            "Tell me about yourself.",
            "What programming languages are you most comfortable with?",
            "Describe a recent project you've worked on."
        ],
        "Mid-Level": [
            "How do you approach code reviews?",
            "Tell me about a challenging bug you fixed.",
            "How do you ensure code quality in your team?"
        ],
        "Senior": [
            "How do you lead technical architecture decisions?",
            "Describe a time you mentored a junior developer.",
            "How do you handle technical debt?"
        ]
    },
    "Data Scientist": {
        "Entry-Level": [
            "What machine learning models are you familiar with?",
            "How do you evaluate model performance?",
            "Describe a data analysis project you've done."
        ],
        "Mid-Level": [
            "Explain how you handle imbalanced datasets.",
            "How do you decide between different ML algorithms?",
            "Describe your experience with A/B testing."
        ],
        "Senior": [
            "How do you design scalable ML systems?",
            "What’s your strategy for leading data initiatives?",
            "Explain how you align data science with business goals."
        ]
    },
    "ML Engineer": {
        "Entry-Level": [
            "What is the difference between model training and inference?",
            "Have you deployed an ML model to production?",
            "What ML frameworks have you worked with?"
        ],
        "Mid-Level": [
            "How do you monitor deployed ML models?",
            "Describe a pipeline you built for model training.",
            "How do you handle data versioning?"
        ],
        "Senior": [
            "How do you manage ML lifecycle in large systems?",
            "What tools do you use for CI/CD in ML?",
            "Describe your leadership role in ML infrastructure."
        ]
    }
}

def get_question(role, level, step):
    try:
        return questions_by_role[role][level][step]
    except IndexError:
        return "That was the final question of this mock interview."
