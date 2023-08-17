-- script that lists all genres in hbtn_0d_tvshows_rate by their rating
SELECT tvg.name, SUM(rate) AS rating
FROM tv_genres AS tvg
INNER JOIN tv_show_genres AS tg
ON tvg.id = tg.genre_id
	INNER JOIN tv_show_ratings AS r
	ON tg.show_id = r.show_id
GROUP BY tvg.name
ORDER BY rating DESC;
