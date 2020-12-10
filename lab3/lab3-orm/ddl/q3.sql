CREATE FUNCTION add_num(
	num	integer,
	val	integer)
	RETURNS integer
	AS $$
		BEGIN 
			UPDATE random
			SET rand_num = rand_num + val
			WHERE rand_num = num;
			COMMIT;
			RETURN random_num;
		END;$$ LANGUAGE plpgsql;


CREATE TRIGGER num_rand 
	AFTER UPDATE OF rand_num
		ON random
EXECUTE PROCEDURE add_num(36, 5);