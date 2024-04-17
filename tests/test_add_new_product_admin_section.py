from page_objects.add_new_product_admin_section import AddNewProductAdminSection
from page_objects.auth_admin_catalog import AdminCatalog
from page_objects.auth_admin_page import AuthAdmin


def test_add_new_product_admin_section(browser):
    AuthAdmin(browser).admin_acc(browser)
    AuthAdmin(browser).login("user", "bitnami")
    AuthAdmin(browser).click_submit_button()
    AdminCatalog(browser).click_menu_catalog()
    AdminCatalog(browser).click_products_list()
    AddNewProductAdminSection(browser).click_add_new_product()
    AddNewProductAdminSection(browser).input_product_name("Add New Product")
    AddNewProductAdminSection(browser).scroll_down_products()
    AddNewProductAdminSection(browser).input_tag_title("Tag Title")
    AddNewProductAdminSection(browser).click_tab_data()
    AddNewProductAdminSection(browser).input_model_product("Product")
    AddNewProductAdminSection(browser).click_tab_seo()
    AddNewProductAdminSection(browser).input_keyword("test")
    AddNewProductAdminSection(browser).click_save_product()
    assert AddNewProductAdminSection(browser).success_alert_product()
