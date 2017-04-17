import json
import logging

from django.template.loader import render_to_string
from django.http import HttpResponseForbidden, HttpResponseBadRequest, JsonResponse
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.conf import settings

import telepot
from config.settings.base import TELEGRAM_BOT_TOKEN, TELEGRAM_WEBHOOK_BASE, TELEGRAM_WEBHOOK_SITE

TelegramBot = telepot.Bot(TELEGRAM_BOT_TOKEN)
TelegramBot.setWebhook('{site}/{base}/bot/{bot_token}/'.format(site=TELEGRAM_WEBHOOK_SITE, base=TELEGRAM_WEBHOOK_BASE,
                                                               bot_token=TELEGRAM_BOT_TOKEN))
logger = logging.getLogger('telegram.bot')


def _display_help():
    return "Hello"


class CommandReceiveView(View):
    def post(self, request, bot_token):
        if bot_token != settings.TELEGRAM_BOT_TOKEN:
            return HttpResponseForbidden('Invalid token')

        commands = {
            '/start': _display_help,
            'help': _display_help,
        }

        raw = request.body.decode('utf-8')
        logger.info(raw)

        try:
            payload = json.loads(raw)
        except ValueError:
            return HttpResponseBadRequest('Invalid request body')
        else:
            chat_id = payload['message']['chat']['id']
            cmd = payload['message'].get('text')  # command

            func = commands.get(cmd.split()[0].lower())
            if func:
                TelegramBot.sendMessage(chat_id, func(), parse_mode='Markdown')
            else:
                TelegramBot.sendMessage(chat_id, 'I do not understand you, Sir!')

        return JsonResponse({}, status=200)

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(CommandReceiveView, self).dispatch(request, *args, **kwargs)
