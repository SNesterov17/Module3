calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(string):
    count_calls()
    return (len(string), string.upper(),string.lower())
def is_contains(string, list_to_search):
    count_calls()
    return string.lower() in [item.lower() for item in list_to_search]
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(string_info('Абракадабра'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(is_contains('циркуль', ['циркуляр', 'циркуляция']))
print(is_contains('Русло', ['карусель', 'РуСЛО', 'Кресло']))
print(calls)