def line(katz_deli):
    if not katz_deli:
        print("The line is currently empty.")
    else:
        current_line = [f"{i+1}. {name}" for i, name in enumerate(katz_deli)]
        print(f"The line is currently: {' '.join(current_line)}")

def take_a_number(katz_deli, name):
    katz_deli.append(name)
    position = katz_deli.index(name) + 1
    print(f"Welcome, {name}. You are number {position} in line.")

def now_serving(katz_deli):
    if not katz_deli:
        print("There is nobody waiting to be served!")
    else:
        serving_person = katz_deli.pop(0)
        print(f"Currently serving {serving_person}.")

# Example usage:
KATZ_DELI = []

take_a_number(KATZ_DELI, "Ada")
take_a_number(KATZ_DELI, "Grace")
take_a_number(KATZ_DELI, "Kent")

line(KATZ_DELI)

now_serving(KATZ_DELI)

line(KATZ_DELI)

take_a_number(KATZ_DELI, "Matz")

line(KATZ_DELI)

now_serving(KATZ_DELI)

line(KATZ_DELI)
