from . import models
from odoo import api, SUPERUSER_ID
import logging


_logger = logging.getLogger(__name__)


def _install_insert_account_type(env):
    chart = env.ref('mjb_l10n_cn.l10n_gen_chart_china')
    china = env.ref('base.cn')
    for acc_template in env['account.account.template'].search([('chart_template_id', '=', chart.id)]):
        acc = env['account.account'].search([
            ('code', '=', acc_template.code),
            ('company_id.partner_id.country_id', '=', china.id),
        ])
        if acc:
            acc.write({
                'china_account_type': acc_template.china_account_type.id
            })


def post_init_hook(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    _install_insert_account_type(env)
