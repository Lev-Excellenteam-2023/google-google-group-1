import typing
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s', datefmt='%H:%M:%S', filename='scoring.log', filemode='w')

def score_sentence(input_sentence: str, expected_sentence: str) -> int:
    """
    Receives a sentence and returns a score for it
    Rules:
    -2 points for each correct letter

    Incorrect letter:
    -5 points for first letter
    -4 points for second letter
    -3 points for third letter
    -2 points for fourth letter
    -1 point for fifth letter and above

    Erase or add letter:
    -10 points for first letter
    -8 points for second letter
    -6 points for third letter
    -4 points for fourth letter
    -2 points for fifth letter and above

    :param input_sentence: str
    :param expected_sentence: str
    :return: score: int

    """
    initial_score = len(input_sentence) * 2
    location_of_mistake = len(input_sentence) - 1

    if abs(len(input_sentence) - len(expected_sentence)) > 1:
        logging.critical('Incorrect sentence length: ' + input_sentence)
        return 0

    # Check for incorrect letters, find its position and subtract the score
    if len(input_sentence) == len(expected_sentence):
        for i in range(len(input_sentence)):
            if input_sentence[i] != expected_sentence[i]:
                location_of_mistake = i
                logging.info('Incorrect letter in sentence: ' + input_sentence + ' at position: ' + str(location_of_mistake))
                break
        if location_of_mistake <= 4:
            final_score = initial_score - 5 + location_of_mistake - 2  # -2 because there is another mistake
        else:
            final_score = initial_score - 1

    # Check for extra letter, find its position and subtract the score
    elif len(input_sentence) > len(expected_sentence):
        for i in range(len(expected_sentence)):
            if input_sentence[i] != expected_sentence[i]:
                location_of_mistake = i
                logging.info('Extra letter in sentence: ' + input_sentence + ' at position: ' + str(location_of_mistake))
                break
        if location_of_mistake <= 4:
            final_score = initial_score - 10 + 2 * location_of_mistake - 2  # -2 because we added 2 points for the extra letter
        else:
            final_score = initial_score - 2 -2 # -2 because we added 2 points for the extra letter

    # Check for missing letter, find its position and subtract the score
    elif len(input_sentence) < len(expected_sentence):
        for i in range(len(input_sentence)):
            if input_sentence[i] != expected_sentence[i]:
                location_of_mistake = i
                logging.info('Extra letter in sentence: ' + input_sentence + ' at position: ' + str(location_of_mistake))
                break
        if location_of_mistake <= 4:
            final_score = initial_score - 10 + 2 * location_of_mistake
        else:
            final_score = initial_score - 2

    return final_score




