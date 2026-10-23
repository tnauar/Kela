CREATE TABLE kela.asiakasymmärrys_bronze (
	rivinumero INTEGER NOT NULL,
	henkilö_id INTEGER NOT NULL,
	käynnin_tyyppi VARCHAR(100) NOT NULL,
	palvelukanava VARCHAR(100) NOT NULL,
	palvelukokemus INTEGER NOT NULL,
	palauteteksti VARCHAR(1000) NOT NULL
);

