def test_looking_for_button_add_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    btn=browser.find_element_by_css_selector(".btn-add-to-basket")

    assert btn != [], "button isn't found"
