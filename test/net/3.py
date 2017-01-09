import sys
sys.path.append("../lib")
import table
import netstat

def run():
	str=netstat.netstat_nat()
	rows=table.getLines(str)
	tbl=table.makeTable(rows,r"\s*")
	tbl.pop(0)
	html=[]
	open='<table>'
	close='</table>'
	html.append(open)
	for row in tbl:
		html.append('<tr>')
		for column in row:		
			value='<td>{}</td>'.format(column)
			html.append(value)
		html.append('</tr>')
	return html
	

html=run()
print html
