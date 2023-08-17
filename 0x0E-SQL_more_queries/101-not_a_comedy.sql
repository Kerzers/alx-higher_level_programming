-- script that lists all shows without the genre Comedy in hbtn_0d_tvshows.
SELECT DISTINCT t.title
FROM tv_shows AS t
LEFT JOIN tv_show_genres AS tg
ON t.id = tg.show_id
	LEFT JOIN tv_genres AS tvg
	ON tg.genre_id = tvg.id
	WHERE t.title NOT IN(
		SELECT t.title
		FROM tv_shows AS `t`
		INNER JOIN tv_show_genres AS `tg`
		ON t.id = tg.show_id
	        INNER JOIN tv_genres AS tvg
        	ON tg.genre_id = tvg.id
        	WHERE tvg.name = "Comedy")
ORDER BY t.title;
