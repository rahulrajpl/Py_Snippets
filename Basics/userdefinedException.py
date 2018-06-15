class Accident(Exception):
    def __init__(self, msg):
        self.msg = msg
    def print_exception(self):
        print("User defined Exception:", self.msg)

try:
    raise Accident("Crash Between Two cars")
except Accident as e:
    e.print_exception();
finally:
    print("This is printed no matter what exception")