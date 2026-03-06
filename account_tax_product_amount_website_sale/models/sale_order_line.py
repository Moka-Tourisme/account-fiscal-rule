from odoo import fields, models


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    def _get_ecotax_amounts(self, website):
        """Return a list of {name, amount, price_include_override} for ecotaxes on this line, converted to website currency."""
        result = []
        currency = website.currency_id
        today = fields.Date.today()
        for ta in self.product_id.tax_amount_ids.filtered(
            lambda t: t.type_tax_use == 'sale' and t.amount > 0
        ):
            amount = ta.company_id.currency_id._convert(
                from_amount=ta.amount,
                to_currency=currency,
                company=ta.company_id,
                date=today,
            )
            result.append({
                'name': ta.tax_id.name,
                'amount': amount,
                'price_include_override': ta.tax_id.price_include_override,
            })
        return result
