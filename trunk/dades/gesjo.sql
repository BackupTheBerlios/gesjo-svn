--
-- Definicio de la BD 
-- de Gesjo - Gesti� Joiera
-- Josep Torrens, (C) GPL 2004.
--
--
CONNECT 'gesjo.fdb' USER 'josep' PASSWORD 'coder69';

--
-- Generadors pels camps ID
--
CREATE GENERATOR GEN_CLI_ID;
CREATE GENERATOR GEN_ARR_ID;
CREATE GENERATOR GEN_MAR_ID;
CREATE GENERATOR GEN_TAL_ID;
CREATE GENERATOR GEN_MEC_ID;


--

--
-- Dominis
--
CREATE DOMAIN DM_ID AS NUMERIC(6);
CREATE DOMAIN DM_TEL AS NUMERIC(13);
CREATE DOMAIN DM_EMAIL AS VARCHAR(128);
CREATE DOMAIN DM_WEB AS VARCHAR(255);
CREATE DOMAIN DM_NOTES AS VARCHAR(2048);
CREATE DOMAIN DM_NOM AS VARCHAR(32);
CREATE DOMAIN DM_LLINATGES AS VARCHAR(64);
CREATE DOMAIN DM_DIRECCIO AS VARCHAR(64);
CREATE DOMAIN DM_POBLACIO AS VARCHAR(20);
CREATE DOMAIN DM_CODIPOSTAL AS NUMERIC(5);
CREATE DOMAIN DM_MONEDA AS NUMERIC(5,3);




--
-- Les Taules
--
--
CREATE TABLE CLIENT ( 
	ID DM_ID NOT NULL,
	NOM DM_NOM,
	LLINATGES DM_LLINATGES,
	DIRECCIO1 DM_DIRECCIO,
	DIRECCIO2 DM_DIRECCIO,
	POBLACIO DM_POBLACIO,
	CODIPOSTAL DM_CODIPOSTAL,
	TELEFON DM_TEL,
	MOBIL	DM_TEL,
	EMAIL DM_EMAIL,
	NOTES DM_NOTES,
	PRIMARY KEY(ID)
);

CREATE TABLE MARCA (
	ID DM_ID NOT NULL,
	NOM	DM_NOM,
	PRIMARY KEY(ID)
);

CREATE TABLE TALLER (
	ID DM_ID NOT NULL,
	NOM 	DM_NOM,
	DIRECCIO1 DM_DIRECCIO,
	DIRECCIO2 DM_DIRECCIO,
	TELEFON	DM_TEL,
	EMAIL DM_EMAIL,
	WEB DM_WEB,
	NOTES DM_NOTES,
	PRIMARY KEY(ID)
);

CREATE TABLE MECANIC (
	ID DM_ID NOT NULL,
	NOM DM_NOM,
	TELEFON DM_TEL,
	TALLER_ID DM_ID,
	PRIMARY KEY (ID),
	FOREIGN KEY (TALLER_ID) REFERENCES TALLER(ID)
	
);

CREATE TABLE ARREGLO (
	ID DM_ID NOT NULL,
	CLIENT_ID DM_ID NOT NULL,
	MARCA_ID DM_ID NOT NULL,
	MODEL	VARCHAR(80),
	DATA_ENTRADA DATE,
	DATA_TALLER DATE,
	DATA_TORNADA DATE,
	DATA_ENTREGA DATE,
	MECANIC_ID DM_ID,
	COST DM_MONEDA,
	PVP DM_MONEDA,
	NOTES DM_NOTES,
	PRIMARY KEY (ID),
	FOREIGN KEY (CLIENT_ID) REFERENCES CLIENT(ID),
	FOREIGN KEY (MARCA_ID) REFERENCES MARCA(ID),
	FOREIGN KEY (MECANIC_ID) REFERENCES MECANIC(ID)
);



-- Triger pels generadors
--
--

-- Taula clients
SET TERM !! ;
CREATE TRIGGER INSERT_GEN_CLI_ID FOR CLIENT
 BEFORE INSERT POSITION 0
 AS BEGIN
	NEW.ID = GEN_ID(GEN_CLI_ID,1);
END
SET TERM ; !!


-- Taula arreglos
SET TERM !! ;
CREATE TRIGGER INSERT_GEN_ARR_ID FOR ARREGLO
 BEFORE INSERT POSITION 0
 AS BEGIN
	NEW.ID = GEN_ID(GEN_ARR_ID,1);
END
SET TERM ; !!


-- Taula marca
SET TERM !! ;
CREATE TRIGGER INSERT_GEN_MAR_ID FOR MARCA
 BEFORE INSERT POSITION 0
 AS BEGIN
	NEW.ID = GEN_ID(GEN_MAR_ID,1);
END
SET TERM ; !!


-- Taula taller
SET TERM !! ;
CREATE TRIGGER INSERT_GEN_TAL_ID FOR TALLER
 BEFORE INSERT POSITION 0
 AS BEGIN
	NEW.ID = GEN_ID(GEN_TAL_ID,1);
END
SET TERM ; !!


-- Taula mecanic
SET TERM !! ;
CREATE TRIGGER INSERT_GEN_MEC_ID FOR MECANIC
 BEFORE INSERT POSITION 0
 AS BEGIN
	NEW.ID = GEN_ID(GEN_MEC_ID,1);
END
SET TERM ; !!

