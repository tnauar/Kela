CREATE TABLE kela.asiakasymmärrys_silver
AS
SELECT *,

CASE 
	WHEN rivinumero IS NULL THEN FALSE
	WHEN henkilö_id IS NULL THEN FALSE
	WHEN käynnin_tyyppi IS NULL OR TRIM(käynnin_tyyppi) = '' OR TRIM(käynnin_tyyppi) = 'Err' OR TRIM(käynnin_tyyppi) = 'null' THEN FALSE
	WHEN palvelukanava IS NULL OR TRIM(palvelukanava) = '' OR TRIM(palvelukanava) = 'Err' OR TRIM(palvelukanava) = 'null' THEN FALSE
	WHEN palvelukokemus IS NULL THEN FALSE
	WHEN palauteteksti IS NULL OR TRIM(palauteteksti) = '' OR TRIM(palauteteksti) = 'Err' OR TRIM(palauteteksti) = 'null' THEN FALSE
	ELSE TRUE
END		AS is_valid,
CASE
        WHEN rivinumero IS NULL THEN 'Erroneous rivinumero'
        WHEN henkilö_id IS NULL THEN 'Erroneous henkilö_id'
        WHEN käynnin_tyyppi IS NULL OR TRIM(käynnin_tyyppi) = '' OR TRIM(käynnin_tyyppi) = 'Err' OR TRIM(käynnin_tyyppi) = 'null' THEN 'Erroneus käynnin_tyyppi'
        WHEN palvelukanava IS NULL OR TRIM(palvelukanava) = '' OR TRIM(palvelukanava) = 'Err' OR TRIM(palvelukanava) = 'null' THEN 'Erroneous palvelukanava'
        WHEN palvelukokemus IS NULL THEN 'Erroneous palvelukokemus'
        WHEN palauteteksti IS NULL OR TRIM(palauteteksti) = '' OR TRIM(palauteteksti) = 'Err' OR TRIM(palauteteksti) = 'null' THEN 'Erroneous palauteteksti'

        ELSE NULL
END             AS dq_error

FROM kela.asiakasymmärrys_bronze


