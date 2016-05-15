from __future__ import print_function

from urlparse import parse_qs

import os
import sys
import json
import logging
import re

log = logging.getLogger()
log.setLevel(logging.DEBUG)

here = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(here, "../lib"))
sys.path.append(os.path.join(here, "../vendored"))

from lib.model.slack import SlackResponseMessage, SlackCommand, SlackException, SlackResponseType


def handler(event, context):
    log.debug("Received event {}".format(json.dumps(event)))

    try:
        command = SlackCommand(parse_qs(event['body'], 1))
    except SlackException as e:
        log.debug(e.message)
        return SlackResponseMessage(e.message).build()

    return handle_command(command)


def handle_command(command):
    channel = SlackResponseType.ephemeral

    if command is None or command.text is None:
        text = 'command is missing'
    elif command.text == '':
        text = 'Please take your discussion elsewhere'
    elif re.match('^#[0-9a-zA-Z-]+', command.text):
        text = 'Please take your discussion to {}'.format(command.text)
        channel = command.text
    else:
        text = '{} is invalid command'.format(command)

    return SlackResponseMessage(text, channel).build()
