from selene.support.shared import browser
from selene import be, have


def test_positive_in_english(open_google):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_positive_in_russian(open_google):
    browser.element('[name="q"]').should(be.blank).type('википедия').press_enter()
    browser.element('[id="search"]').should(have.text('свободная энциклопедия'))


def test_negative_in_english(open_google):
    browser.element('[name="q"]').should(be.blank).type('gfhhdfhfhfhfghhfhf').press_enter()
    browser.element('[id="search"]').should(have.text('ничего не найдено'))
