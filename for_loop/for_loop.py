from colorama import Fore

colors = [Fore.WHITE + "White", Fore.GREEN + "Green", Fore.RED + "Red"]

for el in colors:
    print(el, end=" ")  # White Green Red

# ########################################################################
#
# for s in colors:
#     print(s, "->", len(s), end=" ")  # White -> 5 Green -> 5 Red -> 3
#
##########################################################################
#
# num = int(input("Enter Fibonacci sequence: "))
#
# a, b = 1, 1
#
# for _ in range(num):
#     print(a, end=", ")
#     result = a, b = b, a + b
#
##########################################################################
#
# txt = input("Enter text: ").lower()  # Hello world
#
# search_letters = ["e", "p", "f", "o", "h", " "]
#
# for el in txt:
#     if el in search_letters:
#         print(f"({el}) -> in text.")
#     else:
#         print(f"({el}) -> not in text.")
#
# (h) -> in text.
# (e) -> in text.
# (l) -> not in text.
# (l) -> not in text.
# (o) -> in text.
# ( ) -> in text.
# (w) -> not in text.
# (o) -> in text.
# (r) -> not in text.
# (l) -> not in text.
# (d) -> not in text.
#
###########################################################################
#
