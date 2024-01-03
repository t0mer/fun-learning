class RfIdCard(object):
    CardId: str
    HebrewLetterId: int
    EnglishLetterId: int
    NumberId: int
    
    def __init__(self, CardId: str, HebrewLetterId: int, EnglishLetterId: int, NumberId: int):
        self.CardId = CardId
        self.HebrewLetterId = HebrewLetterId
        self.EnglishLetterId = EnglishLetterId
        self.NumberId = NumberId