-- 1. Retreive the latest rental for each customer's first and last name and email address. 
SELECT DISTINCT ON (customer_id)
    r.customer_id,
    r.rental_date,
    c.first_name,
    c.last_name,
    c.email,
FROM rental AS r
INNER JOIN customer AS c
ON r.customer_id = c.customer_id
ORDER BY customer_id, rental_date DESC

-- 2. Retrieve the latest rental date for each title. 
SELECT DISTINCT ON (title)
	r.rental_date,
	f.title
FROM rental AS r 
INNER JOIN inventory AS i 
ON r.inventory_id = i.inventory_id
INNER JOIN film AS f
on i.film_id = f.film_id
ORDER BY title, rental_date DESC;

-- Bonus:
-- Query 2 only returned 958 movies, which means 42 movies are not being rented. 
-- We know that there are 1,000 movies in the `film` table. 
-- Retrieve the film titles of the 42 movies that are not in the `inventory` table. 
SELECT file_id, title
FROM film
WHERE film_id NOT IN
    (SELECT film_id FROM inventory);

--alternate method

SELECT f.film_id, title
FROM film AS f
LEFT JOIN inventory AS i 
ON f.film_id = i.film_id
WHERE i.film_id IS NULL