WITH jointed AS (
    SELECT e.name AS Employee,e.salary AS Salary,d.name as Department
    FROM Employee e 
    JOIN Department d ON e.departmentId = d.id
),
ranked AS (
    SELECT *,
           DENSE_RANK() OVER (PARTITION BY Department ORDER BY Salary DESC) AS s
    FROM jointed
)
SELECT Employee, Salary, Department
FROM ranked
WHERE s <= 3