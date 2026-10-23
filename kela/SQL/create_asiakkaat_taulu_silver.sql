CREATE TABLE kela.asiakkaat_silver
AS
SELECT *,

CASE 
	WHEN rivinumero IS NULL THEN FALSE
	WHEN etunimi IS NULL OR TRIM(etunimi) = '' THEN FALSE
	WHEN sukunimi IS  NULL OR TRIM(sukunimi) = '' THEN FALSE
	WHEN kansalaisuus IS NULL OR TRIM(kansalaisuus) = '' THEN FALSE
	WHEN koulutustaso IS NULL OR TRIM(koulutustaso) = '' THEN FALSE
	WHEN sukupuoli IS NULL OR TRIM(sukupuoli) = '' THEN FALSE
	WHEN asiakkuustilanne IS NULL OR TRIM(asiakkuustilanne) = '' THEN FALSE
	ELSE TRUE
END			AS is_valid,

CASE 
        WHEN rivinumero IS NULL THEN 'Erroneous rivinumero'
        WHEN etunimi IS NULL OR TRIM(etunimi) = '' THEN 'Erroneous etunimi'
        WHEN sukunimi IS  NULL OR TRIM(sukunimi) = '' THEN 'Erroneous sukunimi'
        WHEN kansalaisuus IS NULL OR TRIM(kansalaisuus) = '' THEN 'Erroneous kanslaisuus'
        WHEN koulutustaso IS NULL OR TRIM(koulutustaso) = '' THEN 'Erroneous koulutustaso'
        WHEN sukupuoli IS NULL OR TRIM(sukupuoli) = '' THEN 'Erroneous sukupuoli'
        WHEN asiakkuustilanne IS NULL OR TRIM(asiakkuustilanne) = '' THEN 'Erroneous asiakastilanne'
        ELSE NULL
END                     AS dq_error

FROM kela.asiakkaat_bronze


