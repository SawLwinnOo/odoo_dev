/** @odoo-module */
import { whenReady } from "@odoo/owl";
import { mountComponent } from "@web/env";
import { Root } from "./contact/contact";

whenReady(() => mountComponent(Root, document.body));