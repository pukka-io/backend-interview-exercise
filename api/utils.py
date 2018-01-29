
from .models import Message

def instantiate_reward_message(first_name, points):
    text = 'Congratulations {}, you reach a total of {} points !'.format(
        first_name,
        points,
    )
    return Message(type=Message.ACTION, text=text)
