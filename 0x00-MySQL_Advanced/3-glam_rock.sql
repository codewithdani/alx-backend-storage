-- List bands with Glam rock as their main style, ranked by longevity
SELECT
    band_name,
    YEAR('2022-01-01') - YEAR(formed) AS lifespan
FROM
    metal_bands
WHERE
    style LIKE '%Glam rock%'
ORDER BY
    lifespan DESC;
