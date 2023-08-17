-- script that lists all Comedy shows in the database hbtn_0d_tvshows.
SELECT t.title
FROM tv_shows AS t
INNER JOIN tv_show_genres AS tg
ON t.id = tg.show_id
	INNER JOIN tv_genres AS tvg
	ON tvg.id = tg.genre_id
	WHERE tvg.name = "Comedy"
ORDER BY t.title;
