SELECT manager.first_name , manager.last_name FROM table1
    JOIN
    manager ON table1.id_manager= manager.id_manager WHERE table1.dt_work_from='20200101 00:00:00' and table1.dt_work_to='20200131'
UNION ALL
SELECT employee.first_name , employee.last_name FROM table1 
    JOIN
    employee ON table1.id_employee= employee.id_employee WHERE table1.dt_work_from='20200101 00:00:00' and table1.dt_work_to='20200131'
