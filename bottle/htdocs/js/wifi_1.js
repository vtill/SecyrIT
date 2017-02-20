function ajax_createSelect(){
	var xhr = new XMLHttpRequest();
	var uri='/get_wifi_scheme_json';
	xhr.open('GET', uri, true);
	xhr.onload = function () {
		createDiv(xhr.responseText);
	}
	xhr.send(null);	
}

function createDiv(response){
	var j=JSON.parse(response);
	var len=j.length;
	var container=document.createElement('div');
	for(var i=0;i<len;i++){
		var heading=createHeading(j[i].ssid);
		if(j[i].scheme){
			var body=createPaneBodyScheme(j[i].scheme.name);
		}else{
			var body=createPaneBodyWifi(j[i].ssid);
		}

		var row=document.createElement('div'); 
		row.appendChild(heading);
		row.appendChild(body);
		container.appendChild(row);
	}
	document.getElementsByTagName('body')[0].appendChild(container);
}

function createHeading(txt){
	var heading=document.createElement('div'); 
	var str=document.createTextNode(txt);
	heading.appendChild(str);
	return heading;
}

function createPaneBodyWifi(ssid){
	var body=document.createElement('div'); 
		var form=document.createElement('form');
			form.action='create_scheme';
			form.method='POST';
			var input_ssid=document.createElement('input');
				input_ssid.type="hidden";
				input_ssid.name="ssid";
				input_ssid.value=ssid;
			form.appendChild(input_ssid);
			var pass=document.createElement('input');
				pass.type="text";
				pass.name="pass";
			form.appendChild(pass);
			var submit=document.createElement('input');	
				submit.type='submit';
				submit.value='verbinden';
			form.appendChild(submit);
		body.appendChild(form);
	return body;
}

function createPaneBodyScheme(scheme_name){
	var body=document.createElement('div'); 
		/** delete */
		var form_delete=document.createElement('form');
			form_delete.action='delete_scheme';
			form_delete.method='POST';
			var input_scheme=document.createElement('input');
				input_scheme.type="hidden";
				input_scheme.name="scheme";
				input_scheme.value=scheme_name;
			form_delete.appendChild(input_scheme);
			var submit=document.createElement('input');	
				submit.type='submit';
				submit.value='loeschen';
			form_delete.appendChild(submit);
		body.appendChild(form_delete);

		/** activate */
		var form_activate=document.createElement('form');
			form_activate.action='activate_scheme';
			form_activate.method='POST';
			var input_scheme=document.createElement('input');
				input_scheme.type="hidden";
				input_scheme.name="scheme";
				input_scheme.value=scheme_name;
			form_activate.appendChild(input_scheme);
			var submit=document.createElement('input');	
				submit.type='submit';
				submit.value='verbinden';
			form_activate.appendChild(submit);
		body.appendChild(form_activate);

	return body;
}

function createSelect(response){
	var j=JSON.parse(response);
	var len=j.length;
	var container=document.createElement('div');
	var select=document.createElement('select');
	select.name='ssid';


	for (var i=0;i<len;i++){
		var opt=document.createElement('option');
			opt.value=j[i].ssid;
			opt.innerHTML=j[i].ssid;
		select.appendChild(opt);
	}
//document.getElementsByTagName('body')[0].appendChild(select);
document.getElementById('wifi').appendChild(select);
}

function createSubmit(){
	var input=document.createElement('input');	
	input.type='submit';
	input.value='senden';
document.getElementById('wifi').appendChild(input);
}

