/** @odoo-module **/

import { registry } from '@web/core/registry';
const {Component}=owl;
class My_Note extends Component {

}
My_Note.template = "my_note.Note";
registry.category("actions").add("my_note.note_client_action", My_Note);