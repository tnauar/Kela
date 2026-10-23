SELECT
	f.palvelukanava,
	COUNT(*) AS palaute_lkm,
	ROUND(AVG(f.palvelukokemus), 2) palaute_keskiarvo
FROM kela.asiakkaat_gold p
JOIN kela.asiakasymmärrys_gold f ON f.asiakas_id = p.asiakas_id
WHERE p.sukupuoli = 'N'
AND p.koulutustaso = 'ylempi korkeakoulututkinto'
GROUP BY f.palvelukanava
ORDER BY palaute_keskiarvo DESC;
