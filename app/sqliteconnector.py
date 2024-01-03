
from loguru import logger
from card import RfIdCard
from sqlalchemy import create_engine
import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import exc
from pymysql.err import IntegrityError
from sqlalchemy.orm import sessionmaker
from letters import Letter, Number


class SqliteConnector:

    def __init__(self):
        self.engine = db.create_engine("mysql+pymysql://root:T0mer!2405-77@localhost/tags", echo=True)

   
    def get_hebrew_letters(self, api_call=False):
        hebrew_letters = []
        logger.debug("api_call = " + str(api_call))
        try:
            with self.engine.connect() as connection:
                ResultProxy = connection.execute('SELECT Id, LetterId, Letter from hebrew_letters')
                ResultSet = ResultProxy.fetchall()
                if api_call == True:
                    for row in ResultSet:
                        json_row = {
                        "Id": row.Id,
                        "LetterId": row.LetterId,
                        "Letter": row.Letter
                    }
                        hebrew_letters.append(json_row)
                    return hebrew_letters
                else:
                    for row in ResultSet:
                        hebrew_letters.append(Letter(row[0],row[1],row[2]))
                    return hebrew_letters
        except Exception as e:
            logger.error(str(e))
            return hebrew_letters



    def get_english_letters(self, api_call=False):
        english_letters = []
        logger.debug("api_call = " + str(api_call))
        try:
            with self.engine.connect() as connection:
                ResultProxy = connection.execute('SELECT Id, LetterId, Letter from english_letters')
                ResultSet = ResultProxy.fetchall()
                if api_call == True:
                    for row in ResultSet:
                        json_row = {
                        "Id": row.Id,
                        "LetterId": row.LetterId,
                        "Letter": row.Letter
                    }
                        english_letters.append(json_row)
                    return english_letters
                else:
                    for row in ResultSet:
                        english_letters.append(Letter(row[0],row[1],row[2]))
                    return english_letters
        except Exception as e:
            logger.error(str(e))
            return english_letters


    def get_numbers(self, api_call=False):
        numbers = []
        logger.debug("api_call = " + str(api_call))
        try:
            with self.engine.connect() as connection:
                ResultProxy = connection.execute('SELECT Id, NumberId, Number FROM numbers')
                ResultSet = ResultProxy.fetchall()
                if api_call == True:
                    for row in ResultSet:
                        json_row = {
                        "Id": row.Id,
                        "NumberId": row.NumberId,
                        "Number": row.Number
                    }
                        numbers.append(json_row)
                    return numbers
                else:
                    for row in ResultSet:
                        numbers.append(Number(row[0],row[1],row[2]))
                    return numbers
        except Exception as e:
            logger.error(str(e))
            return numbers

    def get_cards(self, api_call=False):
        rfid_cards = []
        logger.debug("api_call = " + str(api_call))
        try:
            with self.engine.connect() as connection:
                ResultProxy = connection.execute('SELECT Id, CardId, HebrewLetterId, EnglishLetterId, NumberId FROM rfid_cards')
                ResultSet = ResultProxy.fetchall()
                if api_call == True:
                    for row in ResultSet:
                        json_row = {
                        "Id": row.Id,
                        "CardId": row.CardId,
                        "HebrewLetterId": row.HebrewLetterId,
                        "EnglishLetterId": row.HebrewLetterId,
                        "NumberId": row.NumberId,
                        
                    }
                        rfid_cards.append(json_row)
                    return rfid_cards
                else:
                    for row in ResultSet:
                        rfid_cards.append(RfIdCard(row[0],row[1],row[2],row[3],row[4]))
                    return rfid_cards
        except Exception as e:
            logger.error(str(e))
            return rfid_cards



    def add_new_card(self, rfidcard):
        try:
            with self.engine.connect() as connection:
                query = f"INSERT INTO rfid_cards (CardId,HebrewLetterId,EnglishLetterId,NumberId)" \
                f"VALUES ('{rfidcard.CardId}', {rfidcard.HebrewLetterId}, {rfidcard.EnglishLetterId}, {rfidcard.NumberId})"    
                connection.execute(query)
                return True, "The card has been added successfuly"
        except exc.IntegrityError as e:
            logger.warning(str(e))
            return False, "Duplicate entry, Card Already exists"            
        except Exception as e:
            logger.error(str(e))
            return False, str(e)





# if __name__ == "__main__":
#     con = SqliteConnector()
#     con.create_tables()