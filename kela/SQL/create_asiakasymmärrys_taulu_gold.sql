CREATE TABLE kela.asiakasymmärrys_gold
AS
SELECT *
FROM kela.asiakasymmärrys_silver
WHERE is_valid =TRUE;

ALTER TABLE kela.asiakasymmärrys_gold
ADD COLUMN asiakas_id BIGINT;

UPDATE kela.asiakasymmärrys_gold
SET asiakas_id = floor(random() * 5000 + 1)::bigint;

ALTER TABLE kela.asiakasymmärrys_gold
ADD CONSTRAINT fk_asiakas
FOREIGN KEY (asiakas_id)
REFERENCES kela.asiakkaat_gold(asiakas_id);
