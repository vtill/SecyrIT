	function ajax(){
		var xhr = new XMLHttpRequest();
		xhr.open('GET', '/get_wifi_json', true);
		xhr.onload = function () {
			ajax_onload(xhr.responseText);
	}
	xhr.send(null);	
}

function ajax_onload(response){
	var j=JSON.parse(response);
	var len=j.length;
	var tbl=document.createElement('table');
		tbl.className='table table-striped tablesorter';
	var thead=document.createElement('thead');
	var tbody=document.createElement('tbody');

	var row=document.createElement('tr');
	var cell=document.createElement('th');
		cell.innerHTML='noise';
		row.appendChild(cell);

	var cell=document.createElement('th');
		cell.innerHTML='ssid';
		row.appendChild(cell);

	var cell=document.createElement('th');
		cell.innerHTML='encryption_type';
		row.appendChild(cell);

	var cell=document.createElement('th');
		cell.innerHTML='bitrates';
		row.appendChild(cell);

	var cell=document.createElement('th');
		cell.innerHTML='address';
		row.appendChild(cell);

	var cell=document.createElement('th');
		cell.innerHTML='frequency';
		row.appendChild(cell);

	var cell=document.createElement('th');
		cell.innerHTML='mode';
		row.appendChild(cell);

	var cell=document.createElement('th');
		cell.innerHTML='encrypted';
		row.appendChild(cell);

	var cell=document.createElement('th');
		cell.innerHTML='quality';
		row.appendChild(cell);

	var cell=document.createElement('th');
		cell.innerHTML='signal';
		row.appendChild(cell);

	var cell=document.createElement('th');
		cell.innerHTML='channel';
		row.appendChild(cell);

	thead.appendChild(row);
	tbl.appendChild(thead);

	for (var i=0;i<len;i++){
		var row=document.createElement('tr');
		var cell=document.createElement('td');
			cell.innerHTML=j[i].noise;
			row.appendChild(cell);

		var cell=document.createElement('td');
			cell.innerHTML=j[i].ssid;
			row.appendChild(cell);

		var cell=document.createElement('td');
			cell.innerHTML=j[i].encryption_type;
			row.appendChild(cell);

		var cell=document.createElement('td');
			cell.innerHTML=j[i].bitrates;
			row.appendChild(cell);

		var cell=document.createElement('td');
			cell.innerHTML=j[i].address;
			row.appendChild(cell);

		var cell=document.createElement('td');
			cell.innerHTML=j[i].frequency;
			row.appendChild(cell);

		var cell=document.createElement('td');
			cell.innerHTML=j[i].mode;
			row.appendChild(cell);

		var cell=document.createElement('td');
			cell.innerHTML=j[i].encrypted;
			row.appendChild(cell);

		var cell=document.createElement('td');
			cell.innerHTML=j[i].quality;
			row.appendChild(cell);

		var cell=document.createElement('td');
			cell.innerHTML=j[i].signal;
			row.appendChild(cell);

		var cell=document.createElement('td');
			cell.innerHTML=j[i].hannel;
			row.appendChild(cell);

		tbody.appendChild(row);	
	}
tbl.appendChild(tbody);
$(tbl).tablesorter(); 
document.getElementsByTagName('body')[0].appendChild(tbl);
}
