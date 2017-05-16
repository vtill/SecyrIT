function ajax_createSelect(){
	var xhr = new XMLHttpRequest();
	var uri='/get_ap_con_info_json';
	xhr.open('GET', uri, true);
	xhr.onload = function () {
		createDiv(xhr.responseText);
	}
	xhr.send(null);	
}

function ajax_create(params){
	var xhr = new XMLHttpRequest();
	var uri='/create_netmgr';
	xhr.open('POST', uri, true);
	xhr.onload = function () {
		var div=document.getElementById("debug");
		div.innerHTML=xhr.responseText;
		ajax_createSelect();
	}
	xhr.send(params);	
}

function ajax_activate(params){
	var xhr = new XMLHttpRequest();
	var uri='/activate_netmgr';
	xhr.open('POST', uri, true);
	xhr.onload = function () {
		var div=document.getElementById("debug");
		div.innerHTML=xhr.responseText;
		ajax_createSelect();
	}
	xhr.send(params);	
}

function ajax_delete(params){
	var xhr = new XMLHttpRequest();
	var uri='/delete_netmgr';
	xhr.open('POST', uri, true);
	xhr.onload = function () {
		var div=document.getElementById("debug");
		div.innerHTML=xhr.responseText;
		ajax_createSelect();
	}
	xhr.send(params);	
}


function createDiv(response){
	var j=JSON.parse(response);
	var len=j.length;
	
	var container=document.createElement('div');
	container.id='container';
	container.className='container';

	var div=document.getElementById("container");
	if(div){
		div.parentNode.removeChild(div);
	}

	for(var i=0;i<len;i++){
		if(j[i].SSID!=""){
			var heading=createHeading(j[i].SSID);
			if(j[i].CONNECTION){
				var body=createPaneBodyScheme(j[i].CONNECTION.NAME);
			}else{
				var body=createPaneBodyWifi(j[i].SSID);
			}
			var row=document.createElement('div'); 
			row.className="entry panel";

			if(j[i].ACTIVE=='yes'){
				/*
				var txt=document.createTextNode("aktiv");
				body.appendChild(txt);
				*/
				row.className = "entry active";
			}
			row.appendChild(heading);
			row.appendChild(body);
			container.appendChild(row);
		}

	}
	//document.getElementById('connections').appendChild(container);
	div=document.getElementById('connections');
		div.appendChild(container);
}

function createHeading(txt){
	var heading=document.createElement('div'); 
	heading.className="ssid";
	var span=document.createElement('span');
	span.className='glyphicon glyphicon-signal';
	var str=document.createTextNode(txt);
	heading.appendChild(span);
	heading.appendChild(str);
	return heading;
}

function moruk(txt){
	//evt.preventDefault();
	alert(txt);
}

function createPaneBodyWifi(ssid){
	var body=document.createElement('div'); 
	body.className="actions";
		var form=document.createElement('form');
			//form.action='/create_netmgr';
			form.onsubmit=function(evt){
				evt.preventDefault();
				params="ssid="+encodeURIComponent(ssid)+"&pass="+encodeURIComponent(pass.value);
				moruk(params);
				ajax_create(params);
			};
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
	body.className="actions";
		/** delete */
		var form_delete=document.createElement('form');
			//form_delete.action='/delete_netmgr';
			form_delete.onsubmit=function(evt){
				evt.preventDefault();
				params="ssid="+encodeURIComponent(scheme_name);
				moruk(params);
				ajax_delete(params);
			};
			form_delete.method='POST';
			var input_scheme=document.createElement('input');
				input_scheme.type="hidden";
				input_scheme.name="ssid";
				input_scheme.value=scheme_name;
				form_delete.appendChild(input_scheme);
			var submit=document.createElement('input');	
				submit.type='submit';
				submit.value='loeschen';
				form_delete.appendChild(submit);
		body.appendChild(form_delete);

		/** activate */
		var form_activate=document.createElement('form');
			//form_activate.action='/activate_netmgr';
			form_activate.method='POST';
			form_activate.onsubmit=function(evt){
				evt.preventDefault();
				params="ssid="+encodeURIComponent(scheme_name);
				moruk(params);
				ajax_delete(params);
			};
			var input_scheme=document.createElement('input');
				input_scheme.type="hidden";
				input_scheme.name="ssid";
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
