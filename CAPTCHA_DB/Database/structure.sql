DROP TABLE IF EXISTS captcha;
DROP TABLE IF EXISTS image;
DROP TABLE IF EXISTS captcha_image;
DROP TABLE IF EXISTS user;

CREATE TABLE captcha(
    id varchar(165) PRIMARY KEY,
    class_target varchar(50) not null,
    solution varchar(9) not null,
    moment int not null
);

CREATE TABLE image(
    id varchar(15) PRIMARY KEY,
    class varchar(50) not null,
    reliability int not null,
    path varchar(100) not null 
);

CREATE TABLE captcha_image(
    captcha varchar(165),
    image varchar(15),
    position int not null,
    PRIMARY KEY(captcha,image),
    FOREIGN KEY(captcha) REFERENCES captcha(id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY(image) REFERENCES image(id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE user(
    username varchar(50) PRIMARY KEY,
    pw varchar(100) not null
);