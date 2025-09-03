# A dictionary to group universities by country
university_data = {
    'United States': [
        {'name': 'Massachusetts Institute of Technology (MIT)', 'score': 98.1},
        {'name': 'Harvard University', 'score': 97.7},
        {'name': 'Stanford University', 'score': 97.2}
    ],
    'United Kingdom': [
        {'name': 'University of Oxford', 'score': 98.5},
        {'name': 'University of Cambridge', 'score': 97.4},
        {'name': 'Imperial College London', 'score': 94.4}
    ],
    'Switzerland': [
        {'name': 'ETH Zurich', 'score': 93.0}
    ],
    'China': [
        {'name': 'Tsinghua University', 'score': 92.5}
    ],
    'Singapore': [
        {'name': 'National University of Singapore (NUS)', 'score': 89.9}
    ]
}

class University:
    """Represents a university with its name, country, and score."""
    def __init__(self, name, country, score):
        self.name = name
        self.country = country
        self.score = score
        self.ranking_history = [{'year': 2024, 'score': score}]

    def update_score(self, year, new_score):
        """Updates the university's score and adds it to the history."""
        self.score = new_score
        self.ranking_history.append({'year': year, 'score': new_score})
        print(f"Score for {self.name} updated to {self.score} in {year}.")

    def show_progress(self):
        """Prints the score change from the initial data."""
        if len(self.ranking_history) > 1:
            initial_score = self.ranking_history[0]['score']
            current_score = self.ranking_history[-1]['score']
            score_change = current_score - initial_score
            print(f"\n--- Progress for {self.name} ({self.country}) ---")
            print(f"Initial Score: {initial_score:.2f}")
            print(f"Current Score: {current_score:.2f}")
            if score_change > 0:
                print(f"Score Change: ↑ {score_change:.2f} (Improvement)")
            elif score_change < 0:
                print(f"Score Change: ↓ {abs(score_change):.2f} (Decline)")
            else:
                print(f"Score Change: → 0.00 (No Change)")
        else:
            print(f"No progress to show for {self.name}.")

def create_university_list(data):
    """Creates a list of University objects from a dictionary."""
    universities = []
    for country, schools in data.items():
        for school in schools:
            university = University(school['name'], country, school['score'])
            universities.append(university)
    return universities

def rank_universities(universities):
    """Sorts and prints universities by their current score."""
    universities.sort(key=lambda x: x.score, reverse=True)
    print("\n*** World University Ranking by Score ***")
    for i, uni in enumerate(universities):
        print(f"#{i+1}: {uni.name} ({uni.country}) - Score: {uni.score}")

# Main program flow
if __name__ == "__main__":
    # Create a list of University objects
    university_list = create_university_list(university_data)

    # Rank and display the initial list of universities
    rank_universities(university_list)

    # Demonstrate the use of the class method and progress tracking
    print("\n--- Simulating a ranking update for MIT ---")
    mit = None
    for uni in university_list:
        if "MIT" in uni.name:
            mit = uni
            break
    
    if mit:
        mit.update_score(2025, 98.3)
        mit.show_progress()

    # Re-rank the universities after the update
    rank_universities(university_list)