/** @odoo-module **/
import { patch } from "@web/core/utils/patch";
import { WebsiteSale } from "@website_sale/interactions/website_sale";

patch(WebsiteSale.prototype, {
    /**
     * @override
     */
    _onChangeCombination(ev, parent, combination) {
        super._onChangeCombination(...arguments);

        const ecotaxContainer = parent.querySelector('.o_ecotax_amounts');
        if (ecotaxContainer) {
            ecotaxContainer.innerHTML = combination.ecotax_html || '';
        }
    },
});
