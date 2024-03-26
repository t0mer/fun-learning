-- Add Hebrew letters
INSERT INTO hebrew_letters (ItemId, Item)VALUES (1,"א");
INSERT INTO hebrew_letters (ItemId, Item)VALUES (2,"ב");
INSERT INTO hebrew_letters (ItemId, Item)VALUES (3,"ג");
INSERT INTO hebrew_letters (ItemId, Item)VALUES (4,"ד");
INSERT INTO hebrew_letters (ItemId, Item)VALUES (5,"ה");
INSERT INTO hebrew_letters (ItemId, Item)VALUES (6,"ו");
INSERT INTO hebrew_letters (ItemId, Item)VALUES (7,"ז");
INSERT INTO hebrew_letters (ItemId, Item)VALUES (8,"ח");
INSERT INTO hebrew_letters (ItemId, Item)VALUES (9,"ט");
INSERT INTO hebrew_letters (ItemId, Item)VALUES (10,"י");
INSERT INTO hebrew_letters (ItemId, Item)VALUES (11,"כ");
INSERT INTO hebrew_letters (ItemId, Item)VALUES (12,"ל");
INSERT INTO hebrew_letters (ItemId, Item)VALUES (13,"מ");
INSERT INTO hebrew_letters (ItemId, Item)VALUES (14,"נ");
INSERT INTO hebrew_letters (ItemId, Item)VALUES (15,"ס");
INSERT INTO hebrew_letters (ItemId, Item)VALUES (16,"ע");
INSERT INTO hebrew_letters (ItemId, Item)VALUES (17,"פ");
INSERT INTO hebrew_letters (ItemId, Item)VALUES (18,"צ");
INSERT INTO hebrew_letters (ItemId, Item)VALUES (19,"ק");
INSERT INTO hebrew_letters (ItemId, Item)VALUES (20,"ר");
INSERT INTO hebrew_letters (ItemId, Item)VALUES (21,"ש");
INSERT INTO hebrew_letters (ItemId, Item)VALUES (22,"ת");


-- Add English letters
INSERT INTO english_letters (ItemId, Item)VALUES (1,"A");
INSERT INTO english_letters (ItemId, Item)VALUES (2,"B");
INSERT INTO english_letters (ItemId, Item)VALUES (3,"C");
INSERT INTO english_letters (ItemId, Item)VALUES (4,"D");
INSERT INTO english_letters (ItemId, Item)VALUES (5,"E");
INSERT INTO english_letters (ItemId, Item)VALUES (6,"F");
INSERT INTO english_letters (ItemId, Item)VALUES (7,"G");
INSERT INTO english_letters (ItemId, Item)VALUES (8,"H");
INSERT INTO english_letters (ItemId, Item)VALUES (9,"I");
INSERT INTO english_letters (ItemId, Item)VALUES (10,"J");
INSERT INTO english_letters (ItemId, Item)VALUES (11,"K");
INSERT INTO english_letters (ItemId, Item)VALUES (12,"L");
INSERT INTO english_letters (ItemId, Item)VALUES (13,"M");
INSERT INTO english_letters (ItemId, Item)VALUES (14,"N");
INSERT INTO english_letters (ItemId, Item)VALUES (15,"O");
INSERT INTO english_letters (ItemId, Item)VALUES (16,"P");
INSERT INTO english_letters (ItemId, Item)VALUES (17,"Q");
INSERT INTO english_letters (ItemId, Item)VALUES (18,"R");
INSERT INTO english_letters (ItemId, Item)VALUES (19,"S");
INSERT INTO english_letters (ItemId, Item)VALUES (20,"T");
INSERT INTO english_letters (ItemId, Item)VALUES (21,"U");
INSERT INTO english_letters (ItemId, Item)VALUES (22,"V");
INSERT INTO english_letters (ItemId, Item)VALUES (23,"W");
INSERT INTO english_letters (ItemId, Item)VALUES (24,"X");
INSERT INTO english_letters (ItemId, Item)VALUES (25,"Y");
INSERT INTO english_letters (ItemId, Item)VALUES (26,"Z");


-- Add Numbers
INSERT INTO numbers (ItemId, Item)VALUES (1,"0");
INSERT INTO numbers (ItemId, Item)VALUES (2,"1");
INSERT INTO numbers (ItemId, Item)VALUES (3,"2");
INSERT INTO numbers (ItemId, Item)VALUES (4,"3");
INSERT INTO numbers (ItemId, Item)VALUES (5,"4");
INSERT INTO numbers (ItemId, Item)VALUES (6,"5");
INSERT INTO numbers (ItemId, Item)VALUES (7,"6");
INSERT INTO numbers (ItemId, Item)VALUES (8,"7");
INSERT INTO numbers (ItemId, Item)VALUES (9,"8");
INSERT INTO numbers (ItemId, Item)VALUES (10,"9");
INSERT INTO numbers (ItemId, Item)VALUES (11,"10");


-- Add CardTypes
INSERT INTO card_types (CardTypeId, CardTypeName, TableName)VALUES (0,"Hebrew Letters","hebrew_letters");
INSERT INTO card_types (CardTypeId, CardTypeName, TableName)VALUES (1,"English Letters","english_letters");
INSERT INTO card_types (CardTypeId, CardTypeName, TableName)VALUES (2,"Numbers","numbers");




CREATE TABLE IF NOT EXISTS hebrew_letters (
                                    Id int PRIMARY KEY AUTO_INCREMENT,
                                    ItemId int NOT NULL UNIQUE,
                                    Item text NOT NULL);
                                    
CREATE TABLE IF NOT EXISTS english_letters (
                                    Id int PRIMARY KEY AUTO_INCREMENT,
                                    ItemId int NOT NULL UNIQUE,
                                    Item text NOT NULL);                              
                                  

CREATE TABLE IF NOT EXISTS numbers (  Id int PRIMARY KEY AUTO_INCREMENT,
                                            ItemId int NOT NULL UNIQUE,
                                            Item int NOT NULL);
                                            
CREATE TABLE IF NOT EXISTS card_types (Id int PRIMARY KEY AUTO_INCREMENT,
                                            CardTypeId int NOT NULL UNIQUE,
                                            CardTypeName text NOT NULL,
                                            TableName text NOT NULL);
                                            

CREATE TABLE IF NOT EXISTS cards (
                                    Id integer PRIMARY KEY AUTO_INCREMENT,
                                    CardId text NOT NULL UNIQUE,
                                    CardTypeId int NOT NULL,
                                    ItemId int NOT NULL
                                    );