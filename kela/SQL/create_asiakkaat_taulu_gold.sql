CREATE TABLE kela.asiakkaat_gold
AS
SELECT *
FROM kela.asiakkaat_silver
WHERE is_valid = TRUE;

ALTER TABLE kela.asiakkaat_gold
ADD COLUMN asiakas_id BIGINT GENERATED ALWAYS AS IDENTITY;

ALTER TABLE kela.asiakkaat_gold
ADD CONSTRAINT asiakkaat_gold_pkey  PRIMARY KEY (asiakas_id);
