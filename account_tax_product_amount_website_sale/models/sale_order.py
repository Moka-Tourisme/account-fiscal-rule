from odoo import models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def _get_ecotax_total(self):
        """Return a dict {tax_name: total_amount} for all ecotaxes in the order."""
        result = {}
        for line in self.website_order_line:
            # sudo: `account.tax` is not readable by portal users
            for ta in line.sudo().product_id.tax_amount_ids.filtered(
                lambda t: t.type_tax_use == 'sale' and t.amount > 0
            ):
                key = ta.tax_id.name
                result[key] = result.get(key, 0.0) + ta.amount * line.product_uom_qty
        return result
