select animal_id, name,
       case when sex_upon_intake like('%Neutered%') THEN 'O' 
            when sex_upon_intake like('%Spayed%') THEN 'O' 
       else 'X' END as 중성화
from animal_ins
order by animal_id

SELECT ANIMAL_ID, NAME, 
CASE
    WHEN(SEX_UPON_INTAKE REGEXP 'Neutered|Spayed') THEN 'O'
    ELSE 'X'
END AS '중성화'
FROM ANIMAL_INS

-- 코드를 입력하세요
select i.animal_id, i.name
from animal_ins i
join animal_outs o
on i.animal_id = o.animal_id
order by datediff(o.datetime, i.datetime) desc
limit 2

SELECT ANIMAL_ID, NAME, DATE_FORMAT(DATETIME, '%Y-%m-%d') AS 날짜
FROM ANIMAL_INS
ORDER BY ANIMAL_ID ASC;

-- 코드를 입력하세요
SELECT hour(DATETIME), COUNT(*)
from ANIMAL_OUTS
where hour(DATETIME) >= hour("09:00:00") and hour(DATETIME) < hour('20:00:00')
group by hour(DATETIME)

-- 코드를 입력하세요

SELECT A.cart_id
FROM
    (SELECT cart_id FROM cart_products WHERE name = '우유') A
    JOIN
    (SELECT cart_id FROM cart_products WHERE name = '요거트') B
    ON (A.cart_id = B.cart_id)
ORDER BY A.cart_id

SELECT I.ANIMAL_ID, I.ANIMAL_TYPE, I.NAME
FROM ANIMAL_INS I
JOIN ANIMAL_OUTS O ON I.ANIMAL_ID = O.ANIMAL_ID 
WHERE I.SEX_UPON_INTAKE LIKE 'Intact%' 
AND O.SEX_UPON_OUTCOME NOT LIKE 'Intact%'
ORDER BY I.ANIMAL_ID