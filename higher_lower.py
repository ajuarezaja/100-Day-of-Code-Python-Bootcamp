import random
from art import logo, vs
import game_data

max_score = 0


def get_first_data(name="", job="", country="", followers=""):
    ''' Get the data for the A player from the list in game_data.py file'''
    if name == "":
        first_data = random.choice(game_data.data)
        name = first_data["name"]
        job = first_data["description"]
        country = first_data['country']
        followers =  first_data['follower_count']
    return name, job, country, followers
    
    
def get_second_data():
    ''' Get the data for the B player from the list in game_data.py file'''
    second_data = random.choice(game_data.data)
    name = second_data["name"]
    job = second_data["description"]
    country = second_data['country']
    followers = second_data['follower_count']
    return name, job, country, followers


def compare_followers(a_followers, b_followers):
    '''Get the player with more followers'''
    if a_followers > b_followers:
        winner = 'a'
    elif b_followers > a_followers:
        winner = 'b'
    else:
        winner = 't'
    return winner


def guess_correct(option, real):
    global score
    if option == real:
        score += 1
        print(f"You're right!!!! Current Score: {score} ")
        return True
    elif real == "t":
        score += 1
        print(f"Is a tie but counts as good!!!, Current Score: {score} ")
        return True
    else:
        print(f"I'm sorry, wrong answer!, Last Score: {score}")
        return False


def max_score_counter():
    ''' Max Score counting'''
    global score, max_score
    if score > max_score:
        max_score = score
        print(f'New Max Score: {max_score}!!!')
    else:
        print(f'Score last game: {score}')
        print(f'Max Score: {max_score}')


first_name = ''
second_name = ''
continue_playing = True
next_attempt = True

while next_attempt:
    first_name = ''
    second_name = ''
    continue_playing = True
    score = 0
    while continue_playing:
        print(logo)
        # check if is the first game or not. First game must take first data from game_data.py file
        # later games must take data from second player
        if first_name == '':
            first_name, first_job, first_country, first_followers = get_first_data()
        print(f'Compare A: {first_name}, a {first_job} from {first_country}')
        print(vs)
        # This while is to prevent repeat player A and player B
        while second_name == '':
            second_name, second_job, second_country, second_followers = get_second_data()
            if second_name == first_name:
                second_name, second_job, second_country, second_followers = get_second_data()
            elif second_name != first_name:
                break
        print(f'Against B: {second_name}, a {second_job} from {second_country}')
        # Check who is the winner
        who_wins = compare_followers(first_followers, second_followers)
        guess = input("Who has more followers?: Type 'A' or 'B' ").lower()
        continue_playing = guess_correct(guess, who_wins)
        # Passing Player B information to Player A and resetting player B for new information for next round
        if continue_playing:
            first_name, first_job, first_country, first_followers = second_name, second_job, second_country, \
                                                                    second_followers
            second_name, second_job, second_country, second_followers = "", "", "", "",
    # Check if want more attempts to play and modify scores
    more_attempts = input("Want to play again? Type 'YES' or 'NO: ").lower()
    if more_attempts == 'yes':
        max_score_counter()
    else:
        max_score_counter()
        next_attempt = False
