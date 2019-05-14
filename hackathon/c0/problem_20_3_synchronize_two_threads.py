from threading import Lock, Thread, Event

lock = Lock()

event = Event()


def is_odd_turn(event_state):
    return event_state is False


def is_even_turn(event_state):
    return event_state is True


def switch_to_even(event_object):
    event_object.set()


def switch_to_odd(event_object):
    event_object.clear()


def odd_thread():
    count = 1
    while count < 100:
        if is_odd_turn(event.is_set()):
            print(count, 'odd thread')
            count += 2
            switch_to_even(event)


def even_thread():
    count = 0
    while count < 100:
        if is_even_turn(event.is_set()):
            print(count, 'even thread')
            count += 2
            switch_to_odd(event)


def solution():
    oddThread = Thread(target=odd_thread, daemon=True)
    evenThread = Thread(target=even_thread, daemon=True)

    event.set()

    evenThread.start()
    oddThread.start()

    while oddThread.is_alive() or evenThread.is_alive():
        pass

    print('all threads finished!')


solution()
