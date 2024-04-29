import frappe

@frappe.whitelist()
def switch_theme(theme):
	if theme in ["Dark", "Light", "Automatic", "Tijaabo"]:
		frappe.db.set_value("User", frappe.session.user, "desk_theme", theme)