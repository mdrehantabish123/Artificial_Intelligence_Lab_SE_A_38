from experta import *

# Define the fact class for student interests
class StudentFacts(Fact):
    pass

# Define the expert system with rules for career suggestions
class CareerExpertSystem(KnowledgeEngine):

    @Rule(StudentFacts(likes='Maths'), StudentFacts(likes='Physics'))
    def mechanical(self):
        print("Suggested Career Path: Mechanical Engineering")

    @Rule(StudentFacts(likes='Programming'), StudentFacts(likes='Maths'))
    def computer(self):
        print("Suggested Career Path: Computer Engineering")

    @Rule(StudentFacts(likes='Biology'), StudentFacts(likes='Chemistry'))
    def biotech(self):
        print("Suggested Career Path: Biotechnology")

    @Rule(StudentFacts(likes='Circuits'), StudentFacts(likes='Maths'))
    def electronics(self):
        print("Suggested Career Path: Electronics Engineering")

def main():
    engine = CareerExpertSystem()
    engine.reset()
    print("Welcome to the Career Path Expert System!")
    
    # Get user interests and clean them up
    interests = input("Enter your interests separated by commas (e.g., Maths, Physics, Programming): ")
    interests_list = [interest.strip() for interest in interests.split(',')]
    
    # Declare facts for each interest
    for interest in interests_list:
        engine.declare(StudentFacts(likes=interest))
    
    # Run the expert system engine to trigger rules
    engine.run()

if __name__ == "__main__":
    main()

