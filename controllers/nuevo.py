def check():
	#poner un valor por defecto a un campo del formulario    
	form=SQLFORM.factory(    
    Field('valor',label="Ingrese Un Dni/",requires=IS_NOT_EMPTY(error_message='El campo puede estar vacío'))
    
    )         
    	if form.accepts(request,session):
    		response.flash = 'formulario aceptado'
    		redirect(URL(c='nuevo',f='comprobacion',args=[form.vars.valor]))
    	elif form.errors:
        	response.flash = 'el formulario tiene errores'
    	else:
        	response.flash = 'por favor complete el formulario'  
	return dict(form=form)

def comprobacion():
	dni=request.args[0]
	set_cad=db(db.legajo.dni==dni).select()
	tiene=len(set_cad)

    	if tiene==0:
    		redirect(URL(c='nuevo',f='form',args=[dni]))#si no esta en la tabla padron redirecciona
    	else:#si esta en la tabla padron mustro los datos
        	for x in set_cad:
        		foto=x.foto
        		formacion=x.formacion
        		curso=x.curso
        		cuil=x.cuil
            	apellido=x.apellido
            	nombre=x.nombre
            	casa=x.domicilio
            	nacido=x.f_nacimiento
            	sangre=x.g_sanguineo
            	curso=x.curso
            	ingreso=x.f_ingreso
            	celu=x.celu
            	tel=x.fijo
            	tutor=x.tutor
            	t_tutor=x.tel_tutor
                aler=x.alergias
                estado=x.estado


	return dict(formacion=formacion,curso=curso,cuil=cuil,apellido=apellido,nombre=nombre,casa=casa,nacido=nacido,sangre=sangre,
		ingreso=ingreso,celu=celu,tel=tel,tutor=tutor,t_tutor=t_tutor,dni=dni,foto=foto,aler=aler,estado=estado)

@auth.requires(auth.has_membership(role = 'Super')|auth.has_membership(role = 'Jefe de cuerpo')|auth.has_membership(role = 'Oficiales')) 
def form():
    from datetime import datetime, date, time, timedelta
    import datetime
    import time
    import calendar   
    dni=request.args[0]
	 
    form=SQLFORM.factory(
    Field('foto','upload'),
    Field('dni', 'integer',
            requires=[IS_MATCH('^[0-9\s]+$',error_message="Ingrese el DNI"),
            IS_LENGTH(8),
            IS_NOT_EMPTY()],default=dni),       
    Field('cuil',requires=[IS_UPPER(),IS_NOT_EMPTY(error_message='El campo no  puede estar vacio')]),           
    Field('apellido',requires=[IS_UPPER(),IS_NOT_EMPTY(error_message='El campo no  puede estar vacio')]),
    Field('nombre',requires=[IS_UPPER(),IS_NOT_EMPTY(error_message='El campo no  puede estar vacio')]),
    Field('domicilio',requires=IS_UPPER()),
    Field('f_nacimiento',requires=[IS_NOT_EMPTY(error_message='El campo no puede estar vacio ej: 20/02/2000'), IS_DATE(format='%d/%m/%Y'),]),
    Field('g_sanguineo',requires=IS_IN_SET(["RH+","RH-"],error_message='Error elija el grupo sanguineo'),),
    Field('curso',requires=IS_IN_SET(["1","2","3"],error_message='Error elija el curso'),),
    Field('f_ingreso', requires=[IS_NOT_EMPTY(), IS_DATE(format='%d/%m/%Y')]),
    Field('celu','integer'),
    Field('fijo','integer'),
    Field('tutor',requires=IS_UPPER()),
    Field('tel_tutor','integer'),
    Field('formacion',label='Formacion',requires=IS_IN_SET(["Esc. Cadetes","S.Penitenciario"],error_message='Error elija a que formacion pertenece')),
    Field('alergias','text'), 
    Field('estado',label='Estado',requires=IS_IN_SET(["ACTIVO","INACTIVO","BAJA"],error_message='Error elija el estado'),default="ACTIVO"),
        ) 
    
    if form.accepts(request,session):   
        db.legajo.insert(cuil=form.vars.cuil,foto=form.vars.foto,dni=form.vars.dni,nombre=form.vars.nombre,
            apellido=form.vars.apellido,
                estado=form.vars.estado,domicilio=form.vars.domicilio,f_nacimiento=form.vars.f_nacimiento,
                g_sanguineo=form.vars.g_sanguineo,curso=form.vars.curso,f_ingreso=form.vars.f_ingreso,
                celu=form.vars.celu,fijo=form.vars.fijo,tutor=form.vars.tutor,tel_tutor=form.vars.tel_tutor,
                formacion=form.vars.formacion,alergias=form.vars.alergias

                )
 

        response.flash = 'formulario aceptado'
        redirect(URL(c='nuevo',f='cargado'))

    elif form.errors:
            response.flash = 'el formulario tiene errores'
    else:
            response.flash = 'por favor complete el formulario'  
    return dict(form=form)
def cargado():
	return dict()
def pregunta():
	return dict()
@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)
def sin_autorizacion():
    return dict()
    


            
        
	
