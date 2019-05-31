import requests
from environs import Env
from datetime import *

WEBEX_ROOT_URL = 'https://api.ciscospark.com'


def post_to_room(bot_token, room_id):

    # Send a message to a room
    payload = {'markdown': '@All - Timesheets!!'}
    payload['roomId'] = room_id

    response = requests.post(WEBEX_ROOT_URL + '/v1/messages', headers={
        'Authorization': 'Bearer ' + bot_token,
        'Content-Type': 'application/json; charset=utf-8'
    }, json=payload)
    return response


if __name__ == '__main__':

    ENV = Env()
    ENV.read_env()

    BOT_TOKEN = ENV('bot_token')
    ROOM_ID = ENV('room_id')

    # Post reminder to room
    post_to_room(BOT_TOKEN, ROOM_ID)
