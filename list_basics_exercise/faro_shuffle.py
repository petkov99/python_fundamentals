received_card = input().split()
faro_shuffles = int(input())

for shuffle in range(faro_shuffles):
    middle_of_the_deck = len(received_card) // 2
    left_part = received_card[0:middle_of_the_deck]
    right_part = received_card[middle_of_the_deck:]
    deck_after_shuffle = []
    for card_index in range(len(left_part)):
        deck_after_shuffle.append(left_part[card_index])
        deck_after_shuffle.append(right_part[card_index])
    received_card = deck_after_shuffle

print(deck_after_shuffle)