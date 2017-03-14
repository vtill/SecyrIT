/**
 *
 */
function ajax_update(){
	var xhr = new XMLHttpRequest();
	var uri='/update';
	xhr.open('GET', uri, true);
	xhr.onload = function () {
		showResponse(xhr.responseText);
	}
	xhr.send(null);	
}

/**
 *
 */
function showResponse(response){
	//var j=JSON.parse(response);
	//var len=j.length;
	var div=document.getElementById("debug");
	var txt=document.createTextNode(response);	
	div.appendChild(txt);
}

/**
 *
 */
function ajax_restart(){
	var xhr = new XMLHttpRequest();
	var uri='/restart';
	xhr.open('GET', uri, true);
	xhr.onload = function () {
		restart(xhr.responseText);
	}
	xhr.send(null);	
}
/**
 *
 */
function restart(){
	var div=document.getElementById("debug");
	var txt=document.createTextNode(response);	
	div.appendChild(txt);
}
