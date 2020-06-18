		
from gluon.serializers import json
@auth.requires(auth.has_membership(role = 'Super')|auth.has_membership(role = 'Jefe de cuerpo')|auth.has_membership(role = 'Enfermer@s')|auth.has_membership(role = 'Director')) 


def medica():
	set_todo=db((db.legajo.estado!="INACTIVO")&(db.legajo.estado!="BAJA")).select()
	mf = json(set_todo)
	return dict(set_todo=set_todo,mf=mf)
def mostrar():
	dni=request.args[0]
	set_todo=db(db.n_medicas.dni==dni).select()
	cuanto=len(set_todo)
	cuanto=int(cuanto)
	
	if cuanto==0:
		redirect(URL(c='medica',f='mensaje',args=[dni]))
	else:
		mf = json(set_todo)
 
	return dict(dni=dni,set_todo=set_todo,cuanto=cuanto,mf=mf)#(set_todo=set_todo,mf=mf)
def mensaje():
	dni=request.args[0]
	return dict(dni=dni)
def ingreso():
	from datetime import datetime, date, time, timedelta
	import datetime
	import time
	import calendar
	
	dni=request.args[0]
	set_leg=db(db.legajo.dni==dni).select().first()
	nombre=set_leg.nombre
	apellido=set_leg.apellido

	form=SQLFORM.factory(
	Field('dni','integer'),
    Field('apellido',requires=IS_UPPER()),
    Field('nombre',requires=IS_UPPER()),
	Field('fecha','datetime',label="fecha de ingreso de nota",requires=[IS_NOT_EMPTY(error_message='El campo no puede estar vacio ej: 20/02/2000'), IS_DATE(format='%d/%m/%Y'),]),
    Field('diagnostico',requires=IS_UPPER()),
    Field('reposo',
			requires=[IS_MATCH('^[0-9\s]+$',error_message="Ingrese la cantidad de dias con numeros"),
						IS_NOT_EMPTY()]),		 
    Field('t_reposo',requires=IS_IN_SET(["ABSOLUTO","RELATIVO"],error_message='Elija el tipo de reposo'),),
    Field('medico',requires=IS_UPPER(),label="Medico otorgante"), 
    Field('fecha_c','datetime',label="fecha de cumplimiento",requires=[IS_NOT_EMPTY(error_message='El campo no puede estar vacio ej: 20/02/2000'), IS_DATE(format='%d/%m/%Y'),]),

		)
	if form.accepts(request,session):
		db.n_medicas.insert(dni=dni,apellido=apellido,nombre=nombre,fecha=form.vars.fecha,diagnostico=form.vars.diagnostico,
			reposo=form.vars.reposo,t_reposo=form.vars.t_reposo,medico=form.vars.medico,fecha_c=form.vars.fecha_c)	
		redirect(URL(c='medica',f='cargado',args=[dni]))
	elif form.errors:
        	response.flash = 'el formulario tiene errores'
    	else:
        	response.flash = 'por favor complete el formulario'
	return dict(set_leg=set_leg,nombre=nombre,apellido=apellido,dni=dni,form=form)
@auth.requires(auth.has_membership(role = 'Super')|auth.has_membership(role = 'Jefe de cuerpo')|auth.has_membership(role = 'Enfermer@s')) 	
def editar():
	id=request.args[0]
	set_medica=db(db.n_medicas.id==id).select().first()
	dni=set_medica.dni
	apellido=set_medica.apellido
	nombre=set_medica.nombre
	fecha=set_medica.fecha
	diagnostico=set_medica.diagnostico
	reposo=set_medica.reposo
	t_reposo=set_medica.t_reposo
	medico=set_medica.medico
	fecha_c=set_medica.fecha_c
	form=SQLFORM.factory(
	Field('dni','integer'),
    Field('apellido',requires=IS_UPPER()),
    Field('nombre',requires=IS_UPPER()),
	Field('fecha','datetime',label="fecha de ingreso de nota",requires=[IS_NOT_EMPTY(error_message='El campo no puede estar vacio ej: 20/02/2000'), IS_DATE(format='%d/%m/%Y'),],default=fecha),
    Field('diagnostico',requires=IS_UPPER(),default=diagnostico),
    Field('reposo',
			requires=[IS_MATCH('^[0-9\s]+$',error_message="Ingrese la cantidad de dias con numeros"),
						IS_NOT_EMPTY()],default=reposo),		 
    Field('t_reposo',requires=IS_IN_SET(["ABSOLUTO","RELATIVO"]
    	,error_message='Elija el tipo de reposo'),default=t_reposo),
    Field('medico',requires=IS_UPPER(),label="Medico otorgante",default=medico), 
    Field('fecha_c','datetime',label="fecha de cumplimiento"
    	,requires=[IS_NOT_EMPTY(error_message='El campo no puede estar vacio ej: 20/02/2000')
    	, IS_DATE(format='%d/%m/%Y'),],default=fecha_c),

		)
	if form.accepts(request,session):
		set_medica.update_record(dni=dni,apellido=apellido,nombre=nombre,fecha=form.vars.fecha,diagnostico=form.vars.diagnostico,
			reposo=form.vars.reposo,t_reposo=form.vars.t_reposo,medico=form.vars.medico,fecha_c=form.vars.fecha_c)
		redirect(URL(c='medica',f='mensajes',args=[dni]))
	elif form.errors:
        	response.flash = 'el formulario tiene errores'
    	else:
        	response.flash = 'por favor complete el formulario'


	return dict(id=id,form=form,dni=dni,apellido=apellido,nombre=nombre,fecha=fecha,
		diagnostico=diagnostico,reposo=reposo,t_reposo=t_reposo,medico=medico,fecha_c=fecha_c)
def cargado():
	return dict()
def mensajes():
	dni=id=request.args[0]

	return dict(dni=dni)
def sin_autorizacion():
	return dict()




