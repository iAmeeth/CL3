from ubidots import ApiClient
from flask import Flask
from flask import render_template
from flask import request

app=Flask(__name__)
tok='Pju7Z1oIXlJW23ATz4mxG3OAEUvhPX'
@app.route('/')
def index():
	return render_template('index.html',msg=None)

@app.route('/create',methods=["GET"])
def create():
	name=request.args['name']
	api=ApiClient(token=tok)
	api.create_datasource({"name":name})
	return render_template('index.html',msg="Datastore created")

@app.route('/insert',methods=["GET"])
def insert():
	vname=request.args['vname']
	vunit=request.args['vunit']
	vval=request.args['vval']	
	api=ApiClient(token=tok)
	vari=api.get_datasources()[0].create_variable({"name":vname,"unit":vunit})
	vari.save_values([{"timestamp":12345,"value":vval}])
	return render_template('index.html',msg="Variable Added")

@app.route('/getvalues',methods=["GET"])
def getvalues():
	temp=""
	api=ApiClient(token=tok)
	ds=api.get_datasources()[0]
	vari=ds.get_variables()[0]
	value=vari.get_values()[0]['value']
	temp="Variable retrieved = "+str(vari)+" Value= "+str(value)
	return render_template('index.html',msg=temp)


if __name__=="__main__":
	app.run(debug=True)
