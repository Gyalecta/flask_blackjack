import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

    def __init__(self):
        self.cards = [Card(suit, rank) for suit in self.suits for rank in self.ranks]
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        if card.rank in ['Jack', 'Queen', 'King']:
            self.value += 10
        elif card.rank == 'Ace':
            self.value += 11
            self.aces += 1
        else:
            self.value += int(card.rank)
        self.adjust_for_ace()

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

class BlackjackGame:
    def __init__(self):
        self.reset_game()

    def reset_game(self):
        self.deck = Deck()
        self.player_hand = Hand()
        self.dealer_hand = Hand()
        self.game_over = False
        self.result = ""

    def start_game(self):
        self.reset_game()
        self.player_hand.add_card(self.deck.deal())
        self.player_hand.add_card(self.deck.deal())
        self.dealer_hand.add_card(self.deck.deal())
        self.dealer_hand.add_card(self.deck.deal())

    def hit(self):
        if not self.game_over:
            self.player_hand.add_card(self.deck.deal())
            if self.player_hand.value > 21:
                self.result = "Player busts! Dealer wins."
                self.game_over = True

    def stand(self):
        if not self.game_over:
            while self.dealer_hand.value < 17:
                self.dealer_hand.add_card(self.deck.deal())
            if self.dealer_hand.value > 21:
                self.result = "Dealer busts! Player wins."
            elif self.dealer_hand.value > self.player_hand.value:
                self.result = "Dealer wins."
            elif self.dealer_hand.value < self.player_hand.value:
                self.result = "Player wins."
            else:
                self.result = "It's a draw."
            self.game_over = True

    def get_game_state(self):
        return {
            "player_hand": [self.card_to_string(card) for card in self.player_hand.cards],
            "dealer_hand": [self.card_to_string(card) for card in self.dealer_hand.cards] if self.game_over else [self.card_to_string(self.dealer_hand.cards[0]), "🂠"],
            "player_value": self.player_hand.value,
            "dealer_value": self.dealer_hand.value if self.game_over else "?",
            "result": self.result,
            "game_over": self.game_over
        }

    def card_to_string(self, card):
        suits = {'Hearts': '♥', 'Diamonds': '♦', 'Clubs': '♣', 'Spades': '♠'}
        ranks = {'Jack': 'J', 'Queen': 'Q', 'King': 'K', 'Ace': 'A'}
        rank = ranks.get(card.rank, card.rank)
        suit = suits[card.suit]
        return f"{rank}{suit}"