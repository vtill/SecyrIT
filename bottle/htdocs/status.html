 <!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Title of the document</title>
<link rel="stylesheet" type="text/css" href="css/bootstrap.min.css">
<link rel="stylesheet" type="text/css" href="css/status.css">
<script src="js/jquery-3.1.1.min.js" type="text/javascript"></script>	
<script src="js/bootstrap.min.js" type="text/javascript"></script>
<script src="js/jquery.tablesorter.min.js" type="text/javascript"></script>	
</head>
<!--                             -->
<body>
<ul class="nav nav-tabs">
	<li role="presentation"><a href="status.html">alle Verbindungen</a></li>
	<li role="presentation"><a href="wifi_2.html">wifi auswahlen</a></li>
	<li role="presentation" onclick="location.reload(true);"><a href="#">seite neuladen</a></li>
</ul>

<div class="row">
  <div id="output" class="container">
		<div id="reload"><button onclick="location.reload(true);">neu laden</button></div>
		<table id="status_table" class="table table-striped tablesorter"></table>
	</div>
</div>

<div class="modal fade" id="myModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
        <h4 class="modal-title" id="myModalLabel">Modal title</h4>
      </div>
      <div class="modal-body" id="pcapResponse">
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
        <button type="button" class="btn btn-primary">Save changes</button>
      </div>
    </div>
  </div>
</div>


<!--                             -->
<script type="text/javascript">

	function aGetPcap(dstIP,srcPort){
		params="dstIP=" +encodeURIComponent(dstIP)
			+"&srcPort="  +encodeURIComponent(srcPort);
		var xhr = new XMLHttpRequest();
		xhr.open('POST', 'pcap_read', true);
		xhr.onload = function () {
			getPcap(xhr.responseText);
		}

		xhr.send(params);	
	}

	function getPcap(response){
		var modal1=document.getElementById("myModal");
		var body1=document.getElementById("pcapResponse");
		
		var regex=/\\n\\t/g;
		var replace="<br />";
		response=response.replace(regex,replace);
		var regex=/\\n/g;
		response=response.replace(regex,replace);

		body1.innerHTML="<pre>"+response+"</pre>";
		//var txt=document.createTextNode(response);
		//body.appendChild(txt);
		console.log(response.length);
		$("#myModal").modal();
	}	

	function ajax(){
		var xhr = new XMLHttpRequest();
		xhr.open('GET', '/status_nf_json', true);
		xhr.onload = function () {
		// Request finished. Do processing here.
			//var elem=document.getElementsByTagName("body")[0];
			var elem=document.getElementById("output");
			var j=JSON.parse(xhr.responseText);
			var j=JSON.parse(j);
			var tbl=document.getElementById("status_table");

			console.log(j.length);
			var thead=document.createElement("thead");
			var tr=document.createElement("tr");

			var td=document.createElement("th");
				td.innerHTML="Destination IP";
				tr.appendChild(td);
			var td=document.createElement("th");
				td.innerHTML="Destination Hostname";
				tr.appendChild(td);
			var td=document.createElement("th");
				td.innerHTML="Destination Country";
				tr.appendChild(td);
			var td=document.createElement("th");
				td.innerHTML="Dport_name";
				tr.appendChild(td);
			var td=document.createElement("th");
				td.innerHTML="Delta_time";
				tr.appendChild(td);
			var td=document.createElement("th");
				td.innerHTML="Packet Traffic";
				tr.appendChild(td);
			var td=document.createElement("th");
				td.innerHTML="Daten Traffic in Bytes";
				tr.appendChild(td);
			var td=document.createElement("th");
				td.innerHTML="Trans Layer Protocol Name";
				tr.appendChild(td);
			thead.appendChild(tr);
			tbl.appendChild(thead);

			var tbody=document.createElement("tbody");
			var gatewayIP="10.254.239.1";
			for (i=0;i<j.length;i++){
				if(j[i]==null || j[i].cons[0].dst==gatewayIP||j[i].cons[0].src==gatewayIP){
					continue;
				}
				var tr=document.createElement("tr");
				
				var td=document.createElement("td");
					td.innerHTML=j[i].cons[0].dst;
					tr.appendChild(td);
				var td=document.createElement("td");
					td.innerHTML=j[i].cons[0].dst_name;
					tr.appendChild(td);
				var td=document.createElement("td");
					td.innerHTML=j[i].cons[0].dst_country;
					tr.appendChild(td);
				var td=document.createElement("td");
					td.innerHTML=j[i].cons[0].dport_name;
					tr.appendChild(td);
				var td=document.createElement("td");
					td.innerHTML=j[i].delta_time;
					tr.appendChild(td);
				var td=document.createElement("td");
					td.innerHTML=Number(j[i].cons[0].packets) + Number(j[i].cons[1].packets);
					tr.appendChild(td);
				var td=document.createElement( "td" );
					td.innerHTML=Number(j[i].cons[0].bytes) + Number(j[i].cons[1].bytes);
					tr.appendChild(td);
				var td=document.createElement("td");
					td.innerHTML=j[i].proto_name;
					tr.appendChild(td);
				var td=document.createElement("td");
					var btn=document.createElement("button");
						btn.sport=j[i].cons[0].sport;
						btn.dst=j[i].cons[0].dst;
						btn.addEventListener("click",function(){
							aGetPcap(this.dst,this.sport);
						});
						btn.style.width="30px";
						btn.style.height="30px";
					td.appendChild(btn);
					tr.appendChild(td);

				tbody.appendChild(tr);
			}

			tbl.appendChild(tbody);
			elem.appendChild(tbl);
			$("#status_table").tablesorter(); 
		};
		xhr.send(null);	
	}

$(document).ready(function(){
	ajax();
}); 

</script>

</body>
</html> 
