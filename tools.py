def create_study_plan(subject, days):

    topics = [
        "Basics and Introduction",
        "Variables and Data Types",
        "Operators and Expressions",
        "Conditional Statements",
        "Loops",
        "Functions",
        "Practice and Revision"
    ]

    plan = []

    for i in range(days):

        topic = topics[i % len(topics)]

        plan.append(
            f"Day {i + 1}: {topic}"
        )

    return "\n".join(plan)


def create_quiz(subject):

    quiz = f"""
Quiz: {subject}

1. What is {subject}?

A) Option A
B) Option B
C) Option C
D) Option D

2. What is an important concept in {subject}?

A) Option A
B) Option B
C) Option C
D) Option D

3. Which statement is correct about {subject}?

A) Option A
B) Option B
C) Option C
D) Option D
"""

    return quiz