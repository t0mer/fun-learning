
from loguru import logger
from card import RfIdCard
from sqlalchemy import create_engine
import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import exc, text
from pymysql.err import IntegrityError
from sqlalchemy.orm import sessionmaker
from items import Item


class SqliteConnector:

    def __init__(self):
        self.engine = db.create_engine("mysql+pymysql://root:T0mer!2405-77@localhost/tags", echo=True)

   
    def get_card_types(self, api_call=False):
        card_types = []
        logger.debug("api_call = " + str(api_call))
        try:
            with self.engine.connect() as connection:
                ResultProxy = connection.execute(text('SELECT CardTypeId, CardTypeName, TableName from card_types'))
                ResultSet = ResultProxy.fetchall()
                if api_call == True:
                    for row in ResultSet:
                        json_row = {
                        "CardTypeId": row.CardTypeId,
                        "CardTypeName": row.CardTypeName,
                        "CardItemType": row.TableName
                    }
                        card_types.append(json_row)
                    return card_types
                else:
                    for row in ResultSet:
                        card_types.append(Letter(row[0],row[1],row[2]))
                    return card_types
        except Exception as e:
            logger.error(str(e))
            return card_types

    def get_items(self, table_name, api_call=False):
        items = []
        logger.debug("api_call = " + str(api_call))
        try:
            with self.engine.connect() as connection:
                ResultProxy = connection.execute(text(f"SELECT Id, ItemId, Item from {table_name}"))
                ResultSet = ResultProxy.fetchall()
                if api_call == True:
                    for row in ResultSet:
                        json_row = {
                        "Id": row.Id,
                        "ItemId": row.ItemId,
                        "Item": row.Item
                    }
                        items.append(json_row)
                    return items
                else:
                    for row in ResultSet:
                        items.append(Letter(row[0],row[1],row[2]))
                    return items
        except Exception as e:
            logger.error(str(e))
            return items




    def get_cards(self, api_call=False):
        rfid_cards = []
        logger.debug("api_call = " + str(api_call))
        try:
            with self.engine.connect() as connection:
                ResultProxy = connection.execute(text('SELECT Id, CardId, HebrewLetterId, EnglishLetterId, NumberId FROM rfid_cards'))
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
                connection.execute(text(query))
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