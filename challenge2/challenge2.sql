
SELECT manager.first_name , manager.last_name FROM table1
    FULL OUTER JOIN
    manager ON table1.id_manager= manager.id_manager WHERE table1.dt_work_from='20200101 00:00:00.000' and table1.dt_work_to='20200131 00:00:00.000'
UNION ALL
SELECT employee.first_name , employee.last_name FROM table1 
    FULL OUTER JOIN
    manager ON table1.employee= manager.employee WHERE table1.dt_work_from='20200101 00:00:00.000' and table1.dt_work_to='20200131 00:00:00.000'
