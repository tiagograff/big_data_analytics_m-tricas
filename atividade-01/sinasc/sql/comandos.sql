use SINASC;
select * from dnrs2022;

select 
	dn.*,
    sx.nome
from 
	dnrs2022 as dn 
right join sexo as sx on sx.idsexo = dn.sexo;

