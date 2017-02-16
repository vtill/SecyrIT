	function ajax_createSelect(){
		var xhr = new XMLHttpRequest();
		xhr.open('GET', '/get_wifi_json', true);
		xhr.onload = function () {
			createSelect(xhr.responseText);
			createSubmit();
	}
	xhr.send(null);	
}

function createSelect(response){
	var j=JSON.parse(response);
	var len=j.length;
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

