-- Add Hebrew letters
INSERT INTO hebrew_letters (LetterId, Letter)VALUES (1,"א");
INSERT INTO hebrew_letters (LetterId, Letter)VALUES (2,"ב");
INSERT INTO hebrew_letters (LetterId, Letter)VALUES (3,"ג");
INSERT INTO hebrew_letters (LetterId, Letter)VALUES (4,"ד");
INSERT INTO hebrew_letters (LetterId, Letter)VALUES (5,"ה");
INSERT INTO hebrew_letters (LetterId, Letter)VALUES (6,"ו");
INSERT INTO hebrew_letters (LetterId, Letter)VALUES (7,"ז");
INSERT INTO hebrew_letters (LetterId, Letter)VALUES (8,"ח");
INSERT INTO hebrew_letters (LetterId, Letter)VALUES (9,"ט");
INSERT INTO hebrew_letters (LetterId, Letter)VALUES (10,"י");
INSERT INTO hebrew_letters (LetterId, Letter)VALUES (11,"כ");
INSERT INTO hebrew_letters (LetterId, Letter)VALUES (12,"ל");
INSERT INTO hebrew_letters (LetterId, Letter)VALUES (13,"מ");
INSERT INTO hebrew_letters (LetterId, Letter)VALUES (14,"נ");
INSERT INTO hebrew_letters (LetterId, Letter)VALUES (15,"ס");
INSERT INTO hebrew_letters (LetterId, Letter)VALUES (16,"ע");
INSERT INTO hebrew_letters (LetterId, Letter)VALUES (17,"פ");
INSERT INTO hebrew_letters (LetterId, Letter)VALUES (18,"צ");
INSERT INTO hebrew_letters (LetterId, Letter)VALUES (19,"ק");
INSERT INTO hebrew_letters (LetterId, Letter)VALUES (20,"ר");
INSERT INTO hebrew_letters (LetterId, Letter)VALUES (21,"ש");
INSERT INTO hebrew_letters (LetterId, Letter)VALUES (22,"ת");


-- Add English letters
INSERT INTO english_letters (LetterId, Letter)VALUES (1,"A");
INSERT INTO english_letters (LetterId, Letter)VALUES (2,"B");
INSERT INTO english_letters (LetterId, Letter)VALUES (3,"C");
INSERT INTO english_letters (LetterId, Letter)VALUES (4,"D");
INSERT INTO english_letters (LetterId, Letter)VALUES (5,"E");
INSERT INTO english_letters (LetterId, Letter)VALUES (6,"F");
INSERT INTO english_letters (LetterId, Letter)VALUES (7,"G");
INSERT INTO english_letters (LetterId, Letter)VALUES (8,"H");
INSERT INTO english_letters (LetterId, Letter)VALUES (9,"I");
INSERT INTO english_letters (LetterId, Letter)VALUES (10,"J");
INSERT INTO english_letters (LetterId, Letter)VALUES (11,"K");
INSERT INTO english_letters (LetterId, Letter)VALUES (12,"L");
INSERT INTO english_letters (LetterId, Letter)VALUES (13,"M");
INSERT INTO english_letters (LetterId, Letter)VALUES (14,"N");
INSERT INTO english_letters (LetterId, Letter)VALUES (15,"O");
INSERT INTO english_letters (LetterId, Letter)VALUES (16,"P");
INSERT INTO english_letters (LetterId, Letter)VALUES (17,"Q");
INSERT INTO english_letters (LetterId, Letter)VALUES (18,"R");
INSERT INTO english_letters (LetterId, Letter)VALUES (19,"S");
INSERT INTO english_letters (LetterId, Letter)VALUES (20,"T");
INSERT INTO english_letters (LetterId, Letter)VALUES (21,"U");
INSERT INTO english_letters (LetterId, Letter)VALUES (22,"V");
INSERT INTO english_letters (LetterId, Letter)VALUES (23,"W");
INSERT INTO english_letters (LetterId, Letter)VALUES (24,"X");
INSERT INTO english_letters (LetterId, Letter)VALUES (25,"Y");
INSERT INTO english_letters (LetterId, Letter)VALUES (26,"Z");


-- Add Numbers
INSERT INTO numbers (NumberId, Number)VALUES (1,"0");
INSERT INTO numbers (NumberId, Number)VALUES (2,"1");
INSERT INTO numbers (NumberId, Number)VALUES (3,"2");
INSERT INTO numbers (NumberId, Number)VALUES (4,"3");
INSERT INTO numbers (NumberId, Number)VALUES (5,"4");
INSERT INTO numbers (NumberId, Number)VALUES (6,"5");
INSERT INTO numbers (NumberId, Number)VALUES (7,"6");
INSERT INTO numbers (NumberId, Number)VALUES (8,"7");
INSERT INTO numbers (NumberId, Number)VALUES (9,"8");
INSERT INTO numbers (NumberId, Number)VALUES (10,"9");
INSERT INTO numbers (NumberId, Number)VALUES (11,"10");







CREATE TABLE IF NOT EXISTS hebrew_letters (
                                    Id int PRIMARY KEY AUTO_INCREMENT,
                                    LetterId int NOT NULL UNIQUE,
                                    Letter text NOT NULL);
                                    
CREATE TABLE IF NOT EXISTS english_letters (
                                    Id int PRIMARY KEY AUTO_INCREMENT,
                                    LetterId int NOT NULL UNIQUE,
                                    Letter text NOT NULL);                              
                                  

CREATE TABLE IF NOT EXISTS numbers (  Id int PRIMARY KEY AUTO_INCREMENT,
                                            NumberId int NOT NULL UNIQUE,
                                            Number int NOT NULL);
                                            

CREATE TABLE IF NOT EXISTS rfid_cards (
                                    Id integer PRIMARY KEY AUTO_INCREMENT,
                                    CardId text NOT NULL UNIQUE,
                                    HebrewLetterId int NOT NULL,
                                    EnglishLetterId int NOT NULL,
                                    NumberId int NOT NULL);