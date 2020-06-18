from gluon.serializers import json
@auth.requires(auth.has_membership(role = 'Super')|auth.has_membership(role = 'Jefe de cuerpo')|auth.has_membership(role = 'Oficiales')|auth.has_membership(role = 'Director')) 

def listado():
	set_todo=db((db.legajo.estado!="INACTIVO")&(db.legajo.estado!="BAJA")).select()
	mf = json(set_todo)
	return dict(set_todo=set_todo,mf=mf)

	return dict()
def sanciones():
	dni=request.args[0]

	set_todo=db(db.sanciones.dni==dni).select()
	mf = json(set_todo)
	return dict(set_todo=set_todo,mf=mf,dni=dni)	


@auth.requires(auth.has_membership(role = 'Super')|auth.has_membership(role = 'Jefe de cuerpo')|auth.has_membership(role = 'Oficiales')) 
def sancionar():
	dni=request.args[0]
	set_name=db(db.legajo.dni==dni).select().first()
	nombre=set_name.nombre
	apellido=set_name.apellido	
	form=SQLFORM.factory(
	Field('dni','integer',default=dni),
    Field('apellido',requires=IS_UPPER(),default=apellido),
    Field('nombre',requires=IS_UPPER(),default=nombre),  
    Field('memorandum',requires=[IS_NOT_EMPTY(error_message='El campo no puede estar vacio '),IS_UPPER()]),
    Field('fecha','datetime',label="Fecha ",requires=[IS_NOT_EMPTY(error_message='El campo no puede estar vacio, ej: 20/02/2000'), IS_DATE(format='%d/%m/%Y'),]),
    Field('dias','integer'),
    Field('articulo',requires=[IS_NOT_EMPTY(error_message='El campo no puede estar vacio '),IS_UPPER()]),
    Field('encuadramiento','text',requires=IS_UPPER()),    
    Field('descripcion','text',requires=IS_UPPER()),
    Field('sancionador',requires=[IS_NOT_EMPTY(error_message='El campo no puede estar vacio '),IS_UPPER()]),
    Field('fecha_cumpli','datetime',label="Fecha de cumplimiento "
    	,requires=[IS_NOT_EMPTY(error_message='El campo no puede estar vacio, ej: 20/02/2000 '), IS_DATE(format='%d/%m/%Y'),]),
    Field('visacion',requires=[IS_NOT_EMPTY(error_message='El campo no puede estar vacio  '),IS_UPPER()]),

    )
    	if form.accepts(request,session):
    		db.sanciones.insert(dni=dni,nombre=nombre,apellido=apellido,memorandum=form.vars.memorandum,fecha=form.vars.fecha,dias=form.vars.dias,
    			encuadramiento=form.vars.encuadramiento,articulo=form.vars.articulo,descripcion=form.vars.descripcion,sancionador=form.vars.sancionador,
    			fecha_cumpli=form.vars.fecha_cumpli,visacion=form.vars.visacion
    			)
    		redirect(URL(c='sanciones',f='mensaje',args=[dni]))
    	elif form.errors:
        	response.flash = 'el formulario tiene errores'
    	else:
        	response.flash = 'por favor complete el formulario'		

	return dict(form=form,dni=dni,nombre=nombre,apellido=apellido)

def mensaje():
    dni=request.args[0]

    return dict(dni=dni)
@auth.requires(auth.has_membership(role = 'Super')|auth.has_membership(role = 'Jefe de cuerpo')|auth.has_membership(role = 'Oficiales')) 
def editar():
	ide=request.args[0]
	set_sancion=db(db.sanciones.id==ide).select().first()
        dni=set_sancion.dni
        nombre=set_sancion.nombre
        apellido=set_sancion.apellido
        memorandum=set_sancion.memorandum
        fecha=set_sancion.fecha
        dias=set_sancion.dias
        articulo=set_sancion.articulo
        encuadramiento=set_sancion.encuadramiento
        descripcion=set_sancion.descripcion
        sancionador=set_sancion.sancionador
        fecha_cumpli=set_sancion.fecha_cumpli
        visacion=set_sancion.visacion
        form=SQLFORM.factory(
        Field('dni','integer',default=dni),
        Field('apellido',requires=IS_UPPER(),default=apellido),
        Field('nombre',requires=IS_UPPER(),default=nombre),        
        Field('memorandum',requires=[IS_NOT_EMPTY(error_message='El campo no puede estar vacio '),IS_UPPER()],default=memorandum),
        Field('fecha','datetime',label="Fecha ",requires=[IS_NOT_EMPTY(error_message='El campo no puede estar vacio, ej: 20/02/2000'), IS_DATE(format='%d/%m/%Y'),],default=fecha),
        Field('dias','integer',default=dias),
        Field('articulo',requires=[IS_NOT_EMPTY(error_message='El campo no puede estar vacio '),IS_UPPER()],default=articulo),
        Field('encuadramiento','text',requires=IS_UPPER(),default=encuadramiento),    
        Field('descripcion','text',requires=IS_UPPER(),default=descripcion),
        Field('sancionador',requires=[IS_NOT_EMPTY(error_message='El campo no puede estar vacio '),IS_UPPER()],default=descripcion),
        Field('fecha_cumpli','datetime',label="Fecha de cumplimiento "
            ,requires=[IS_NOT_EMPTY(error_message='El campo no puede estar vacio, ej: 20/02/2000 '), IS_DATE(format='%d/%m/%Y'),],default=fecha_cumpli),
        Field('visacion',requires=[IS_NOT_EMPTY(error_message='El campo no puede estar vacio  '),IS_UPPER()],default=visacion),

        )
        if form.accepts(request,session):
            set_sancion.update_record(dni=dni,nombre=nombre,apellido=apellido,memorandum=form.vars.memorandum,fecha=form.vars.fecha,dias=form.vars.dias,
                encuadramiento=form.vars.encuadramiento,articulo=form.vars.articulo,descripcion=form.vars.descripcion,sancionador=form.vars.sancionador,
                fecha_cumpli=form.vars.fecha_cumpli,visacion=form.vars.visacion
                )
            redirect(URL(c='sanciones',f='mensaje',args=[dni]))

        elif form.errors:
            response.flash = 'el formulario tiene errores'
        else:
            response.flash = 'por favor complete el formulario'     

	return dict(form=form,dni=dni,set_sancion=set_sancion,nombre=nombre,apellido=apellido,memorandum=memorandum,fecha=fecha,
        dias=dias,articulo=articulo,encuadramiento=encuadramiento,descripcion=descripcion,sancionador=sancionador,
        fecha_cumpli=fecha_cumpli,visacion=visacion)
def sin_autorizacion():
    return dict()