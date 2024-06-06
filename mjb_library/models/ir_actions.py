# -*- encoding: utf-8 -*-
import json
import ast
import logging
import base64
import requests
import random
import urllib
import hashlib
import hmac
import xmlrpc.client
from odoo import api, models, fields

_logger = logging.getLogger(__name__)


class ServerActions(models.Model):

    _inherit = 'ir.actions.server'

    # ----------------------------------------------------------
    # Functions
    # ----------------------------------------------------------

    @api.model
    def _get_eval_context(self, action=None):
        eval_context = super(
            ServerActions, self)._get_eval_context(action=action)

        eval_context.update({
            'mb': {
                'json': json,
                'random': random,
                'hashlib': hashlib,
                'hmac': hmac,
                'urllib': urllib,
                'ast': ast,
                'requests': requests,
                'base64': base64,
                'xmlrpc.client': xmlrpc.client
            }
        })
        return eval_context
