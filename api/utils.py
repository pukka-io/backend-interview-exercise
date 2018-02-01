
from .models import Message

def instantiate_reward_message(first_name, points):
    if (points % 10) == 0:
        text = 'Congratulations {}, you reach a total of {} points !'.format(
            first_name,
            points,
            )

        return Message(type=Message.ACTION, text=text)

    return False
