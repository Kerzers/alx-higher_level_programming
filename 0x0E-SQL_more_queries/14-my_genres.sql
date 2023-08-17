-- script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter
SELECT tvg.name
FROM tv_genres AS tvg
INNER JOIN tv_show_genres AS tg
ON tvg.id = tg.genre_id
	INNER JOIN tv_shows AS t
	ON t.id = tg.show_id
	WHERE t.title = "Dexter"
ORDER BY tvg.name;
