/** @odoo-module */
import { Component, useState } from "@odoo/owl";

export class Root extends Component {
    setup(){
        this.state = useState({
            "contacts": [],
        });
        this.getAllContact();
    }
    async getAllContact(){
        this.state.contacts = await this.env.services.orm.searchRead('res.partner', [], ['id', 'name','email','phone'])
    }



    static template = "contact_app.Root";
    static props = {};
}