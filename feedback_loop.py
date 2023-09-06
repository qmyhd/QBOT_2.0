import json
import logging

# Initialize logging
logging.basicConfig(filename='feedback_loop.log', level=logging.INFO)

# Function to prompt for feedback
def prompt_for_feedback():
    action_handlers = [
        'generate_cover_letter', 
        'generate_follow_up_email_content',
        'generate_resume',
        'prepare_for_behavioral_interview',
        'prepare_for_consulting_interview',
        'generate_networking_email',
        'tailor_answers_for_position'
    ]  # Add other handlers here
    
    feedback_data = {}
    
    print("Feedback Form:")
    
    for handler in action_handlers:
        print(f"\nPlease provide feedback for {handler}:")
        
        effectiveness = int(input("Effectiveness (1-5): "))
        comments = input("Comments: ")
        
        feedback_data[handler] = {'effectiveness': effectiveness, 'comments': comments}

    return {'action_handlers_feedback.json': feedback_data}

# Function to collect feedback
def collect_feedback(parsed_data):
    feedback_data = parsed_data.get('action_handlers_feedback.json', {})
    return feedback_data

# Function to analyze feedback
def analyze_feedback(feedback_data):
    improvement_suggestions = {}
    for handler, feedback in feedback_data.items():
        effectiveness = feedback.get('effectiveness', 0)
        comments = feedback.get('comments', '')
        
        if effectiveness < 4:
            suggestion = f"Consider revising {handler}. Feedback: {comments}"
        else:
            suggestion = f"{handler} is performing well. Feedback: {comments}"
        
        logging.info(suggestion)
        improvement_suggestions[handler] = suggestion

    return improvement_suggestions

if __name__ == "__main__":
    # Trigger feedback form
    if input("Would you like to provide feedback? (y/n): ").lower() == 'y':
        parsed_data = prompt_for_feedback()

        # Collect and analyze feedback
        feedback_data = collect_feedback(parsed_data)
        improvement_suggestions = analyze_feedback(feedback_data)
        
        print("Improvement Suggestions:")
        for handler, suggestion in improvement_suggestions.items():
            print(f"{handler}: {suggestion}")
