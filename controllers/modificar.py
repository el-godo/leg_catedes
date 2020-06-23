@auth.requires(auth.has_membership(role = 'Super')|auth.has_membership(role = 'Jefe de cuerpo')|auth.has_membership(role = 'Oficiales')) 
def modificar():
	
	from datetime import datetime, date, time, timedelta
	dni=request.args(0)
	set_leg=db(db.legajo.dni==dni).select().first()
	
	####################saco datos del legajo################
	
	dni=set_leg.dni
	cuil=set_leg.cuil
	apellido=set_leg.apellido
	nombre=set_leg.nombre
	domicilio=set_leg.domicilio
	f_nacimiento=set_leg.f_nacimiento
	g_sanguineo=set_leg.g_sanguineo
	curso=set_leg.curso
	f_ingreso=set_leg.f_ingreso
	celu=set_leg.celu	
	fijo=set_leg.fijo
	tutor=set_leg.tutor
	tel_tutor=set_leg.tel_tutor
	formacion=set_leg.formacion
	aler=set_leg.alergias
	estado=set_leg.estado
	genero=set_leg.genero

	###########creo el formulario############################

	form=SQLFORM.factory(
	
    Field('dni', 'integer',
			requires=[IS_MATCH('^[0-9\s]+$',error_message="Ingrese el DNI"),
			IS_LENGTH(8),
			IS_NOT_EMPTY()],default=dni),		
    Field('cuil',requires=[IS_UPPER(),IS_NOT_EMPTY(error_message='El campo no  puede estar vacio')],default=cuil),	
    Field('genero',label='genero',requires=IS_IN_SET(["Masculino","Femenino"],error_message='Debe Elegir el Genero'),default=genero), 		
    Field('apellido',requires=[IS_UPPER(),IS_NOT_EMPTY(error_message='El campo no  puede estar vacio')],default=apellido),
    Field('nombre',requires=[IS_UPPER(),IS_NOT_EMPTY(error_message='El campo no  puede estar vacio')],default=nombre),
    Field('domicilio',requires=IS_UPPER(),default=domicilio),
    Field('f_nacimiento',requires=[IS_NOT_EMPTY(error_message='El campo no puede estar vacio ej: 20/02/2000'),
     IS_DATE(format='%d/%m/%Y'),],default=f_nacimiento),

    Field('g_sanguineo',requires=IS_IN_SET(["RH+","RH-"],error_message='Error elija el grupo sanguineo'),default=g_sanguineo),
    Field('curso',requires=IS_IN_SET(["1","2","3"],error_message='Error elija el curso'),default=curso),
    Field('f_ingreso', requires=[IS_NOT_EMPTY(), IS_DATE(format='%d/%m/%Y')],default=f_ingreso),
    Field('celu','integer',default=celu),
    Field('fijo','integer',default=fijo),
    Field('tutor',requires=IS_UPPER(),default=tutor),
    Field('tel_tutor','integer',default=tel_tutor),
    Field('formacion',label='Formacion',requires=IS_IN_SET(["Esc. Cadetes","S.Penitenciario"],
    	error_message='Error elija a que formacion pertenece'),default=formacion),
    Field('alergias','text',default=aler), 
    Field('estado',label='Estado',requires=IS_IN_SET(["ACTIVO","BAJA POR SACIONES","BAJA VONLUNTARIA","RECIBIDO"],error_message='Error elija el estado'),default=estado),
    	) 
	if form.accepts(request,session):
		set_leg.update_record(dni=form.vars.dni,cuil=form.vars.cuil,apellido=form.vars.apellido,nombre=form.vars.nombre,
				domicilio=form.vars.domicilio,f_nacimiento=form.vars.f_nacimiento,g_sanguineo=form.vars.g_sanguineo,curso=form.vars.curso,
				f_ingreso=form.vars.f_ingreso,celu=form.vars.celu,fijo=form.vars.fijo,tutor=form.vars.tutor,tel_tutor=form.vars.tel_tutor,
				formacion=form.vars.formacion,aler=form.vars.alergias,estado=form.vars.estado,genero=form.vars.genero)
		
    		response.flash = 'formulario aceptado'
    		redirect(URL(c='modificar',f='modificado',args=dni))
    	elif form.errors:
        	response.flash = 'el formulario tiene errores'
    	else:
        	response.flash = 'por favor complete el formulario'  
	

	return dict(form=form,set_leg=set_leg)

def modificado():
	dni=request.args[0]

	return dict(dni=dni)
def sin_autorizacion():
	return dict()