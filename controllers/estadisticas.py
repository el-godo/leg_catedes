@auth.requires(auth.has_membership(role = 'Super')|auth.has_membership(role = 'Jefe de cuerpo')|auth.has_membership(role = 'Director')) 

def menu():

	return dict()
def totales():
	from datetime import datetime, date, time, timedelta
	import calendar
	fecha=datetime.now()
	hoy_anio=fecha.year
	hoy_mes=fecha.month
	set_leg=db(db.legajo.estado).select()
	ctp=0   #contador total de escuela de cadetes-->
	p1=0	#contador de total de cadetes de policia de 1 año
	p2=0 	#contador de total de cadetes de policia de 2 año
	p3=0 	#contador de total de cadetes de policia de 3 año
	p1b=0	#contador de total de cadetes de policia de 1 año de baja
	p2b=0	#contador de total de cadetes de policia de 2 año de baja
	p3b=0	#contador de total de cadetes de policia de 3 año de baja
	cts=0 	#contador total de escuela sevicio penitenciario-->
	s1=0	#contador de total de cadetes del servicio de 1 año
	s2=0	#contador de total de cadetes del servicio de 2 año
	s3=0	#contador de total de cadetes del servicio de 3 año
	s1b=0	#contador de total de cadetes del servicio de 1 año de baja
	s2b=0	#contador de total de cadetes del servicio de 2 año de baja
	s3b=0	#contador de total de cadetes del servicio de 3 año de baja
	atie=0   # Acumulador total de inscriptos en el establecimiento
	ta=0


 






	return dict(set_leg=set_leg,ctp=ctp,p1=p1,p2=p2,p3=p3,p1b=p1b,p2b=p2b,p3b=p3b,s1b=s1b,s2b=s2b,s3b=s3b,
		s1=s1,s2=s2,s3=s3,atie=atie,ta=ta)	

def sin_autorizacion():
	return dict()
def cant_sanciones():
	from datetime import datetime, date, time, timedelta
	import calendar
	dni=request.args[0]
	set_sanciones=db(db.sanciones.dni==dni).select()
	fecha=datetime.now()
	hoy_anio=fecha.year
	hoy_mes=fecha.month
	a="si"
	csa=0#contador sanciones anio
	csm=0#contador sanciones mes
	smgm=0#la sancion mas grande del mes
	smga=0# La sancion mas grande del año
	cpa=0#compara sanciones del año
	cpm=0#compara sanciones del hoy_mes
	csea=0 # compara sancion mas alta del año
	csem=0 # compara sancion mas alta del mes
	idma=0 # id de mayor dias de arresyto del año
	idmm=0 # id de mayor dias de arresyto del mes
	


	return dict(set_sanciones=set_sanciones,hoy_anio=hoy_anio,hoy_mes=hoy_mes,csa=csa,csm=csm,)

def cant_n_medicas():
	from datetime import datetime, date, time, timedelta
	import calendar
	dni=request.args[0]
	set_medicas=db(db.n_medicas.dni==dni).select()
	fecha=datetime.now()
	hoy_anio=fecha.year
	hoy_mes=fecha.month
	a="si"
	cna=0#acumulador de notas por anio
	anmm=0#acumulador de notas por mes
	anaa=0 #acumulador de notas medicas roposo absoluto del anio
	anra=0 #acumulador de notas medicas roposo relativo del anio


	nmgm=0#la nota mas grande del mes
	nmga=0# La nota mas grande del año
	cpa=0#compara nota del año
	cpm=0#compara nota del hoy_mes
	cnmaa=0 # compara nota mas alta del año
	cnemam=0 # compara nota mas alta del mes
	idmna=0 # id de mayor dias de nota del año
	idmnm=0 # id de mayor dias de nota del mes
	comp_anio=0
	abs_a=0 #acumulador de notas reposo absoluto en el año
	arl_a=0 #acumulador de notas medicas reposo relativo en el año
	anra_m=0 #acumulador de notas medicas reposo absoluto en el mes
	anrr_m=0 #acumulador de notas medicas reposo absoluto en el mes



	return dict(set_medicas=set_medicas,hoy_anio=hoy_anio,hoy_mes=hoy_mes,comp_anio=comp_anio,cna=cna,abs_a=abs_a,arl_a=arl_a,
		anmm=anmm,anra_m=anra_m,anrr_m=anrr_m,)


	
	











